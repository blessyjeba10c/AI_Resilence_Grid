# Install necessary packages
!pip install xgboost
!pip install pandas openpyxl scikit-learn matplotlib imbalanced-learn

# Imports
import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE

# Upload Excel
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
data = pd.read_excel(file_name)

print("First 5 rows:")
print(data.head())

# ---------- Feature Engineering ----------
# Add engineered features (example)
data['Load_per_Voltage'] = data['Load_MW'] / data['Voltage_V']
data['Pressure_Deviation'] = data['Pressure_hPa'] - data['Pressure_hPa'].mean()

# Features and target
feature_cols = ['Wind_Speed_kmph', 'Rainfall_mm', 'Pressure_hPa',
                'Voltage_V', 'Load_MW', 'Past_Outages_Count',
                'Load_per_Voltage', 'Pressure_Deviation']

X = data[feature_cols]
y = data['Blackout_Risk']

# ---------- Check for Class Imbalance ----------
print("\nBlackout Risk Class Distribution:")
print(y.value_counts())

# Apply SMOTE to balance classes if needed
smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X, y)

print("\nClass Distribution After SMOTE:")
print(pd.Series(y_balanced).value_counts())

# ---------- Train-test split ----------
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

# ---------- Hyperparameter Tuning ----------
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.05, 0.1],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

xgb_clf = xgb.XGBClassifier()
grid_search = GridSearchCV(estimator=xgb_clf, param_grid=param_grid,
                           cv=3, n_jobs=-1, verbose=1, scoring='accuracy')

grid_search.fit(X_train, y_train)

print("\nBest Parameters Found:")
print(grid_search.best_params_)

# ---------- Evaluation ----------
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("\nImproved Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ---------- Feature Importance ----------
xgb.plot_importance(best_model, importance_type='gain')
plt.title("Feature Importance (Tuned Model)")
plt.show()

# ---------- OPTIONAL: Export Predictions ----------
results = X_test.copy()
results['Actual'] = y_test
results['Predicted'] = y_pred
results.to_excel("Predictions.xlsx", index=False)

# Download link for predictions
from google.colab import files
files.download("Predictions.xlsx")
