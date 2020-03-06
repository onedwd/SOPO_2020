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



def make_map(year, data, type):
    print(data)
    # data = data.mask([data.lats>=58.])
    # data = data.mask(data.lats >= 58.)
    pac_mask = (data['lats'] <= 60.)
    print(data[pac_mask])
    print(pac_mask.sum())

    # Make map:
    print(min(data.lats), min(data.lons))
    print(max(data.lats), max(data.lons))
    print(data.lons)

    left_lon = -145#-135.#-129.6
    right_lon = -120.5 #-120. #-128.3
    bot_lat = 46 #47.#53.3
    top_lat = 58#57. #54.05

    m = Basemap(llcrnrlon=left_lon, llcrnrlat=bot_lat,
                urcrnrlon=right_lon, urcrnrlat=top_lat,
                projection='lcc', #width=40000, height=40000,
                # projection='cyl',
                resolution='h', lat_0=53.4, lon_0=-129.0)
    m.drawcoastlines(color='0.2', linewidth=0.2)
    m.drawmapboundary(fill_color='white')
    m.fillcontinents(color='0.8')
    m.drawmeridians(np.arange(-145, -108, 10),
                      labels=[False, False, False, True], fontsize=16)
    m.drawparallels(np.arange(40, 60, 3),
                      labels=[True, False, False, False], fontsize=16)
    x, y = m(data.lons.values, data.lats.values)

    # m.plot(x, y, 'ro', markersize=4, )
    m.scatter(x, y, c='r', alpha=0.2)
    plt.title(str(year) + ' ' + type + ' Pacific Profiles ' + str(pac_mask.sum()), fontsize=16)
    plt.savefig('./plots/' + str(year) + type +'_map.png')
    plt.show()
    return m


def make_allmap(data, type):
    print(data)
    # data = data.mask([data.lats>=58.])
    # data = data.mask(data.lats >= 58.)
    pac_mask = (data['latitude'] <= 68.) & (data['longitude'] <= -118.)
    # pac_mask = (data['latitude'] >= 68.) #& (data['longitude'] <= -118.)
    # pac_mask =
    print(data[pac_mask])
    print(pac_mask.sum())

    # Make map:
    print(min(data.latitude), min(data.longitude))
    print(max(data.latitude), max(data.longitude))
    print(data.longitude)

    left_lon = -179#-135.#-129.6
    right_lon = -115 #-120. #-128.3
    bot_lat = 20 #47.#53.3
    top_lat = 70 #57. #54.05

    m = Basemap(llcrnrlon=left_lon, llcrnrlat=bot_lat,
                urcrnrlon=right_lon, urcrnrlat=top_lat,
                # projection='lcc',  #width=40000, height=40000,
                projection='cyl',  # width=40000, height=40000,
                # projection='npstere',  # width=40000, height=40000,
                resolution='h', lat_0=53.4, lon_0=-129.0)

    m.drawcoastlines(color='0.2', linewidth=0.2)
    m.drawmapboundary(fill_color='white')
    m.fillcontinents(color='0.7')
    m.drawmeridians(np.arange(-175, -109, 15),
                    labels=[False, False, False, True], fontsize=16)
    m.drawparallels(np.arange(20, 101, 10),
                    labels=[True, False, False, False], fontsize=16)
    # m.drawmeridians(np.arange(-175, 1, 25),
    #                   labels=[False, True, False, True], fontsize=16)
    # m.drawparallels(np.arange(20, 101, 10),
    #                   labels=[True, False, False, False], fontsize=16)

    x, y = m(data[pac_mask].longitude.values, data[pac_mask].latitude.values)

    # m.plot(x, y, 'ro', markersize=3, alpha=0.2)
    m.scatter(x, y, c='r', alpha=0.2)
    plt.title('1965 - 2019 ' + type + ' Pacific Profiles ' + str(pac_mask.sum()), fontsize=16)
    plt.savefig('./plots/all_pac_' + type +'_map.png')
    plt.show()
    return m


def make_all_arcticmap(data, type):
    print(data)
    # data = data.mask([data.lats>=58.])
    # data = data.mask(data.lats >= 58.)
    # pac_mask = (data['latitude'] <= 68.) & (data['longitude'] <= -118.)
    pac_mask = (data['latitude'] >= 68.) #& (data['longitude'] <= -118.)
    # pac_mask =
    print(data[pac_mask])
    print(pac_mask.sum())

    # Make map:
    print(min(data.latitude), min(data.longitude))
    print(max(data.latitude), max(data.longitude))
    print(data.longitude)

    left_lon = -179#-135.#-129.6
    right_lon = -115 #-120. #-128.3
    bot_lat = 20 #47.#53.3
    top_lat = 70 #57. #54.05

    # m = Basemap(llcrnrlon=left_lon, llcrnrlat=bot_lat,
    #             urcrnrlon=right_lon, urcrnrlat=top_lat,
    #             # projection='lcc',  #width=40000, height=40000,
    #             projection='cyl',  # width=40000, height=40000,
    #             # projection='npstere',  # width=40000, height=40000,
    #             resolution='h', lat_0=53.4, lon_0=-129.0)
    m = Basemap(#llcrnrlon=left_lon, llcrnrlat=bot_lat,
                #urcrnrlon=right_lon, urcrnrlat=top_lat,
                # projection='lcc',  #width=40000, height=40000,
                # projection='cyl',  # width=40000, height=40000,
                projection='npstere',  # width=40000, height=40000,
                boundinglat=67,
                resolution='h', lat_0=90, lon_0=-129.0)
    m.drawcoastlines(color='0.2', linewidth=0.2)
    m.drawmapboundary(fill_color='white')
    m.fillcontinents(color='0.7')
    # m.drawmeridians(np.arange(-175, -109, 15),
    #                   labels=[False, False, False, True], fontsize=16)
    # m.drawparallels(np.arange(20, 101, 10),
    #                   labels=[True, False, False, False], fontsize=16)
    m.drawmeridians(np.arange(-175, 1, 25),
                      labels=[False, True, False, True], fontsize=16)
    m.drawparallels(np.arange(20, 101, 10),
                      labels=[True, False, False, False], fontsize=16)
    x, y = m(data[pac_mask].longitude.values, data[pac_mask].latitude.values)

    # m.plot(x, y, 'ro', markersize=3, alpha=0.2)
    m.scatter(x, y, c='r', alpha=0.2)
    plt.title('1965 - 2019 ' + type + ' Arctic Profiles ' + str(pac_mask.sum()), fontsize=16)
    plt.savefig('./plots/all_arctic' + type +'_map.png')
    plt.show()
    return m