import netCDF4
import pandas as pd
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib
import xarray as xr
# import matplotlib.pyplot as plt
# import numpy as np
# import argparse
# import common_functions as cf
# import os
# import scipy.io as sio
# from netCDF4 import Dataset
# import matplotlib.tri as tri
from mpl_toolkits.basemap import Basemap, shiftgrid, cm
# from scipy.spatial import Delaunay
# from pylab import ginput
# import cPickle as pickle
# import scipy as spy
# from scipy.interpolate import griddata
# import os
import matplotlib.pyplot as plt
# import csv
# import xarray as xr
import glob
import h5py
import dask.array as da
import numpy as np
import datareader as dr



def make_map(data):
    print(data)
    # Make map:
    print(min(data.lats), min(data.lons))
    print(max(data.lats), max(data.lons))
    print(data.lons)

    left_lon = -146#-135.#-129.6
    right_lon = -120.5 #-120. #-128.3
    bot_lat = 45 #47.#53.3
    top_lat = 56#57. #54.05

    m = Basemap(llcrnrlon=left_lon, llcrnrlat=bot_lat,
                urcrnrlon=right_lon, urcrnrlat=top_lat,
                projection='lcc', #width=40000, height=40000,
                resolution='h', lat_0=53.4, lon_0=-129.0)
    m.drawcoastlines(color='0.2', linewidth=0.2)
    m.drawmapboundary(fill_color='white')
    m.fillcontinents(color='0.8')
    m.drawmeridians(np.arange(-146, -110, 10),
                      labels=[False, False, True, True], fontsize=16)
    m.drawparallels(np.arange(45, 56, 3),
                      labels=[True, False, False, False], fontsize=16)
    x, y = m(data.lons.values, data.lats.values)

    m.plot(x, y, 'ro', markersize=4, )
    plt.show()


# Year that is being processed
year = 2019
read_all = True

# directory that stores all osd_archive_data
archive_dir_test = '/run/user/1000/gvfs/smb-share:server=sid01hnas01b,share=osd_data/OSD_DataArchive/osd_data_final/'
if read_all:

    archive_dir_test = '/run/user/1000/gvfs/smb-share:server=sid01hnas01b,share=osd_data/OSD_DataArchive/osd_data_final/'

    # list_of_bot = archive_dir_test+'netCDF_Data/BOT/'+str(year) + '/1950-050-0002.bot.nc'
    list_of_profiles = glob.glob(archive_dir_test + 'netCDF_Data/CTD/' + str(year) + '/*.nc', recursive=True)
    lats = np.zeros((len(list_of_profiles)))
    lons = np.zeros((len(list_of_profiles)))
    first_p = np.zeros((len(list_of_profiles)))
    print(lats)
    print(lats.shape)
    i = 0
    for bot in list_of_profiles:
        data_xr = xr.open_dataset((bot))
        # print(data_xr.longitude)
        lons[i] = data_xr.longitude
        lats[i] = data_xr.latitude
        first_p[i] = data_xr.PRESPR01[0]
        i = i + 1
        # print(data_xr.PRESPR01[0].values)
    data_in = {'lats': lats,
               'lons': lons,
               'first_pres': first_p}
    print(data_in)
    data = pd.DataFrame(data=data_in, columns=['lats', 'lons', 'first_pres'])
    plt.plot(data.first_pres)
    plt.show()
    data.to_csv('/home/wand/PycharmProjects/adcp_analysis/oceanprocess/cioos/ctd_'+str(year) + '.csv')
    print(data_xr)
    # make_map(data)

else:
    data = pd.read_csv('/home/wand/PycharmProjects/adcp_analysis/oceanprocess/cioos/ctd_'+str(year) + '.csv')
    make_map(data)


print(lats, lons)
print(xr.open_dataset(list_of_profiles[0]))
file1 = xr.open_dataset(list_of_profiles[0])
print(file1.latitude)
#list_of_paths = glob.glob('C:/Users/sam/Desktop/myfolder/**/*.nc', recursive=True)
nc = xr.open_mfdataset(list_of_profiles, parallel=True, concat_dim="z", )
                  # data_vars='TEMPS901')
print(nc)