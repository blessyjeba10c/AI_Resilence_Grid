# AI_Resilience_Grid

## AI Resilience Grid: Blackout Prediction and Simulation

This repository provides a complete pipeline for **predicting blackout risks in electrical grids using machine learning** and simulating those risks using **OpenDSS**. The system integrates **real-time weather** and **grid data** to assist in improving grid resilience and proactive outage management.

---

##  Project Overview

**Objective:**  
Predict potential blackouts in electrical grids based on environmental and electrical parameters, and simulate their impact using OpenDSS.

---

##  Components

- Predictive Modeling with **XGBoost**
- Confusion Matrix and Metrics Visualization
- **Heatmap Visualization** of High-Risk Zones
- **OpenDSS Simulation File Generation**

---

##  Dataset Description

| **Feature**          | **Description**                                 |
|----------------------|-------------------------------------------------|
| `Wind_Speed_kmph`    | Wind speed (km/h)                               |
| `Rainfall_mm`        | Rainfall (mm)                                   |
| `Pressure_hPa`       | Atmospheric pressure (hPa)                      |
| `Voltage_V`          | Grid voltage (V)                                |
| `Load_MW`            | Electrical load (MW)                            |
| `Past_Outages_Count` | Number of previous outages                      |
| `Blackout_Risk`      | Target label → `0 = Low risk, 1 = High risk`    |

---

##  Features

- Data preprocessing and balancing using **SMOTE**
- Hyperparameter-tuned **XGBoost** classifier
- **Classification Report** and **Confusion Matrix** visualization
- Interactive **Heatmap** visualization using **Folium**
- Automatic generation of **OpenDSS (.dss)** files for simulation

---


