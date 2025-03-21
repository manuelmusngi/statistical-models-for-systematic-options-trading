import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import datetime

# Load the data
data = pd.read_csv('SPX_data.csv', parse_dates=['Date'], index_col='Date')

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Close'])
plt.title('SPX Close Price')
plt.show()

# Split the data into training and testing sets
train = data[:int(0.8*len(data))]
test = data[int(0.8*len(data)):]

# Fit the SARIMAX model
model = SARIMAX(train['Close'], order=(1, 1, 1), seasonal_order=(0, 0, 0, 0))
results = model.fit()

# Print the model summary
print(results.summary())

# Make predictions
predictions = results.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)

# Plot the predictions against the actual data
plt.figure(figsize=(10, 6))
plt.plot(train['Close'], label='Training')
plt.plot(test['Close'], label='Actual')
plt.plot(predictions, label='Predicted')
plt.legend()
plt.title('ARIMA Model Predictions')
plt.show()

# Calculate the mean squared error
mse = np.mean((predictions - test['Close'])**2)
print(f'Mean Squared Error: {mse}')
