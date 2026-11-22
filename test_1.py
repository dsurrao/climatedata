# tutorial from https://www.youtube.com/watch?v=hiwDEjv2a60
# https://tutorial.xarray.dev/overview/xarray-in-45-min.html

import numpy as np
import xarray as xr

x = np.array([
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
])

y = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
])

temps = np.array([
    [23, 23, 24, 23],
    [24, 24, 28, 23],
    [23, 22, 24, 22],
])

humids = np.array([
    [70, 69, 69, 70],
    [68, 68, 60, 67],
    [71, 70, 70, 68],
])

humidity_da = xr.DataArray(humids, dims=['y', 'x'])
# print(humidity_da)
# print(humidity_da['y'])
# print(humidity_da['x'])
# print(humidity_da.sum('x'))
# print(humidity_da.sum('y'))
# exit()

humidity_da = xr.DataArray(humids, coords=(y[:,0], x[0,:]))
print(humidity_da.coords['dim_0'])
exit()

humidity_da.name = 'Relative Humidity'
humidity_da.attrs['units'] = 'percent'
print(humidity_da)

temp_da = xr.DataArray(temps, coords=(y[:,0], x[0,:]), dims=('y', 'x'))
temp_da.name = 'Air Temperature'
temp_da.attrs['units'] = 'degC'
print(temp_da)

ds = xr.Dataset(
    {'air_temperature': (['y', 'x'], temp_da.data), 
     'rel_humidity': (['y', 'x'], humidity_da.data)},
    coords = {'x': x[0, :], 'y': y[:, 0]}
)

ds.attrs['title'] = 'My Model Output'
print(ds)