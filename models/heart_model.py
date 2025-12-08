import os
import joblib


# Load the model
model = joblib.load("C:\\Users\\ytsub\\Desktop\\github\\Know_Your_Health_MLModel\\models\\heart_atack_model.pkl")

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
