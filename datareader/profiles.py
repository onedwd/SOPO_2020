
import numpy as np
import glob
import pandas as pd

def read_ctd(archive_dir):
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
    data.to_csv('/home/wand/PycharmProjects/adcp_analysis/oceanprocess/cioos/ctd_' + str(year) + '.csv')
    print(data_xr)