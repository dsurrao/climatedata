# https://docs.xarray.dev/en/stable/user-guide/data-structures.html#dataarray
import numpy as np
import pandas as pd
import xarray as xr

data = np.random.rand(4, 3)
locs = ["IA", "IL", "IN"]
times = pd.date_range("2000-01-01", periods=4)
foo = xr.DataArray(data, coords=[times, locs], dims=["time", "space"])
print(foo)

# get the data point for 'Il' on 2000-01-02
print(foo.sel({'time': '2000-01-02', 'space': 'IL'}).data)

"""
a 2D array, assigned the names x and y to the two dimensions respectively and 
associated two coordinate labels ‘10’ and ‘20’ with the two locations along the 
x dimension. 
"""
"""
values = np.random.randn(2, 3)
print(values)
data = xr.DataArray(values, dims=("x", "y"), coords={"x": [10, 20]})
"""

"""
Xarray supports four kinds of indexing. Since we have assigned coordinate 
labels to the x dimension we can use label-based indexing along that dimension 
just like pandas. The four examples below all yield the same result (the value 
at x=10) but at varying levels of convenience and intuitiveness.
"""

"""
# positional and by integer label, like numpy
print(data[0, :])
print()

# loc or "location": positional and coordinate label, like pandas
print(data.loc[10])
print()

# isel or "integer select":  by dimension name and integer label
print(data.isel(x=0))
print()

# sel or "select": by dimension name and coordinate label
print(data.sel(x=10))
print()

# sel or "select": by dimension name and coordinate label
print(data.sel(x=20))

"""