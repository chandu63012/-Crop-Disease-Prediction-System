import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load Data
df = pd.read_csv("crop_disease_environment_large_dataset_3000.csv")

# Separating x and y
x = df.drop('disease', axis=1)
y = df['disease']

# One hot encoding for crops and soil_type
X_encoded = pd.get_dummies(x, columns=["crop", "soil_type"])
feature_columns = X_encoded.columns.tolist()

# Label encoding for disease
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Save feature columns, label encoder, and scaler
with open("feature_columns.pkl", "wb") as file:
    pickle.dump(feature_columns, file)

with open("label_encoder.pkl", "wb") as file:
    pickle.dump(le, file)

with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)

# Train Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_scaled, y_encoded)

# Save RF model
with open("rf_best_model.pkl", "wb") as file:
    pickle.dump(rf, file)

print("Model and preprocessing objects saved successfully.")
