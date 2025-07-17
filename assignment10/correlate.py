import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv("./correlation-data-eustrophic.csv", delim_whitespace=True)

# plot with outlier
r = np.around(pearsonr(df["Chla_[mg/m3]_ref"], df["CHL1_mean_mean"])[0],3)
print(r)
fig, ax = plt.subplots()
#ax.grid()
ax.scatter(df["Chla_[mg/m3]_ref"], df["CHL1_mean_mean"], color='blue')
ax.set_xlabel(r"Chla [mg/m$^3$]")
ax.set_ylabel(r"CHL1 [mg/m$^3$]")
#ax.set_xlim(0,1.3)
#ax.set_ylim(0,12.5)
ax.annotate(fr"$r = {r}$", xy=(0.1,0.9),xycoords='axes fraction', fontsize=14,bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
ax.grid()
fig.savefig("correlation-plot-eustrophic.png")

#plot without outlier (station 12)
df = pd.read_csv("./correlation-data-mesotrophic.csv", delim_whitespace=True)
r = np.around(pearsonr(df["Chla_[mg/m3]_ref"], df["CHL1_mean_mean"])[0],3)
fig, ax = plt.subplots()
#ax.grid()
ax.scatter(df["Chla_[mg/m3]_ref"], df["CHL1_mean_mean"], color='blue')
ax.set_xlabel(r"Chla [mg/m$^3$]")
ax.set_ylabel(r"CHL1 [mg/m$^3$]")
#ax.set_xlim(0,1.3)
ax.grid()
#ax.set_ylim(0,3)

ax.annotate(fr"$r = {r}$", xy=(0.1,0.9),xycoords='axes fraction', fontsize=14, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
fig.savefig("correlation-plot-mesotrophic.png")