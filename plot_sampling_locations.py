# Plot CTD sampling locations

# Read ctd and bottle lon/lat data into csv files

import os
import matplotlib.pyplot as plt
import csv
import xarray as xr

bot_dir = '/home/hourstonh/Documents/data/BOT_nc/2019'
ctd_dir = '/home/hourstonh/Documents/data/CTD_nc/2019'

ctd_csv = "/home/hourstonh/Documents/Hana_D_drive/SOPO_2020/ctd_2019_lat_lon.csv"
bot_csv = "/home/hourstonh/Documents/Hana_D_drive/SOPO_2020/bot_2019_lat_lon.csv"

# Can change these to bot_dir, bot_csv, respectively
type_dir = ctd_dir
out_csv = ctd_csv

os.chdir(type_dir)

# Write csv files of lon and lat; comment out after done
with open(out_csv, mode = 'w') as infile:
    writer = csv.writer(infile, delimiter=',')

    # Add header
    writer.writerow(['file', 'latitude', 'longitude'])

    # iterate through all 2019 ctd files
    for f in os.listdir(type_dir):
        print(f)
        d = xr.open_dataset(f)
        lat = d.latitude.data
        lon = d.longitude.data
        writer.writerow([f, lat, lon])


""""# Create plots:
# https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6

from shapely.geometry import Point
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame

os.chdir("/home/hourstonh/Documents/Hana_D_drive/SOPO_2020/")

# Can change to lon_lat_csv = bot_csv
lon_lat_csv = ctd_csv

df = pd.read_csv(lon_lat_csv, delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

world.plot()

"""