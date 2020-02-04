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
    plt.savefig('./plots/map.png')
    plt.show()
    return m