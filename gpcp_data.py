import xarray as xr
import datetime as dt
import matplotlib.pyplot as plt

def get_precip_monthly_mean():
    """
    Data from 01/1979 to 07/2026
    """    
    da = xr.open_dataset("data/gpcp/precip.mon.mean.nc", engine='netcdf4', 
                     decode_times=False)
    precip = da.data_vars['precip']
    return precip

def show_bar_chart(precip, lat_long, years):
    months = []
    mean_precip_mm = []
    for year in years:
        i = 0
        for i in range(12):
            curr_date = dt.datetime(year, i+1, 1)
            days_since_18000101 = (curr_date
                                - dt.datetime(1800, 1, 1)).days

            # data for plot
            mean_precip_mm.append(
                precip.sel({'lat': lat_long[0], 
                            'lon': lat_long[1],  
                            'time': days_since_18000101}, method='nearest').data
            )
            months.append(curr_date.strftime("%B")[:3] + ' ' + str(curr_date.year))

    #print(mean_precip_mm, months)

    _, ax = plt.subplots()
    ax.barh(months, mean_precip_mm)
    plt.show()