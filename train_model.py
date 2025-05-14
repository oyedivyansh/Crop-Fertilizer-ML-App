# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your dataset (replace with your actual dataset path)
df = pd.read_csv('crop_data.csv')

# Assuming your dataset has columns: 'N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'crop'
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]  # Features
y = df['crop']  # Target variable

# Encoding crop names (as integers) using LabelEncoder
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Create a RandomForestClassifier model
model = RandomForestClassifier()

# Train the model
model.fit(X, y_encoded)

# Save the model
joblib.dump(model, 'crop_model.pkl')

# Save the label encoder (to decode the integer predictions back to crop names)
joblib.dump(label_encoder, 'label_encoder.pkl')

print("Model trained and saved successfully!")
