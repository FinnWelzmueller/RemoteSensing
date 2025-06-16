import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_sar_may = pd.read_csv("sar_may.csv", delim_whitespace=True)
df_sar_july = pd.read_csv("sar_july.csv", delim_whitespace=True)
df_modis_may_1 = pd.read_csv("modis_may_1.csv", delim_whitespace=True)
df_modis_july_1 = pd.read_csv("modis_july_1.csv", delim_whitespace=True)
df_modis_may_2 = pd.read_csv("modis_may_2.csv", delim_whitespace=True)
df_modis_july_2 = pd.read_csv("modis_july_2.csv", delim_whitespace=True)
df_modis_may_3 = pd.read_csv("modis_may_3.csv", delim_whitespace=True)
df_modis_july_3 = pd.read_csv("modis_july_3.csv", delim_whitespace=True)

fig, ax = plt.subplots(nrows=2)
ax[0].plot(df_sar_may["pixel_no"], df_sar_may["mean"], color="blue", label="SAR")
ax[0].set_ylabel(r"$\sigma_0$")
ax[0].grid()
ax[0].set_xlim(left=0, right=max(df_sar_may["pixel_no"]))
ax[0].set_ylim(bottom=0, top=0.2)

ax[1].plot(df_modis_may_1["pixel_no"], df_modis_may_1["mean"], color="red", label="MODIS, red band")
ax[1].plot(df_modis_may_2["pixel_no"], df_modis_may_2["mean"], color="green", label="MODIS, green band")
ax[1].plot(df_modis_may_3["pixel_no"], df_modis_may_3["mean"], color="blue", label="MODIS, blue band")
ax[1].set_xlabel("Pixel")
ax[1].set_ylabel("Virtual Brightness")
ax[1].grid()
ax[1].set_xlim(left=0, right=max(df_modis_may_1["pixel_no"]))
ax[1].set_ylim(bottom=0, top=255)
plt.savefig("sar-modis-may.png")

print("---- SAR MAY ----")
print(rf"Mean: {df_sar_may["mean"].mean()}$\pm${df_sar_may["mean"].std()}")

print("---- SAR JULY ----")
print(rf"Mean: {df_sar_july["mean"].mean()}$\pm${df_sar_july["mean"].std()}")

print("---- MODIS MAY ----")
print(rf"Mean R: {df_modis_may_1["mean"].mean()}$\pm${df_modis_may_1["mean"].std()}")
print(rf"Mean G: {df_modis_may_2["mean"].mean()}$\pm${df_modis_may_2["mean"].std()}")
print(rf"Mean B: {df_modis_may_3["mean"].mean()}$\pm${df_modis_may_3["mean"].std()}")

print("---- MODIS JULY ----")
print(rf"Mean R: {df_modis_july_1["mean"].mean()}$\pm${df_modis_july_1["mean"].std()}")
print(rf"Mean G: {df_modis_july_2["mean"].mean()}$\pm${df_modis_july_2["mean"].std()}")
print(rf"Mean B: {df_modis_july_3["mean"].mean()}$\pm${df_modis_july_3["mean"].std()}")