import pandas as pd
import yfinance as yf
from arch import arch_model

# Fetch SPX data from Yahoo Finance
spx = yf.download('^GSPC', start='2000-01-01', end='2025-01-01')

# Calculate the daily returns
spx['Return'] = spx['Close'].pct_change().dropna()

# Fit a GARCH(1,1) model
model = arch_model(spx['Return'].dropna(), vol='Garch', p=1, q=1)
garch_fit = model.fit(disp='off')

# Print the summary of the model
print(garch_fit.summary())

# Make a forecast
forecast = garch_fit.forecast(horizon=5)
print(forecast.variance[-1:])  # Print the forecasted variance

# Plot the forecast
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(forecast.variance[-1:], label='Forecasted Variance')
plt.title('GARCH Model Forecast')
plt.legend()
plt.show()
