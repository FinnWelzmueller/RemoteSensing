import pandas as pd
import matplotlib.pyplot as plt


sentinel = pd.read_csv("./sentinel.csv", delim_whitespace=True)
csm = pd.read_csv("./csm.csv", delim_whitespace=True)
csv = pd.read_csv("./202405061556_allfinal4SNAP.csv")

fig, ax = plt.subplots(nrows=3, sharex=True)
ax[0].plot(sentinel["latitude"], sentinel["mean"], color='blue', label="Sentinel-1")
ax[0].set_ylabel("backscatter")
ax[0].grid()
ax[0].legend()
ax[1].plot(csm["latitude"], csm["mean"], color='red', label="CSM")
ax[1].set_ylabel("backscatter")
ax[1].grid()
ax[1].legend()
ax[2].set_xlabel("Latitude")
ax[2].plot(csv["Lat"], csv["TT"], color="green", label="AEM")
ax[2].set_ylabel("ice thickness")
ax[2].grid()
ax[2].legend()
ax[2].set_ylim(0,20)

fig.savefig("comparison.png")