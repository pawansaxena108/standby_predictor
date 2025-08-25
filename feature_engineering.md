1 Feature engineering.

---

### **1. Flight Duration Features**

**avg\_flight\_duration\_hours**

* **Logic:** Longer flights increase crew fatigue and workload, beyond just counting the number of flights.
* **Why it matters:** Captures variability in operational complexity and potential demand for standby crew.
* **Example benefit:** Days with fewer but longer flights may require more standby crew than days with many short flights.

**departure\_duration\_interaction**

* **Logic:** Combines daily flight count × average flight duration to estimate total daily flight hours.
* **Why it matters:** Provides a stronger signal of actual crew workload than flight count alone.
* **Example benefit:** Helps predict high-demand days more accurately, improving staffing allocation.

---

### **2. Cyclical Encoding (day\_sin, day\_cos, week\_sin, week\_cos)**

* **Logic:** Days and weeks repeat in cycles; numeric representation alone can mislead the model.
* **Why it matters:** Preserves periodicity, allowing the model to detect patterns like weekends or holiday weeks.
* **Example benefit:** Model learns that standby demand spikes on weekends or during certain weeks of the year.

---

### **3. Rolling Statistics (rolling\_absence\_7d, rolling\_standby\_7d)**

* **Logic:** Short-term averages show recent trends and smooth out daily noise.
* **Why it matters:** Reflects ongoing changes in absences or standby usage, helping predict upcoming demand.
* **Example benefit:** Detects increasing absence rates over a week, allowing proactive adjustment of standby crew.

---

### **4. Lag Features (standby\_lag\_1d, standby\_lag\_7d)**

* **Logic:** Past demand often influences future demand; yesterday’s or last week’s numbers carry predictive value.
* **Why it matters:** Provides temporal context to the model for time-series forecasting.
* **Example benefit:** Helps the model anticipate patterns like recurring weekday demand spikes.

---

### **5. Missing Data Indicator (weather\_missing\_flag)**

* **Logic:** Missing weather data can signal unusual operational conditions or data issues.
* **Why it matters:** Treats missingness as a potential signal instead of losing information.
* **Example benefit:** Model accounts for disruption risks when weather data is unavailable, improving robustness.

---

### **6. Experience-Weighted Crew (experience\_weighted\_crew)**

* **Logic:** Not all crew members have the same productivity — experienced staff handle complex routes better.
* **Why it matters:** Captures quality of crew, not just quantity.
* **Example benefit:** Days with fewer but highly experienced crew might need less standby support.

---

If you want, I can also **combine all these into a single 1-page memory map** with **keywords and categories** so you can recall everything instantly in an interview. This works really well for quick mental retrieval. Do you want me to do that?
