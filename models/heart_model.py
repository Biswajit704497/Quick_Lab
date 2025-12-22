import os
import joblib

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "heart_atack_model.pkl")


# Load the model
model = joblib.load(path)

def heart_def(data):
    return model.predict(data)

# For local test
# age, gender, highBloodPressure, lowBloodPressure,cholesterol, heartRate, smoking, alcoholConsumption, exerciseHours, diet, diabetes, familyHistory, previousHeartProblems, medicationUse, stressLevel

if __name__ == "__main__":
    # Example with random parameters matching the feature order
    test_data = [[45, 1, 1, 0, 200, 75, 0, 0, 5, 2, 0, 1, 0, 1, 6]]
    result = heart_def(test_data)
    print(result)
    print(f"Prediction: {result[0]}")
