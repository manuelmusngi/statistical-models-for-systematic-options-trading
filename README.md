Systematic options trading relies on statistical models to identify opportunities, manage risk, and execute trades consistently. 
These are some key statistical models used in systematic options trading:

---

### **1. Time Series Models**
   - **Purpose:** Forecast price movements or implied volatility for options strategies.
   - **Common Techniques:**
     - **ARIMA (AutoRegressive Integrated Moving Average)** – Forecasting price trends
     - [ARIMA](https://github.com/manuelmusngi/statistical-models-for-systematic-options-trading/blob/main/src/ARIMA.py)
     - **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)** – Forecasting volatility changes
     - [GARCH](https://github.com/manuelmusngi/qr-statistical-models-for-systematic-options-trading/blob/main/src/GARCH.py)
---
### **2. Risk-Based Models**
   - **Purpose:** Manage position or porfolio risk dynamically.
   - **Common Techniques:**
     - Value at Risk (VaR) and Conditional VaR (CVaR)
     - Delta, Gamma, Vega hedging strategies
     - Bayesian risk models to adjust exposure dynamically
---
### **3. Stochastic Models**
   - **Purpose:** Model the randomness in price movements and volatility.
   - **Common Techniques:**
     - Heston Model (stochastic volatility)
     - Jump-Diffusion Models (to account for market crashes)
     - Brownian Motion (used in option pricing models)
---
### **4. Market Microstructure and Order Flow Models**
   - **Purpose:** Analyze liquidity, order flow, and market participant behavior.
   - **Common Techniques:**
     - Order book imbalance analysis
     - Volume-weighted average price (VWAP) deviation models
     - Implied volatility surface analysis
---
### **5. Machine Learning-Based Models**
   - **Purpose:** Detect patterns in option pricing and market data.
   - **Common Techniques:**
     - Support Vector Machines (SVMs) for classification of profitable vs. non-profitable trades
     - Reinforcement Learning for optimizing strategy execution
     - Decision Trees & Random Forests for feature selection (e.g., IV percentile, delta skew)
---
### **6. Mean Reversion Models**
   - **Purpose:** Identify assets where implied volatility, price, or option Greeks revert to a historical mean.
   - **Common Techniques:**
     - Z-Score Analysis (for IV rank and IV percentile)
     - Bollinger Bands
     - Ornstein-Uhlenbeck Process (for modeling mean-reverting behavior in asset prices)
---
### **7. Probability and Expected Value Models**
   - **Purpose:** Evaluate expected returns of different options strategies.
     - **Black-Scholes Model**: Used to estimate theoretical option prices and compare against market prices for arbitrage.
     - **Monte Carlo Simulations**: Simulating thousands of price paths to evaluate strategy performance.
   - **Common Techniques:**
     - Probability of touch (chances of an option strike being hit)
     - Expected value calculations for credit spreads, iron condors, etc.
---
### **Practical Application in Systematic Trading**
A systematic trading approach may combine multiple models. For example:
1. **Use a GARCH model** to predict volatility and enter an options spread.
2. **Apply Monte Carlo simulations** to test potential P&L outcomes.
3. **Optimize position sizing** using the Kelly Criterion.
4. **Use machine learning classifiers** to filter high-probability setups.

