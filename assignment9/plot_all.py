import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data import

chl1 = pd.read_csv("./track1-chl1.csv", delim_whitespace=True)
chl2 = pd.read_csv("./track2-chl1.csv", delim_whitespace=True)
chl3 = pd.read_csv("./track3-chl1.csv", delim_whitespace=True)

cdm1 = pd.read_csv("./track1-cdm.csv", delim_whitespace=True)
cdm2 = pd.read_csv("./track2-cdm.csv", delim_whitespace=True)
cdm3 = pd.read_csv("./track3-cdm.csv", delim_whitespace=True)

spm1 = pd.read_csv("./track1-spm.csv", delim_whitespace=True)
spm2 = pd.read_csv("./track2-spm.csv", delim_whitespace=True)
spm3 = pd.read_csv("./track3-spm.csv", delim_whitespace=True)

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(12,12))

ax[0,0].plot(chl1["pixel_no"], chl1["CHL1_mean_mean"], color='blue', linestyle='solid', label="Track 1 - CHL1")
ax[0,0].set_xlim(0, max(chl1["pixel_no"]))
ax[0,0].set_ylabel(r"CHL1 [mg/m$^3$]")
#ax[0,0].legend(loc="upper right")
ax[0,0].grid()
ax[0,0].set_title("Open Water")

ax[1,0].plot(cdm1["pixel_no"], cdm1["CDM_mean_mean"], color='red', linestyle='solid', label="Track 1 - CDM")
ax[1,0].set_xlim(0, max(cdm1["pixel_no"]))
ax[1,0].set_ylabel(r"CDM [m$^{-1}$]")
#ax[1,0].legend(loc="upper right")
ax[1,0].grid()

ax[2,0].plot(spm1["pixel_no"], spm1["SPM_mean_mean"], color='green', linestyle='solid', label="Track 1 - SPM-OC5")
ax[2,0].set_xlim(0, max(spm1["pixel_no"]))
ax[2,0].set_xlabel("Pixel number")
ax[2,0].set_ylabel(r"SPM-OC5 [g/m$^3$]")
#ax[2,0].legend(loc="upper right")
ax[2,0].grid()

ax[0,1].plot(chl2["pixel_no"], chl2["CHL1_mean_mean"], color='blue', linestyle='solid', label="Track 2 - CHL1")
ax[0,1].set_xlim(0, max(chl2["pixel_no"]))
#ax[0,1].legend(loc="upper right")
ax[0,1].grid()
ax[0,1].set_title("Coastal")

ax[1,1].plot(cdm2["pixel_no"], cdm2["CDM_mean_mean"], color='red', linestyle='solid', label="Track 2 - CDM")
ax[1,1].set_xlim(0, max(cdm2["pixel_no"]))
#ax[1,1].legend(loc="upper right")
ax[1,1].grid()

ax[2,1].plot(spm2["pixel_no"], spm2["SPM_mean_mean"], color='green', linestyle='solid', label="Track 2 - SPM-OC5")
ax[2,1].set_xlim(0, max(spm2["pixel_no"]))
ax[2,1].set_xlabel("Pixel number")
#ax[2,1].legend(loc="upper right")
ax[2,1].grid()

ax[0,2].plot(chl3["pixel_no"], chl3["CHL1_mean_mean"], color='blue', linestyle='solid', label="Track 3 - CHL1")
ax[0,2].set_xlim(0, max(chl3["pixel_no"]))
#ax[0,2].legend(loc="upper right")
ax[0,2].grid()
ax[0,2].set_title("Upwelling")

ax[1,2].plot(cdm3["pixel_no"], cdm3["CDM_mean_mean"], color='red', linestyle='solid', label="Track 3 - CDM")
ax[1,2].set_xlim(0, max(cdm3["pixel_no"]))
#ax[1,2].legend(loc="upper right")
ax[1,2].grid()

ax[2,2].plot(spm3["pixel_no"], spm3["SPM_mean_mean"], color='green', linestyle='solid', label="Track 3 - SPM-OC5")
ax[2,2].set_xlim(0, max(spm3["pixel_no"]))
ax[2,2].set_xlabel("Pixel number")
#ax[2,2].legend(loc="upper right")
ax[2,2].grid()

fig.savefig("overview-lineplots.png")