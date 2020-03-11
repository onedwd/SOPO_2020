import fiona
from fiona import collection
from shapely.geometry import mapping, shape
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import geopandas as gpd
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('xtick', labelsize=16)
matplotlib.rc('ytick', labelsize=16)
import cartopy.crs as ccrs

# Open a file for reading. We'll call this the "source."
pac_mpa = gpd.read_file("./data/DFO_MPA_wgs84/DFO_MPA_wgs84.shp")
print(pac_mpa.NAME_E)
print(pac_mpa)
print(gpd.GeoDataFrame(pac_mpa.iloc[0]))
ctd = pd.read_csv("./data/IOS_CTD_Profiles_5a5a_a665_bb0c.csv")
ctd['year'] = pd.DatetimeIndex(ctd['time']).year
print(ctd)
gdf_ctd = gpd.GeoDataFrame(ctd, geometry=gpd.points_from_xy(ctd.longitude, ctd.latitude))
print(gdf_ctd)
joinDF = gpd.sjoin(gdf_ctd, pac_mpa, how='right', op="within")
print(joinDF['NAME_E'])
mpa1 = joinDF[joinDF['NAME_E']==pac_mpa.NAME_E[0]]
mpa2 = joinDF[joinDF['NAME_E']==pac_mpa.NAME_E[1]]
mpa3 = joinDF[joinDF['NAME_E']==pac_mpa.NAME_E[4]]

print(joinDF.year.min())
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 8),  squeeze=True,sharex=True,)
hist1 = mpa1['year'].hist(ax=axs[0], color='b', bins=range(joinDF.year.min(), 2021), alpha=0.6,
                          label='Endeavour Hydrothermal Vents')
axs[0].legend(loc='upper right', fontsize=16)
axs[0].set_ylim([0,50])
axs[0].set_ylabel('Num of CTD Profiles', fontsize=16)
hist2 = mpa2['year'].hist(ax=axs[1], color='r', bins=range(joinDF.year.min(), 2021), alpha=0.6,
                          label='Hecate Strait/Queen Charlotte Sound Glass Sponge Reef')
axs[1].legend(loc='upper right', fontsize=16)
axs[1].set_ylim([0,50])
axs[1].set_ylabel('Num of CTD Profiles', fontsize=16)
hist2 = mpa3['year'].hist(ax=axs[2], color='k', bins=range(joinDF.year.min(), 2021), alpha=0.6,
                          label='SGaan Kinghlas-Bowie Seamount')
plt.legend(loc='upper right', fontsize=16)
axs[2].set_ylim([0,50])
axs[2].set_ylabel('Num of CTD Profiles', fontsize=16)
plt.show()

bot = pd.read_csv("./data/IOS_BOT_Profiles_73c7_1532_b05f.csv")
bot['year'] = pd.DatetimeIndex(bot['time']).year
gdf_bot = gpd.GeoDataFrame(bot, geometry=gpd.points_from_xy(bot.longitude, bot.latitude))
print(gdf_ctd)
joinDF2 = gpd.sjoin(gdf_bot, pac_mpa, how='right', op="within")
# print(joinDF.header())
mpa1b = joinDF2[joinDF2['NAME_E']==pac_mpa.NAME_E[0]]
mpa2b = joinDF2[joinDF2['NAME_E']==pac_mpa.NAME_E[1]]
mpa3b = joinDF2[joinDF2['NAME_E']==pac_mpa.NAME_E[4]]
print(joinDF2.year.min())
# fig = plt.figure(figsize=(8,6))
fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 8),  squeeze=True,sharex=True,)
hist1 = mpa1b['year'].hist(ax=axs[0], color='b', bins=range(joinDF2.year.min(), 2021), alpha=0.6,
                          label='Endeavour Hydrothermal Vents')
axs[0].legend(loc='upper left', fontsize=16)
axs[0].set_ylim([0,10])
axs[0].set_ylabel('Num of BOT Profiles', fontsize=16)
hist2 = mpa2b['year'].hist(ax=axs[1], color='r', bins=range(joinDF2.year.min(), 2021), alpha=0.6,
                          label='Hecate Strait/Queen Charlotte Sound Glass Sponge Reef')
axs[1].legend(loc='upper left', fontsize=16)
axs[1].set_ylim([0,10])
axs[1].set_ylabel('Num of BOT Profiles', fontsize=16)
hist2 = mpa3b['year'].hist(ax=axs[2], color='k', bins=range(joinDF2.year.min(), 2021), alpha=0.6,
                          label='SGaan Kinghlas-Bowie Seamount')
