import joblib
import os

# Get the path to cancer.pkl in the same directory as this file
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "cancer.pkl")

# Load the model
model = joblib.load(path)

def cancer_fun(data):
    predict = model.predict([data])
    return predict

print(f"Model path: {path}")
print(f"Model loaded successfully: {model is not None}")
