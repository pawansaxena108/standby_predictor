import pandas as pd
import numpy as np

# Create dummy data for 60 days this time
np.random.seed(42)
date_range = pd.date_range(start='2025-01-01', periods=60, freq='D')

data = pd.DataFrame({
    'date': date_range,
    'active_crew_count': np.random.randint(50, 70, size=60),
    'daily_flight_departures': np.random.randint(40, 60, size=60),
    'crew_absence_rate': np.random.uniform(0, 0.1, size=60),
    'weather_risk_score': np.random.uniform(0, 1, size=60),
    'special_event_flag': np.random.choice([0, 1], size=60, p=[0.9, 0.1]),
    'avg_flight_duration_hours': np.random.uniform(1, 5, size=60),  # new feature
    'crew_experience_level': np.random.uniform(0.5, 1, size=60)  # 0.5=junior, 1=senior
})

# Target variable - number of standby crew needed
data['standby_crew_needed'] = (
    0.3 * data['daily_flight_departures'] +
    0.4 * data['active_crew_count'] * (1 - data['crew_absence_rate']) +
    4 * data['special_event_flag'] +
    0.2 * data['avg_flight_duration_hours'] * data['crew_experience_level'] +
    np.random.normal(0, 3, size=60)
).astype(int)

# Feature Engineering

# 1. Cyclical encoding of day of week and week of year
data['day_of_week'] = data['date'].dt.dayofweek
data['day_sin'] = np.sin(2 * np.pi * data['day_of_week'] / 7)
data['day_cos'] = np.cos(2 * np.pi * data['day_of_week'] / 7)

data['week_of_year'] = data['date'].dt.isocalendar().week
data['week_sin'] = np.sin(2 * np.pi * data['week_of_year'] / 52)
data['week_cos'] = np.cos(2 * np.pi * data['week_of_year'] / 52)

# 2. Rolling statistics for crew absence and standby needed
data['rolling_absence_7d'] = data['crew_absence_rate'].rolling(window=7, min_periods=1).mean()
data['rolling_standby_7d'] = data['standby_crew_needed'].rolling(window=7, min_periods=1).mean()

# 3. Interaction feature: Flight departures × Avg flight duration
data['departure_duration_interaction'] = data['daily_flight_departures'] * data['avg_flight_duration_hours']

# 4. Lag features for target variable
data['standby_lag_1d'] = data['standby_crew_needed'].shift(1).fillna(method='bfill')
data['standby_lag_7d'] = data['standby_crew_needed'].shift(7).fillna(method='bfill')

# 5. Missing data example for weather risk
data.loc[10:14, 'weather_risk_score'] = np.nan
data['weather_missing_flag'] = data['weather_risk_score'].isnull().astype(int)
data['weather_risk_score'].fillna(data['weather_risk_score'].mean(), inplace=True)

# 6. Experience-weighted active crew
data['experience_weighted_crew'] = data['active_crew_count'] * data['crew_experience_level']

# Display first 15 rows of data with new features
print(data.head(15))
