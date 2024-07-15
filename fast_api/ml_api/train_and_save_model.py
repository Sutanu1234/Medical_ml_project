import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
dataset = pd.read_csv('diabetes.csv')

# Separate features and target
X = dataset.drop(columns='Outcome', axis=1)
Y = dataset['Outcome']

# Standardize the features
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

# Update X with the standardized data
X = standardized_data

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Evaluate the model
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Training data accuracy:', training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Test data accuracy:', test_data_accuracy)

# Save the trained model and scaler
joblib.dump(classifier, 'diabetes_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
