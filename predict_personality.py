import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the model and scaler
model = joblib.load('personality_prediction_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to get input and predict personality
def get_input():
    age = float(input("Age: "))
    openness = float(input("Openness (1-10): "))
    neuroticism = float(input("Neuroticism (1-10): "))
    conscientiousness = float(input("Conscientiousness (1-10): "))
    agreeableness = float(input("Agreeableness (1-10): "))
    extraversion = float(input("Extraversion (1-10): "))
    gender = input("Gender (Male/Female): ").strip().lower()

    # Convert gender to numerical value (0 for Male, 1 for Female)
    gender = 0 if gender == 'male' else 1

    # Return input as a list
    return [age, openness, neuroticism, conscientiousness, agreeableness, extraversion, gender]

# Main execution
if __name__ == "__main__":
    print("Enter the following details:")

    # Get user input
    input_data = get_input()

    # Convert the input data to a DataFrame with the same columns as the training data
    input_data_df = pd.DataFrame([input_data], columns=['age', 'openness', 'neuroticism', 'conscientiousness', 'agreeableness', 'extraversion', 'gender'])

    # Scale the input data using the fitted scaler
    scaled_input_data = scaler.transform(input_data_df)

    # Predict personality trait using the trained model
    prediction = model.predict(scaled_input_data)

    # Output the prediction
    print(f"\nPredicted Personality Trait: {prediction[0]}")
