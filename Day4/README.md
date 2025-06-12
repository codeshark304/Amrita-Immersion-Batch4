#  Day 4 – Multivariate Time Series Classification & Dashboarding

Welcome to Day 4 of the Amrita Immersion Batch 4!  
This module focuses on **multivariate time series classification**, **EDA**, **model training**, **evaluation**, and **data visualization** using Power BI.

---

##  Objective

The objective of this task is to:

- Perform **Exploratory Data Analysis (EDA)** on multivariate time series data from 4 sensors (S001 to S004).
- Train a classification model to predict:
  - `Event_Type`: *normal, high hum, gas, fire*
  - `Alert_Level`: *low, medium, high*
- Evaluate model performance using confusion matrix, F1-score, precision, recall, and accuracy.
- Visualize real-time sensor behavior using **Power BI**.

---

##  Dataset Info

- **Filename**: `ENDGAME_with_dates1.csv`
- **Data points**: 40,320 (4 sensors × 10,080 per week)
- **Features Used (X)**:
  - `Temperature`, `Humidity`, `Gas_Concentration`, `Fire_Status`
- **Targets (y)**:
  - `Event_Type`, `Alert_Level`
- **Dropped Columns**:
  - `Location_ID`, `Response_Actions`, `Incident_ID`

---

##  Notebook Highlights: `final.ipynb`

- **Data Preprocessing**:
  - Timestamp parsing, Sensor ID grouping, normalization using `MinMaxScaler`.
- **Modeling**:
  - Classifier trained separately for `Event_Type` and `Alert_Level`.
  - Evaluation using confusion matrix and classification metrics.
- **Prediction Output**:
  - `predicted_next_week_labels_final.csv` includes predictions with `Sensor_ID` and `Timestamp`.

---

##  Dashboard: `PowerBI Dashboard.pbix`

- Visual insights on:
  - Weekly event patterns per sensor
  - Alert level heatmaps
  - Sensor anomalies (spikes in gas/fire)
- Drag-and-drop filtering by `Sensor_ID`, `Event_Type`, and `Timestamp`
![image](https://github.com/user-attachments/assets/3c1627c9-c3e5-4e13-a2e2-bf2b9877e49e)

---

##  Outputs

- 🔮 **Predicted Labels**: Stored in `predicted_next_week_labels_final.csv`
  - Columns: `Timestamp`, `Sensor_ID`, `Predicted_Event_Type`, `Predicted_Alert_Level`
-  **Evaluation Metrics**: Printed in notebook including:
  - Accuracy, Precision, Recall, F1-Score
  - Confusion Matrix

---




