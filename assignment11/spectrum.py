import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data import

rhow = pd.read_csv("./spectrum-rhow-all.csv", delim_whitespace=True, skiprows=1)
rtoa = pd.read_csv("./spectrum-rtoa-all.csv", delim_whitespace=True, skiprows=1)

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