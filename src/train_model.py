import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

from feature_extraction import extract_features

# Load dataset
data = pd.read_csv("data/dataset.csv")

X = []
y = data['label']

for pwd in data['password']:
    X.append(extract_features(pwd))

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X, y)

# Save model
joblib.dump(model, "model/model.pkl")

print("Model trained and saved successfully")
