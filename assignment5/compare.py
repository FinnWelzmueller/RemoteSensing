"""
This script parses LaTeX files containing a Table and plots comparison plots using pandas Dataframes
"""

import pandas as pd
from astropy.table import Table
from calculateGreatCircle import load_angle
import matplotlib.pyplot as plt

# Read Data
d1calculated = Table.read("./calculated1.tex").to_pandas()
d2calculated = Table.read("./calculated2.tex").to_pandas()

d1measured = Table.read("./measured1.tex").to_pandas()
d2measured = Table.read("./measured2.tex").to_pandas()

for idx, row in d1calculated.iterrows():
    d1calculated["Initial Latitude"][idx] = d1calculated["Initial Latitude"][idx].replace("[", "").replace("]", "").split(",")
    d2calculated["Initial Latitude"][idx] = d2calculated["Initial Latitude"][idx].replace("[", "").replace("]", "").split(",")
    d1measured["Initial Latitude"][idx] = d1measured["Initial Latitude"][idx].replace("[", "").replace("]", "").split(",")
    d2measured["Initial Latitude"][idx] = d2measured["Initial Latitude"][idx].replace("[", "").replace("]", "").split(",")
    d1calculated["Initial Longitude"][idx] = d1calculated["Initial Longitude"][idx].replace("[", "").replace("]", "").split(",")
    d2calculated["Initial Longitude"][idx] = d2calculated["Initial Longitude"][idx].replace("[", "").replace("]", "").split(",")
    d1measured["Initial Longitude"][idx] = d1measured["Initial Longitude"][idx].replace("[", "").replace("]", "").split(",")
    d2measured["Initial Longitude"][idx] = d2measured["Initial Longitude"][idx].replace("[", "").replace("]", "").split(",")

# Overview Plot
fig, ax = plt.subplots()
for idx, row in d1calculated.iterrows():
    ax.plot([1,2], [float(d1calculated["Drift Speed"][idx]), float(d2calculated["Drift Speed"][idx])], color=d1calculated["Colour"][idx], linestyle="dashed", marker='o')
    ax.plot([1,2], [float(d1measured["Drift Speed"][idx]), float(d2measured["Drift Speed"][idx])], color=d1calculated["Colour"][idx], linestyle="solid", marker='o')
ax.set_xlim(0.75,2.25)
ax.set_xticks([1,2])
ax.set_xticklabels([r"$\delta_1$", r"$\delta_2$"])
ax.set_xlabel("Time interval")
ax.set_ylabel("Drift Speed [km/h]")
ax.grid()
fig.show()
fig.savefig('timeseries.png')

# Drift Speed vs Coords

fig, ax = plt.subplots(ncols=1, nrows=2, fig_size=(12,15))
for idx, row in d1calculated.iterrows():
    ax[0].scatter([load_angle(ele, "deg") for ele in d1calculated["Initial Latitude"]], d1calculated["Drift Speed"], color='blue')
    ax[0].scatter([load_angle(ele, "deg") for ele in d1measured["Initial Latitude"]], d1measured["Drift Speed"], color='red')
    ax[1].scatter([load_angle(ele, "deg") for ele in d1calculated["Initial Longitude"]], d1calculated["Drift Speed"], color='blue')
    ax[1].scatter([load_angle(ele, "deg") for ele in d1measured["Initial Longitude"]], d1measured["Drift Speed"], color='red')
ax[0].set_xlabel("Initial Latitude [deg]")
ax[0].set_ylabel("Drift Speed [km/h]")
ax[0].grid()
ax[1].set_xlabel("Initial Longitude [deg]")
ax[1].set_ylabel("Drift Speed [km/h]")
ax[1].grid()
fig.show()
fig.savefig("scatter.png")