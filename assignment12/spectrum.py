import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score, root_mean_squared_error

def resample_spectrum(wl_insitu, rho_insitu, band_centers, band_widths):
    """
    wl_insitu: in-situ wavelengths
    rho_insitu: in-situ rhown
    band_centers: band centers of the data on which the in-situ data has to be resampled
    band_widths: band widths of the data on which the in-situ data has to be resampled
    """
    resampled = []
    for center, width in zip(band_centers, band_widths):
        lower = center - width / 2
        upper = center + width / 2
        # value pairs within interval
        idx = np.where((wl_insitu >= lower) & (wl_insitu <= upper))[0]
        if len(idx) > 0:
            mean_value = np.mean(rho_insitu[idx])
        else:
            mean_value = np.nan  # if no value pairs within interval
        resampled.append(mean_value)
    return np.array(resampled)

def filter_for_nan(insitu, enmap, wavelengths):
    x = np.array(insitu)
    y = np.array(enmap)
    w = np.array(wavelengths)
    return x[~np.isnan(x)], y[~np.isnan(x)], w[~np.isnan(x)]

def sam(insitu, satellite):
    insitu = np.array(insitu)
    satellite = np.array(satellite)
    return np.acos(sum(np.multiply(insitu, satellite))/(np.sqrt(sum(np.square(insitu))) * np.sqrt(sum(np.square(satellite)))))

df_s2a = pd.read_csv("./ljco_rhown.csv", sep="\t")
df_enmap = pd.read_csv("./ljco_enmap.csv", sep="\t")
df_insitu = pd.read_csv("./insitu.csv", sep="\t")

df_enmap_bandinfo = pd.read_csv("./enmap-bandinfo.csv", sep=",")
df_s2a_bandinfo = pd.read_csv("./s2a-bandinfo.csv", sep=",")

insitu_resample_s2a = resample_spectrum(df_insitu["Wavelength"], df_insitu["rhown"], df_s2a_bandinfo["CentralWavelength"], df_s2a_bandinfo["Bandwidth"])
insitu_resample_enmap = resample_spectrum(df_insitu["Wavelength"], df_insitu["rhown"], df_enmap_bandinfo["CentralWavelength"], df_enmap_bandinfo["Bandwidth"])
enmap_resample_s2a = resample_spectrum(df_enmap["Wavelength"], df_enmap["LJCO"], df_s2a_bandinfo["CentralWavelength"], df_s2a_bandinfo["Bandwidth"])


fig, ax = plt.subplots(nrows=3)
ax[0].plot(df_s2a["Wavelength"], df_s2a["LJCO"], color='blue', label="S2A")
ax[0].set_xlabel("Wavelength [nm]")
ax[0].set_ylabel("rhown")
ax[0].grid()
ax[0].legend(loc="upper right")
ax[0].set_ylim(bottom=0)
ax[1].plot(df_enmap["Wavelength"], df_enmap["LJCO"], color='red', label="EnMAP")
ax[1].set_xlabel("Wavelength [nm]")
ax[1].set_ylabel("rhown")
ax[1].grid()
ax[1].legend(loc="upper right")
ax[1].set_ylim(bottom=0)
ax[2].plot(df_insitu["Wavelength"], df_insitu["rhown"], color='green', label="in-situ")
ax[2].set_xlabel("Wavelength [nm]")
ax[2].set_ylabel("rhown")
ax[2].grid()
ax[2].legend(loc="upper right")
ax[2].set_ylim(bottom=0)
fig.savefig("spectra-unresampled.png")


# resampled plot

fig, ax = plt.subplots()
ax.plot(df_insitu["Wavelength"], df_insitu["rhown"], "b-",label="in-situ")
ax.plot(df_enmap_bandinfo["CentralWavelength"], insitu_resample_enmap, "ro", label="in-situ resample EnMAP")
ax.plot(df_s2a_bandinfo["CentralWavelength"], insitu_resample_s2a, "gs", label="in-situ resample S2A")

ax.set_xlabel("Wavelength [nm]")
ax.set_ylabel("rhown")
ax.grid()
ax.legend(loc="upper right")
ax.set_ylim(bottom=0)
fig.savefig("spectra-resampled.png")

