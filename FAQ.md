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

Would you like me to **customize one version** to match a specific role, like a **data scientist** or **operations analyst** position?
