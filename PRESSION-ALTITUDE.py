import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker

data = pd.read_csv('SONDEGALILEOUpper+descent.csv')

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'
altitude = data['Altitude']
pression = data['Pression']
altitude_array = altitude.to_numpy()
pression_array = pression.to_numpy()
fig, pa = plt.subplots(figsize = (7,5))
pa.grid(True,ls="-",which="both",alpha=0.3)
pa.set_xlabel("Pression (bar)")
pa.set_ylabel("Altitude (km)")
pa.axhline(y=290, xmin=0.0, xmax=1.0, color='g', linewidth=1)
pa.axhline(y=28, xmin=0.0, xmax=1.0, color='g', linewidth=1)
pa.axhline(y=-133, xmin=0.0, xmax=1.0, color='g', linewidth=1)
pa.text(10**-6, 300, 'Limite Stratosphere-Thermosphere', fontsize=8)
pa.text(10**-6, 40, 'Tropopause', fontsize=8)
pa.text(10**-6, -120, 'Limite Troposphere-Atmosphere Profonde', fontsize=8)
pa.set_xscale('log')
pa.plot(pression_array, altitude_array)
pa.scatter(pression_array[-1], altitude_array[-1], marker='+',color='k')
locmaj = matplotlib.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
pa.xaxis.set_major_locator(locmaj)
locmin = matplotlib.ticker.LogLocator(base=10.0, subs=np.arange(2, 10)
* .1, numticks=100)
pa.xaxis.set_minor_locator(locmin)
pa.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
plt.show()