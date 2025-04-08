import pandas as pd
import numpy as np
import yfinance as yf
from arch import arch_model
import matplotlib.pyplot as plt

# Download historical data for NQ
ticker = '^NDX'  # Nasdaq 100 index ticker
data = yf.download(ticker, start='2010-01-01', end='2025-03-27')
data = data['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna() * 100

# Plot the returns
plt.figure(figsize=(10, 6))
plt.plot(returns)
plt.title('Daily Returns of Nasdaq 100 (NQ)')
plt.xlabel('Date')
plt.ylabel('Returns (%)')
plt.show()

# Fit GARCH(1,1) model
model = arch_model(returns, vol='Garch', p=1, q=1, rescale=False)
garch_fit = model.fit(disp='off')

print(garch_fit.summary())

# Forecast volatility
forecast_horizon = 10  # Forecasting for the next 10 days
forecast = garch_fit.forecast(horizon=forecast_horizon)
variance_forecast = forecast.variance.values[-1, :]
volatility_forecast = np.sqrt(variance_forecast)

print("10-day Volatility Forecast:")
print(volatility_forecast)

# Plot forecasted volatility
plt.figure(figsize=(10, 6))
plt.plot(volatility_forecast, marker='o', linestyle='--')
plt.title('10-day Volatility Forecast for Nasdaq 100 (NQ)')
plt.xlabel('Days')
plt.ylabel('Volatility (%)')
plt.show()





