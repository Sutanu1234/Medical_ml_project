import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Loading dataset
dataset = pd.read_csv('diabetes.csv')

# Displaying dataset information
print(dataset.head())
print(dataset.shape)
print(dataset.describe())
print(dataset['Outcome'].value_counts())
print(dataset.groupby('Outcome').mean())

# Separating data and labels
X = dataset.drop(columns='Outcome', axis=1)
Y = dataset['Outcome']
print(X)
print(Y)

# Standardizing data
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
print(standardized_data)

X = standardized_data
Y = dataset['Outcome']

# Splitting data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)
print(X.shape, X_train.shape, X_test.shape)

# Training the SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Model evaluation
# Accuracy score
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data: ', training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data: ', test_data_accuracy)

# Predicting with new data
input_data = (2, 197, 70, 45, 543, 30.5, 0.158, 53)

# Converting the input data to a numpy array and creating a DataFrame
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
input_data_df = pd.DataFrame(input_data_as_numpy_array, columns=dataset.columns[:-1])

# Standardizing the input data
std_data = scaler.transform(input_data_df)
print(std_data)

# Making a prediction
prediction = classifier.predict(std_data)
print(prediction)

if prediction[0] == 0:
    print('The person does not have diabetes')
else:
    print('The person has diabetes')

