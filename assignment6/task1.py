import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def linear(m,x,b):
    return m*x + b
def lin_fit(inp_x, inp_y, inp_y_err):
    popt, pcov =  curve_fit(linear, inp_x, inp_y, sigma=inp_y_err, absolute_sigma=True)
    m, b = popt
    m_err, b_err = np.sqrt(np.diag(pcov))
    return m, m_err, b, b_err 
    
    


df_may = pd.read_csv("Amplitude_HH_may.csv", delim_whitespace=True)
df_july = pd.read_csv("Amplitude_HH_july.csv", delim_whitespace=True)


print("----- Statistics for May-----")
print(f"Mean Amplitude: {np.around(np.mean(df_may['Amplitude_HH_mean']),2)}")
print(f"Standard deviation Amplitude: {np.around(np.std(df_may['Amplitude_HH_mean']),2)}")
print("----- Statistics for July-----")
print(f"Mean Amplitude: {np.around(np.mean(df_july['Amplitude_HH_mean']),2)}")
print(f"Standard deviation Amplitude: {np.around(np.std(df_july['Amplitude_HH_mean']),2)}")

m_m, m_err_m, b_m, b_err_m = lin_fit(df_may["pixel_no"], df_may["Amplitude_HH_mean"], df_may["Amplitude_HH_sigma"])
print("----- fitting results for May -----")
print(f"Slope: {np.around(m_m,4)} +- {np.around(m_err_m,4)}")
print(f"Intercept: {np.around(b_m,4)} +- {np.around(b_err_m,4)}")

fig, ax = plt.subplots(nrows=2)
ax[0].plot(df_may["pixel_no"], df_may["Amplitude_HH_mean"], 'b.', label="Data")
ax[0].plot(df_may["pixel_no"], [linear(m_m, ele, b_m) for ele in df_may["pixel_no"]], 'r--', label="Linear fit")
ax[0].set_xlim(0, max(df_may["pixel_no"]))
ax[0].set_ylabel("Amplitude")
ax[0].legend()
ax[0].grid()
ax[0].set_ylim(0,900)

m_j, m_err_j, b_j, b_err_j = lin_fit(df_july["pixel_no"], df_july["Amplitude_HH_mean"], df_july["Amplitude_HH_sigma"])
print("----- fitting results for July -----")
print(f"Slope: {np.around(m_j,4)} +- {np.around(m_err_j,4)}")
print(f"Intercept: {np.around(b_j,4)} +- {np.around(b_err_j,4)}")

ax[1].plot(df_july["pixel_no"], df_july["Amplitude_HH_mean"], 'b.', label="Data")
ax[1].plot(df_july["pixel_no"], [linear(m_j, ele, b_j) for ele in df_july["pixel_no"]], 'r--', label="Linear fit")

ax[1].set_xlim(0, max(df_july["pixel_no"]))
ax[1].set_xlabel("Pixel number along line")
ax[1].set_ylabel("Amplitude")
ax[1].legend()
ax[1].grid()
plt.savefig("linear_fits_Amplitude.png")
plt.show()


