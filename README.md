# AI_Resilence_Grid
AI_Resilence_Grid - Fault Detection

AI Resilience Grid: Blackout Prediction and Simulation
This repository contains a complete pipeline for predicting blackout risks in electrical grids using machine learning and performing grid simulations using OpenDSS. The project integrates real-time weather and grid data to assist in improving grid resilience and proactive outage management.

Project Overview
Objective:
Predict potential blackouts in the electrical grid based on environmental and electrical parameters, and simulate their impact using OpenDSS.

Components:

Predictive Modeling with XGBoost

Confusion Matrix and Metrics Visualization

Heatmap Visualization of High-Risk Zones

OpenDSS Simulation File Generation

Dataset Description
Feature	Description
Wind_Speed_kmph	Wind speed in kilometers per hour
Rainfall_mm	Rainfall in millimeters
Pressure_hPa	Atmospheric pressure in hectopascals
Voltage_V	Grid voltage in volts
Load_MW	Electrical load in megawatts
Past_Outages_Count	Number of previous outages
Blackout_Risk	Target label (0 = Low risk, 1 = High risk)

Features
Data preprocessing and balancing using SMOTE

Hyperparameter-tuned XGBoost classification model

Classification report and confusion matrix visualization

Interactive heatmap visualization of predicted risks using Folium

Automatic generation of OpenDSS (.dss) files for simulation purposes
