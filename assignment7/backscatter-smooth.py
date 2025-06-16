import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


sentinel = pd.read_csv("./sentinel.csv", delim_whitespace=True)
csm = pd.read_csv("./csm.csv", delim_whitespace=True)
csv = pd.read_csv("./202405061556_allfinal4SNAP.csv")

sentinel["mean_smooth"] = np.convolve(np.array(sentinel["mean"]), np.ones(50)/50, "same")

csm["mean_smooth"] = np.convolve(np.array(csm["mean"]), np.ones(50)/50, "same")
csv["mean_smooth"] = np.convolve(np.array(csv["TT"]), np.ones(50)/50, "same")
fig, ax = plt.subplots(nrows=3, sharex=True)
ax[0].plot(sentinel["latitude"], sentinel["mean_smooth"], color='blue', label="Sentinel-1")
ax[0].set_ylabel("backscatter")
ax[0].grid()
ax[0].legend()
ax[1].plot(csm["latitude"], csm["mean_smooth"], color='red', label="CSM")
ax[1].set_ylabel("backscatter")
ax[1].grid()
ax[1].legend()
ax[2].set_xlabel("Latitude")
ax[2].plot(csv["Lat"], csv["mean_smooth"], color="green", label="External")
ax[2].set_ylabel("backscatter")
ax[2].grid()
ax[2].legend()
ax[2].set_ylim(0,20)
fig.savefig("comparisson-smooth.png")