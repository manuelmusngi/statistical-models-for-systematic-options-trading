# pip install pandas numpy statsmodels matplotlib yfinance

# Fetch and Prepare the Data
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Fetch the data
ticker = "^SPX"  # Ticker symbol for S&P 500 Index
data = yf.download(ticker, start="2010-01-01", end="2025-01-01")

# Display the first few rows of the dataset
print(data.head())

# Plot the closing price
data['Close'].plot(title='S&P 500 Closing Prices', figsize=(14, 7))
plt.show()

#  Check for Stationarity
def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()

    # Plot rolling statistics:
    plt.figure(figsize=(14, 7))
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)

# Test for stationarity
test_stationarity(data['Close'])

# Making the Series Stationary
# Take the first difference to make the series stationary
data['Close_diff'] = data['Close'] - data['Close'].shift(1)
data['Close_diff'].dropna(inplace=True)

# Test for stationarity again
test_stationarity(data['Close_diff'])

# Plot ACF and PACF
# Plot ACF and PACF to determine p and q
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
plot_acf(data['Close_diff'].dropna(), ax=axes[0])
plot_pacf(data['Close_diff'].dropna(), ax=axes[1])
plt.show()

# Train the ARIMA Model
# Fit the ARIMA model
model = SARIMAX(data['Close'], order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
results = model.fit(disp=False)
print(results.summary())

# Make Predictions
# Forecast for the next 30 days
forecast = results.get_forecast(steps=30)
forecast_index = pd.date_range(start=data.index[-1], periods=30, freq='B')
forecast_df = pd.DataFrame(forecast.predicted_mean, index=forecast_index, columns=['Forecast'])

# Plot the forecast
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Historical')
plt.plot(forecast_df, label='Forecast', color='red')
plt.title('S&P 500 Index Price Forecast')
plt.legend()
plt.show()