plt.legend(loc='upper left', fontsize=16)
axs[2].set_ylim([0,10])
axs[2].set_ylabel('Num of BOT Profiles', fontsize=16)
plt.show()

fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(12, 8),  squeeze=True,sharex=True,)
hist1 = mpa1['year'].hist(ax=axs[0], color='b', bins=range(joinDF2.year.min(), 2021), alpha=0.4,
                          label='Endeavour H.T.V CTD')
hist1 = mpa1b['year'].hist(ax=axs[0], color='b', bins=range(joinDF2.year.min(), 2021), alpha=0.9,
                          label='Endeavour H.T.V BOT')
axs[0].legend(loc='upper left', fontsize=16)
axs[0].set_ylim([0,50])
axs[0].set_ylabel('Num of Profiles', fontsize=16)
hist2 = mpa2['year'].hist(ax=axs[1], color='r', bins=range(joinDF2.year.min(), 2021), alpha=0.4,
                          label='Glass Sponge Reef CTD')
hist2 = mpa2b['year'].hist(ax=axs[1], color='r', bins=range(joinDF2.year.min(), 2021), alpha=0.9,
                          label='Glass Sponge Reef BOT')
axs[1].legend(loc='upper left', fontsize=16)
axs[1].set_ylim([0, 50])
axs[1].set_ylabel('Num of Profiles', fontsize=16)
hist3 = mpa3['year'].hist(ax=axs[2], color='k', bins=range(joinDF2.year.min(), 2021), alpha=0.4,
                          label='SGaan Kinghlas-Bowie Seamount CTD')
hist3 = mpa3b['year'].hist(ax=axs[2], color='k', bins=range(joinDF2.year.min(), 2021), alpha=0.9,
                          label='SGaan Kinghlas-Bowie Seamount BOT')
plt.legend(loc='upper left', fontsize=16)
axs[2].set_ylim([0, 50])
axs[2].set_ylabel('Num of Profiles', fontsize=16)
plt.show()

fig = plt.figure(figsize=(8,6))
pac_ctd = gdf_ctd.cx[:, 45:60]
hist1 = pac_ctd['year'].hist(color='b', bins=range(pac_ctd.year.min(), 2021), alpha=0.6,)# label='Endeavour Hydrothermal Vents')
# hist2 = mpa2['year'].hist(color='r', bins=range(1977, 2020), alpha=0.4, label='Glass Sponge Reef')
# hist2 = mpa3['year'].hist(color='k', bins=range(1977, 2020), alpha=0.4, label='SGaan Kinghlas-Bowie Seamount')
# plt.legend()
plt.ylabel('Num of CTD Profiles in [45, 60] N', fontsize=16)
plt.show()

fig = plt.figure(figsize=(8,6))
pac_bot = gdf_bot.cx[:, 45:60]
hist1 = pac_bot['year'].hist(color='r', bins=range(pac_bot.year.min(), 2021), alpha=0.6,)# label='Endeavour Hydrothermal Vents')
# hist2 = mpa2['year'].hist(color='r', bins=range(1977, 2020), alpha=0.4, label='Glass Sponge Reef')
# hist2 = mpa3['year'].hist(color='k', bins=range(1977, 2020), alpha=0.4, label='SGaan Kinghlas-Bowie Seamount')
# plt.legend()
plt.ylabel('Num of BOT Profiles in [45, 60] N', fontsize=16)
plt.show()

# with fiona.open('./data/DFO_MPA_MPO_ZPM.shp') as src:
#     # for
#     print(src.schema)
#     for point in src:
#         print(shape(point['geometry']))
#
#     # The file we'll write to, the "destination", must be initialized
#     # with a coordinate system, a format driver name, and
#     # a record schema.  We can get initial values from the open
#     # collection's ``meta`` property and then modify them as
#     # desired.
#     print(src)
#     meta = src.meta
#     print(meta)
#     meta['schema']['geometry'] = 'Point'
#
#     # Open an output file, using the same format driver and
#     # coordinate reference system as the source. The ``meta``
#     # mapping fills in the keyword parameters of fiona.open().
#
#     with fiona.open('test_write.shp', 'w', **meta) as dst:
#
#         # Process only the records intersecting a box.
#         for f in src.filter(bbox=(-107.0, 37.0, -105.0, 39.0)):
#
#             # Get a point on the boundary of the record's
#             # geometry.
#
#             f['geometry'] = {
#                 'type': 'Point',
#                 'coordinates': f['geometry']['coordinates'][0][0]}
#
#             # Write the record out.
#
#             dst.write(f)