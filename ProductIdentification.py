# Import required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset (assuming we have a dataset with product features and labels)
# Example CSV file structure: 'feature1', 'feature2', ..., 'is_genuine'
data = pd.read_csv("product_data.csv")

# Prepare the data
X = data.drop(columns=['is_genuine'])  # Features
y = data['is_genuine']  # Labels: 1 for genuine, 0 for fake

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

# Save the model for future use
joblib.dump(model, "product_authentication_model.pkl")
