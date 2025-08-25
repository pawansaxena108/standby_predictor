1 Feature engineering.

### **1. Technical Tone**

* Added **`avg_flight_duration_hours`** to model workload intensity beyond flight counts, capturing variability in operational complexity.
* Engineered **`departure_duration_interaction`** (flights × duration) to represent **total daily flight hours**, a stronger predictor of crew demand.
* These features improved model accuracy and feature importance, helping better predict **standby crew requirements** in dynamic schedules.

---

### **2. Business/Operational Tone**

* Introduced **flight duration-based features** to account for the **higher crew demand and fatigue risk** associated with longer flights.
* Created a **total daily flight hours metric** to align predictions with real operational workload.
* Enabled **more accurate staffing forecasts**, supporting **better crew planning and reduced operational disruptions**.




Here’s a **clear and interview-ready explanation** of the other engineered features in your code and **how they add value**:

---

### **1. Cyclical Encoding (`day_sin`, `day_cos`, `week_sin`, `week_cos`)**

* **Why:** Days and weeks are cyclical — Monday follows Sunday, Week 1 follows Week 52.
* **Benefit:** Prevents the model from misinterpreting the numerical order of days/weeks and helps detect **seasonal patterns**, like weekend crew shortages or busy weekly cycles.

---

### **2. Rolling Statistics (`rolling_absence_7d`, `rolling_standby_7d`)**

* **Why:** Short-term trends affect demand — if absences have been high for a week, standby needs likely increase.
* **Benefit:** Captures **recent moving averages** for absence rates and standby usage, helping the model adjust to **short-term shifts or anomalies**.

---

### **3. Lag Features (`standby_lag_1d`, `standby_lag_7d`)**

* **Why:** Yesterday’s or last week’s standby need often predicts today’s need due to operational continuity.
* **Benefit:** Improves **time-series forecasting** by giving the model temporal context of recent demands.

---

### **4. Missing Data Indicator (`weather_missing_flag`)**

* **Why:** Missing weather data might signal **data issues** or unusual conditions.
* **Benefit:** Allows the model to **use missingness as a signal** rather than losing data, improving robustness.

---

### **5. Experience-Weighted Crew (`experience_weighted_crew`)**

* **Why:** More experienced crews handle schedules more efficiently, reducing standby demand.
* **Benefit:** Helps the model differentiate between **quantity of crew** and **quality of experience**, improving staffing predictions.

---

### **How to summarize in interviews**

You could say:

> “I engineered features like **cyclical encodings** for seasonal patterns, **rolling averages and lags** to capture recent trends, **missing-data flags** for robustness, and **experience-weighted crew metrics** to factor in skill levels. These features helped the model better align predictions with operational realities and improved forecast accuracy.”

Would you like me to show you how to quickly **measure the importance** of each of these features using a model, so you can talk about performance impact in your interview?
