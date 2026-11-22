import xarray as xr
import datetime as dt

da = xr.open_dataset("data/gpcp/precip.mon.mean.nc", engine='netcdf4', 
                     decode_times=False)
precip = da.data_vars['precip']

# print(precip)
# exit(0)

"""
print(precip['time'])
    units:          days since 1800-1-1 00:00:0.0
    actual_range:   [65378. 82696.]

dt.date(1800, 1, 1) + dt.timedelta(days=1)
"""

# print(precip.sel({'lat': -83.75,  'lon': 6.25,  'time': 82696}).data)


# chennai lat long: 13.07096267632839, 80.28562580980238
# precipitation unit: mm/day
# print(precip.sel({'lat': 13.07096267632839,  
#                   'lon': 80.28562580980238,  
#                   'time': 82696}, method='nearest'))

"""
Google Gemini:
Chennai's heaviest one-day rainfall in history was 494 mm (19.45 inches), 
recorded on December 1, 2015, during the catastrophic 2015 South India floods.
"""
# print(dt.date(2015, 12, 1) - dt.date(1800, 1, 1)) # 78861
for i in range(78861 - 60, 78861):
    print(precip.sel({'lat': 13.07096267632839, 
                      'lon': 80.28562580980238,  
                      'time': i}, method='nearest').data)

# monthly intervals
# print(precip['time'][1].data - precip['time'][0].data)

