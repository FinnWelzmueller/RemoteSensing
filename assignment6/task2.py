import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def linear(m,x,b):
    return m*x + b
def lin_fit(inp_x, inp_y, inp_y_err):
    popt, pcov =  curve_fit(linear, inp_x, inp_y)
    m, b = popt
    m_err, b_err = np.sqrt(np.diag(pcov))
    return m, m_err, b, b_err 
    
    


df_may = pd.read_csv("Sigma0_HH_may.csv", delim_whitespace=True)
df_july = pd.read_csv("Sigma0_HH_july.csv", delim_whitespace=True)


print("----- Statistics for May-----")
print(f"Mean Sigma0: {np.mean(df_may['Sigma0_HH_mean'])}")
print(f"Standard deviation Sigma0: {np.std(df_may['Sigma0_HH_mean'])}")
print("----- Statistics for July-----")
print(f"Mean Sigma0: {np.mean(df_july['Sigma0_HH_mean'])}")
print(f"Standard deviation Sigma0: {np.std(df_july['Sigma0_HH_mean'])}")

m_m, m_err_m, b_m, b_err_m = lin_fit(df_may["pixel_no"], df_may["Sigma0_HH_mean"], df_may["Sigma0_HH_sigma"])
print("----- fitting results for May -----")
print(f"Slope: {m_m} +- {m_err_m}")
print(f"Intercept: {b_m} +- {b_err_m}")

fig, ax = plt.subplots(nrows=2)
ax[0].plot(df_may["pixel_no"], df_may["Sigma0_HH_mean"], 'b.', label="Data")
ax[0].plot(df_may["pixel_no"], [linear(m_m, ele, b_m) for ele in df_may["pixel_no"]], 'r--', label="Linear fit")
ax[0].set_xlim(0, max(df_may["pixel_no"]))
ax[0].set_ylabel(r"$\sigma_0$")
ax[0].legend()
ax[0].grid()


m_j, m_err_j, b_j, b_err_j = lin_fit(df_july["pixel_no"], df_july["Sigma0_HH_mean"], df_july["Sigma0_HH_sigma"])
print("----- fitting results for July -----")
print(f"Slope: {m_j} +- {m_err_j}")
print(f"Intercept: {b_j} +- {b_err_j}")

ax[1].plot(df_july["pixel_no"], df_july["Sigma0_HH_mean"], 'b.', label="Data")
ax[1].plot(df_july["pixel_no"], [linear(m_j, ele, b_j) for ele in df_july["pixel_no"]], 'r--', label="Linear fit")

ax[1].set_xlim(0, max(df_july["pixel_no"]))
ax[1].set_xlabel("Pixel number along line")
ax[1].set_ylabel(r"$\sigma_0$")
ax[1].legend()
ax[1].grid()
plt.savefig("linear_fits_Sigma0.png")
plt.show()


