import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

path1 = "/RAID0/home/yoshida/practice_file_tokken/t/t.1992.288x145.pl50.nc"
data = xr.open_dataset(path1)

plev = data["plev"]
lat = data["lat"]

data1 = data.sel(plev = 10. , lat = slice(-90. , -80.)).mean(dim = ('lat')).mean(dim = ('lon'))
data2 = data.sel(plev = 10. , lat = slice(-70. , -60.)).mean(dim = ('lat')).mean(dim = ('lon'))

data1 = data1["t"]
data2 = data2["t"]
data5 = data1 - data2

time = data5["time"]

plt.plot(time , data5 , color = 'k')
plt.title("∇ T in 1992" , fontsize = 20)
plt.ylabel("[K]")
plt.axhline(y = 0 , color = 'r')
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 1))
plt.show()
