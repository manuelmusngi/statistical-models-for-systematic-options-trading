# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Step 1: Load and preprocess the data
def load_data(file_path):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    data = data['Close']
    return data

# Step 2: Perform time series analysis
def test_stationarity(timeseries):
    result = adfuller(timeseries)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    for key, value in result[4].items():
        print('Critical Values:')
        print(f'   {key}: {value}')

def plot_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data, color='blue')
    plt.title('Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

# Step 3: Fit the ARIMA model
def fit_arima_model(data):
    model = ARIMA(data, order=(5, 1, 0))
    model_fit = model.fit()
    print(model_fit.summary())
    return model_fit

# Step 4: Forecast future prices
def forecast_prices(model_fit, steps=30):
    forecast = model_fit.forecast(steps=steps)
    return forecast

# Step 5: Evaluate the model
def evaluate_model(test_data, forecast):
    mse = mean_squared_error(test_data, forecast)
    print('Mean Squared Error:', mse)

# Main function to run the steps
def main():
    # Load data
    file_path = 'NQ_data.csv'  # Replace with your data file path
    data = load_data(file_path)

    # Plot data
    plot_data(data)

    # Test stationarity
    test_stationarity(data)

    # Fit ARIMA model
    train_data, test_data = data[:-30], data[-30:]
    model_fit = fit_arima_model(train_data)

    # Forecast prices
    forecast = forecast_prices(model_fit, steps=30)

    # Evaluate model
    evaluate_model(test_data, forecast)

    # Plot forecast
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Original')
    plt.plot(pd.Series(forecast, index=test_data.index), label='Forecast', color='red')
    plt.title('Price Forecast')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
