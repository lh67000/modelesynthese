import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker

data = pd.read_csv('SONDEGALILEOUpper+descent.csv')

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'STIXGeneral'

temperature = data['Temperature']
pression = data['Pression']
temperature_array = temperature.to_numpy()
pression_array = pression.to_numpy()
fig, ax = plt.subplots(figsize = (7,5))
ax.set_ylim(max(pression_array), min(pression_array))
ax.set_xlim(0, 1000)
ax.xaxis.tick_top()
ax.set_yscale('log')    
ax.grid(True,ls="-",which="both",alpha=0.3)
locmaj = matplotlib.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
ax.yaxis.set_major_locator(locmaj)
ax.xaxis.set_label_position('top')
locmin = matplotlib.ticker.LogLocator(base=10.0, subs=np.arange(2, 10) * .1, numticks=100)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Pression (bar)")
ax.plot(temperature_array, pression_array)
ax.scatter(temperature_array[-1], pression_array[-1], marker='+',color='k')
plt.show()