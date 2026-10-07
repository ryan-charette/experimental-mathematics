import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Parameters
mu0 = 60
sigma = 4
n = 16
alpha = 0.05

# Z-scores for the two-tailed test
z_low = norm.ppf(alpha/2)
z_high = norm.ppf(1 - alpha/2)

# Boundaries of the acceptance region under H0
x_low = mu0 + z_low * sigma/np.sqrt(n)
x_high = mu0 + z_high * sigma/np.sqrt(n)

# Range of true means under H1
mu_values = np.linspace(55, 65, 100)

# Power for each mu
power = []
for mu in mu_values:
    # Z-scores for the boundaries under H1
    z_low_H1 = (x_low - mu) / (sigma/np.sqrt(n))
    z_high_H1 = (x_high - mu) / (sigma/np.sqrt(n))

    # Probability of falling inside the acceptance region under H1
    beta = norm.cdf(z_high_H1) - norm.cdf(z_low_H1)

    # Power is 1 - beta
    power.append(1 - beta)

# Plot
plt.figure(figsize=(10,6))
plt.plot(mu_values, power, color='k')

# Vertical lines representing cut-off points
plt.axvline(x_low, color='k', linestyle='--', label='Lower cutoff')
plt.axvline(x_high, color='k', linestyle='--', label='Upper cutoff')
plt.grid()
plt.show()
