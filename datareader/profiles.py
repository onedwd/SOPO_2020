
import numpy as np
import glob
import pandas as pd
import xarray as xr

# not necessary 
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


def read_ctd(archive_dir, year, type):
# list_of_bot = archive_dir_test+'netCDF_Data/BOT/'+str(year) + '/1950-050-0002.bot.nc'
    list_of_profiles = glob.glob(archive_dir + 'netCDF_Data/' 
                                 + str(type) + '/' + str(year) + '/*.nc', recursive=True)
    lats = np.zeros((len(list_of_profiles)))
    lons = np.zeros((len(list_of_profiles)))
    first_p = np.zeros((len(list_of_profiles)))
    print(lats)
    print(lats.shape)
    i = 0
    for bot in list_of_profiles:

        data_xr = xr.open_dataset((bot))
        print(data_xr)
        input('xr?')
        # print(data_xr.longitude)
        lons[i] = data_xr.longitude
        lats[i] = data_xr.latitude
        # first_p[i] = data_xr.PRESPR01[0]
        # if data_xr.PRESPR01[0] > 10.:
        #     print(bot)

        i = i + 1
        # print(data_xr.PRESPR01[0].values)
    data_in = {'lats': lats,
               'lons': lons,
               'first_pres': first_p}
    print(data_in)
    data = pd.DataFrame(data=data_in, columns=['lats', 'lons', 'first_pres'])
    plt.plot(data.first_pres)
    plt.savefig('./plots/ctd_' + str(year) + '.png')
    plt.show()
    data.to_csv('./data/ctd_' + str(year) + '.csv')
    print(data_xr)

    return data


def count_ctd(archive_dir, years, type):
    counts = pd.DataFrame(data=None, index=np.arange(years[0], years[-1]), columns=['CTD_counts'])
    for year in years:
        try:
            list_of_profiles = glob.glob(archive_dir + 'netCDF_Data/'
                                         + str(type) + '/' + str(year) + '/*.nc', recursive=True)
            print(len(list_of_profiles))
            # lats = np.zeros((len(list_of_profiles)))
            # lons = np.zeros((len(list_of_profiles)))
            # first_p = np.zeros((len(list_of_profiles)))
            # print(lats)
            # print(lats.shape)
            # i = 0
            # for bot in list_of_profiles:
            #
            #     data_xr = xr.open_dataset((bot))
            #     # print(data_xr)
            #     # print(data_xr.longitude)
            #     lons[i] = data_xr.longitude
            #     lats[i] = data_xr.latitude
            #     # first_p[i] = data_xr.PRESPR01[0]
            #     # if data_xr.PRESPR01[0] > 10.:
            #     #     print(bot)
            #
            #     i = i + 1
            #     # print(data_xr.PRESPR01[0].values)
            # data_in = {'lats': lats,
            #            'lons': lons,
            #            'first_pres': first_p}
            # print(data_in)
            # pac_mask = (data_in['lats'] <= 60.)
            # print(data_in[pac_mask])
            # print(pac_mask.sum())
            # counts.iloc[year, 'CTD_counts'] = pac_mask.sum()
            counts.ix[year, 'CTD_counts'] = len(list_of_profiles)
        except:
            pass
    # print(data_xr)
    counts.to_csv('./data/ctd_counts.csv')
    # return data