# resampled versus original spectra
fig, ax = plt.subplots(nrows=2, sharex=True)
ax[0].plot(df_s2a["Wavelength"], df_s2a["LJCO"], color='blue', label="S2A")
ax[0].plot(df_s2a_bandinfo["CentralWavelength"], insitu_resample_s2a, "b--", label="in-situ resample S2A")
ax[0].set_ylabel("rhown")
ax[0].grid()
ax[0].set_xlim(left=400, right=750)
ax[0].legend(loc="upper right")
ax[0].set_ylim(bottom=0)
ax[1].plot(df_enmap["Wavelength"], df_enmap["LJCO"], color='red', label="EnMAP")
ax[1].plot(df_enmap_bandinfo["CentralWavelength"], insitu_resample_enmap, "r--", label="in-situ resample EnMAP")
ax[1].set_xlabel("Wavelength [nm]")
ax[1].set_ylabel("rhown")
ax[1].grid()
ax[1].set_xlim(left=400, right=750)
ax[1].legend(loc="upper right")
ax[1].set_ylim(bottom=0)

fig.savefig("spectra-sorted.png")


# scatterplot
# filter only entries from enmap data which are in resampled data points by wavelength
enmap_original = []
wavelengths_enmap = []
for center in df_enmap_bandinfo["CentralWavelength"].values:
    idx_closest = np.argmin(np.abs(df_enmap["Wavelength"].values - center))
    enmap_original.append(df_enmap["LJCO"].values[idx_closest])
    wavelengths_enmap.append(df_enmap["Wavelength"].values[idx_closest])
insitu_enmap_clean, enmap_clean, wavelengths_enmap_clean = filter_for_nan(insitu_resample_enmap, enmap_original, wavelengths_enmap)

s2a_original = []
wavelengths_s2a = []
for center in df_s2a_bandinfo["CentralWavelength"].values:
    idx_closest = np.argmin(np.abs(df_s2a["Wavelength"].values - center))
    s2a_original.append(df_s2a["LJCO"].values[idx_closest])
    wavelengths_s2a.append(df_s2a["Wavelength"].values[idx_closest])
insitu_s2a_clean, s2a_clean, wavelengths_s2a_clean = filter_for_nan(insitu_resample_s2a, s2a_original, wavelengths_s2a)

# statistics:
r = r2_score(insitu_enmap_clean, enmap_clean)
rmse = root_mean_squared_error(insitu_enmap_clean, enmap_clean)
mdape = np.median(np.abs((enmap_clean - insitu_enmap_clean) / insitu_enmap_clean)) * 100.

fig, ax = plt.subplots(ncols=2, figsize=(12.8, 4.8))
sc = ax[0].scatter(insitu_enmap_clean, enmap_clean, c=wavelengths_enmap_clean)
ax[0].set_xlabel("In-Situ")
ax[0].set_ylabel("EnMAP")
ax[0].set_xlim(left=0)
ax[0].set_ylim(bottom=0)
ax[0].annotate(
    f"R² = {r:.2f}\nRMSE = {rmse:.4f}\nMdAPE = {mdape:.2f}%", 
    xy=(0.1, 0.8), 
    xycoords='axes fraction',
    fontsize=12,
    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
)
ax[0].grid()
cbar = fig.colorbar(sc, ax=ax[0])
cbar.set_label("Wavelength [nm]")

r = r2_score(insitu_s2a_clean, s2a_clean)
rmse = root_mean_squared_error(insitu_s2a_clean, s2a_clean)
mdape = np.median(np.abs((s2a_clean - insitu_s2a_clean) / insitu_s2a_clean)) * 100.

sc = ax[1].scatter(insitu_s2a_clean, s2a_clean, c=wavelengths_s2a_clean)
ax[1].set_xlabel("In-Situ")
ax[1].set_ylabel("EnMAP")
ax[1].set_xlim(left=0)
ax[1].set_ylim(bottom=0)
ax[1].annotate(
    f"R² = {r:.2f}\nRMSE = {rmse:.4f}\nMdAPE = {mdape:.2f}%", 
    xy=(0.1, 0.8), 
    xycoords='axes fraction',
    fontsize=12,
    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
)
ax[1].grid()
cbar = fig.colorbar(sc, ax=ax[1])
cbar.set_label("Wavelength [nm]")
fig.savefig("scatter_enmap.png")

# SAM

print(f"EnMAP: theta = {np.around(sam(insitu_enmap_clean, enmap_clean) * 180/np.pi, 3)}°")
print(f"S2A: theta = {np.around(sam(insitu_s2a_clean, s2a_clean) * 180/np.pi, 3)}°")