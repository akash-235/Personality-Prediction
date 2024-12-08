import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('psyc.csv')

# Assuming the CSV includes 'age', 'openness', 'neuroticism', 'conscientiousness', 'agreeableness', 'extraversion', and 'gender'
# Convert gender to numerical values (Male=0, Female=1)
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'].str.lower())  # Convert gender to lowercase before encoding

# Features and target variable
X = data[['age', 'openness', 'neuroticism', 'conscientiousness', 'agreeableness', 'extraversion', 'gender']]  # Include 'gender' as a feature
y = data['Personality']  # Assuming 'personality' is the column you're predicting

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the scaler and fit it on the training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit and transform the training data

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Save the model and the scaler
joblib.dump(model, 'personality_prediction_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model and scaler saved successfully.")
