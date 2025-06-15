# AI_Resilience_Grid

# AI-Enhanced Simulation for Resilient Grids in Disaster Response

## Problem Statement

Natural disasters such as cyclones can lead to severe disruptions in electrical grids, impacting critical infrastructure and communities. There is a growing need for resilient grid management that integrates predictive capabilities with real-time simulation tools. This project addresses that need by developing an AI-assisted framework to predict blackout risks and simulate grid responses. By analyzing historical outage records, real-time weather patterns, and electrical parameters, the system enables proactive decision-making for prioritized restoration and resource optimization. The solution also features simulation environments to test and validate microgrid resilience during disaster-induced isolation scenarios.

## Methodology

1. **Data Preparation**  
   - Collected and curated synthetic datasets comprising weather variables (wind speed, rainfall, pressure), electrical load data, outage history, and blackout risk labels.
   - Applied preprocessing techniques to handle class imbalance using SMOTE for better model training.

2. **AI Model Development**  
   - Used machine learning algorithms (primarily XGBoost) to build a predictive model for blackout risks.
   - Performed hyperparameter tuning to improve model accuracy and generalization.
   - Evaluated model performance using confusion matrix, classification reports, and accuracy metrics.

3. **Grid Simulation using OpenDSS**  
   - Generated automated OpenDSS (.dss) scripts to simulate various fault scenarios on an example grid.
   - Simulated fault conditions and analyzed system behavior under blackout conditions.

4. **Visualization and Dashboard**  
   - Created interactive heatmaps using Folium to display geographical high-risk zones for blackouts.
   - Developed an interactive visualization dashboard using Power BI to provide real-time risk insights, trends, and simulation results for faster decision-making.

## Features

- Predictive blackout risk classification using machine learning
- Confusion matrix visualization for performance evaluation
- Geographic risk visualization through interactive heatmaps
- OpenDSS integration for electrical grid simulation
- Power BI dashboard for monitoring, analysis, and decision support

## Key Outcomes

- Proactive identification of potential blackout areas before disasters strike
- Simulation-based analysis of fault impact on grid behavior
- Enhanced visualization of risk zones and restoration processes
- Framework that can be scaled and customized for real-world grid environments

<p align="center">
  <img src="https://github.com/user-attachments/assets/c73d7d55-1e3b-45c4-b439-cbadbc5bf050" width="400">
</p>

