import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# data import
rhow = pd.read_csv("./spectrum-rhow-all.csv", delim_whitespace=True, skiprows=1)
rtoa = pd.read_csv("./spectrum-rtoa-all.csv", delim_whitespace=True, skiprows=1)

# Erste Figure (bleibt unverändert)
fig, ax = plt.subplots(nrows=2, sharex=True)

ax[0].plot(rhow["Wavelength"], rhow["open_water"], color='blue', label="rhow")
ax[0].plot(rtoa["Wavelength"], rtoa["open_water"], color='red', label="rtoa")
ax[0].legend(loc="upper right")
ax[0].grid()
ax[0].set_xlim(min(rhow["Wavelength"]), max(rhow["Wavelength"]))
ax[0].set_ylabel("Open Water")

ax[1].plot(rhow["Wavelength"], rhow["LJCO"], color='blue', label="rhow")
ax[1].plot(rtoa["Wavelength"], rtoa["LJCO"], color='red', label="rtoa")
ax[1].grid()
ax[1].set_xlabel("Wavelength [nm]")
ax[1].set_ylabel("LJCO")
ax[1].set_xlim(min(rhow["Wavelength"]), max(rhow["Wavelength"]))
fig.savefig("pin-comparison.png")

# Zweite Figure mit Inset
fig, ax = plt.subplots(nrows=2, sharex=True)

ax[0].plot(rhow["Wavelength"], rhow["open_water"], color='blue', label="open water")
ax[0].plot(rhow["Wavelength"], rhow["LJCO"], color='red', label="LJCO")
ax[0].legend(loc="upper right")
ax[0].grid()
ax[0].set_ylabel("rhow")

# Inset-Achse im oberen Plot (ax[0])
axins = inset_axes(ax[1], width="30%", height="30%", loc="upper right", borderpad=1)

axins.plot(rtoa["Wavelength"], rtoa["open_water"], color='blue')
axins.plot(rtoa["Wavelength"], rtoa["LJCO"], color='red')
axins.set_xlim(750, 780)
axins.set_ylim(0.01, 0.06)
axins.grid()

ax[1].plot(rtoa["Wavelength"], rtoa["open_water"], color='blue', label="open water")
ax[1].plot(rtoa["Wavelength"], rtoa["LJCO"], color='red', label="LJCO")
ax[1].grid()
ax[1].set_xlabel("Wavelength [nm]")
ax[1].set_ylabel("rtoa")
ax[1].set_xlim(min(rhow["Wavelength"]), max(rhow["Wavelength"]))

fig.savefig("spectrum-comparison.png")
