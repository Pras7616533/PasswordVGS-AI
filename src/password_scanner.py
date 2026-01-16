import joblib
from src.feature_extraction import extract_features

model = joblib.load("model/model.pkl")

def scan_password(password):
    features = extract_features(password)
    result = model.predict([features])[0]

    if result == 0:
        return "Very Weak"
    elif result == 1:
        return "Medium"
    else:
        return "Strong"

# Test
if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Password Strength:", scan_password(pwd))
