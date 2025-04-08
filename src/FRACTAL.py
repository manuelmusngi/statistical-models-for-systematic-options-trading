import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def get_hurst_exponent(time_series, max_lag=20):
    lags = range(2, max_lag)
    tau = [np.sqrt(np.std(np.subtract(time_series[lag:], time_series[:-lag]))) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0] * 2.0

# Fetch SPX data from Yahoo Finance
spx = yf.download('^GSPC', start='2000-01-01', end='2025-01-01')

# Use Close prices for Hurst exponent calculation
spx['Return'] = spx['Close'].pct_change().dropna()

# Calculate Hurst exponent
hurst_exponent = get_hurst_exponent(spx['Return'].dropna())
print(f'Hurst exponent: {hurst_exponent}')

# Interpretation
if hurst_exponent < 0.5:
    interpretation = "The time series is mean reverting."
elif hurst_exponent == 0.5:
    interpretation = "The time series is a Geometric Brownian Motion."
else:
    interpretation = "The time series is trending."

print(interpretation)

# Plot the SPX Close prices
plt.figure(figsize=(10, 6))
plt.plot(spx['Close'], label='SPX Close Price')
plt.title('SPX Close Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot the returns
plt.figure(figsize=(10, 6))
plt.plot(spx['Return'], label='SPX Daily Returns')
plt.title('SPX Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.show()
