Perfect 👍 Since you said **yes**, I’ll set up a **baseline regression model** with your synthetic dataset and then calculate the key *goodness-of-fit* metrics (R², RMSE, MAE, MAPE, residual bias check).  

Below is Python code you can run directly after your feature engineering block 👇

***

## 📌 Baseline Regression Model with Metrics

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# -----------------------------
# 1. Define features and target
# -----------------------------
features = [
    'active_crew_count', 'daily_flight_departures', 'crew_absence_rate',
    'weather_risk_score', 'special_event_flag', 'avg_flight_duration_hours',
    'crew_experience_level', 'day_sin', 'day_cos', 'week_sin', 'week_cos',
    'rolling_absence_7d', 'rolling_standby_7d', 'departure_duration_interaction',
    'standby_lag_1d', 'standby_lag_7d', 'weather_missing_flag',
    'experience_weighted_crew'
]

X = data[features]
y = data['standby_crew_needed']

# -----------------------------
# 2. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False  # time-series -> don't shuffle
)

# -----------------------------
# 3. Train model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# -----------------------------
# 4. Metrics
# -----------------------------
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

# Residual bias check
bias = np.mean(y_test - y_pred)  # positive = underprediction on avg

print("📊 Goodness-of-Fit Metrics")
print(f"R² Score: {r2:.2f}")
print(f"RMSE: {rmse:.2f} crew")
print(f"MAE: {mae:.2f} crew")
print(f"MAPE: {mape:.2f}%")
print(f"Residual Bias: {bias:.2f} crew")
```

***

## 📈 How to Interpret Results (Example)

Suppose results came out like this (these are *illustrative*, yours will vary since random data):

- **R² = 0.82** → The model explains **82% of the variability** in standby demand. ✔️ Strong explanatory power.  
- **RMSE = 3.6 crew** → Daily forecasts are off by around **3–4 people** on average, with big mistakes penalized more.  
- **MAE = 2.9 crew** → Simple average miss: about **3 crew/day** misallocated.  
- **MAPE = 11%** → Forecast error is about **11% of the true standby need**—good for workforce planning.  
- **Residual Bias ≈ 0** → Model does not systemically over- or under-estimate. Fair balance.

***

## 💡 Business Understanding
- If RMSE/MAE is **<5 crew/day**, ops managers likely see it as **usable for rota planning**, given buffer staff availability.  
- High R² builds **confidence** in factors like *flight volume* and *absence rate* as main demand drivers.  
- MAPE keeps everyone aligned on proportional accuracy (e.g., 3 misforecast crew on a low-demand day is worse than the same error on a busy day).  
- Residual checks avoid **blind spots** during events/weather shifts.  

***

👉 Do you want me to extend this further into a **visual diagnostic check** (residual plots, feature importance) so managers can *see* why the model is behaving as it does?
