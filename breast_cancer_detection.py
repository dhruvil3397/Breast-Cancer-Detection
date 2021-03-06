# -*- coding: utf-8 -*-
"""Breast Cancer Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2o1FGhfj3FyMjQut1ksp1MdChDFPHdz

**Breast Cancer Detection With Logistic Regression**
* **The problem statement for this project is to predict whether a patient has breast cancer in benign or malignant stage.**

**import libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import datasets from the sklearn library
from sklearn.datasets import load_breast_cancer

# Load the dataset
breast_cancer_data = load_breast_cancer()
print(breast_cancer_data)

breast_cancer_data.data

dir(breast_cancer_data)

data = pd.DataFrame(breast_cancer_data.data,columns =breast_cancer_data.feature_names)
data.head()

"""**Assign the class column to the dataframe**"""

data["class"] = breast_cancer_data.target
data.head()

data.shape

print(len(data[data["class"]==0]))

print(len(data[data["class"]==1]))

df = []
for i in data["class"].unique():
  df.append([i,len(data[data["class"]==i])])
df

data["class"].value_counts()

# plot the pie chart
data["class"].value_counts().plot(kind ="pie")

data.describe()

print(breast_cancer_data.target_names)

data.groupby("class").mean()

"""**0 : Malignant**

**1 : Benign**

**Train Test Split method :**
* it devides the data in tarin data test data
"""

X = data.iloc[:,:30]
Y = data.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1)

print(X_train.shape,X_test.shape,X.shape)

print(Y_train.shape,Y_test.shape,Y.shape)

print(Y_train.mean(),Y_test.mean(),Y.mean())

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,random_state=1,stratify=Y)
# stratify --> for correct distribution of data as of the original data

print(Y_train.mean(),Y_test.mean(),Y.mean())

"""**Let's train the model using Logistic Regression :**"""

# import Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression().fit(X_train,Y_train)
model

"""**Find the accuracy of the model based upon the training data**"""

print("Accuracy of the model ",model.score(X_train,Y_train))

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
cm = confusion_matrix(Y_train,model.predict(X_train))
cm

import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot= True)

print(classification_report(Y_train,model.predict(X_train)))

"""**Find the accuracy of the model based upon the testing data**"""

print("Accuracy of the model ",model.score(X_test,Y_test))

"""**Model Evalution :**"""

cm = confusion_matrix(Y_test,model.predict(X_test))
cm

import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot= True)

print(classification_report(Y_test,model.predict(X_test)))

"""**Model validation :** **Detecting whether the patient has breast cancer in benign or malignant stage**"""

prediction = model.predict([[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]])
print(prediction)
if prediction[0]==0:
  print("The breast cancer is Malignant")
else :
  print("The breast cancer is Benign")

prediction = model.predict([[13.03,18.42,82.61,523.8,0.08983,0.03766,0.02562,0.02923,0.1467,0.05863,0.1839,2.342,1.17,14.16,0.004352,0.004899,0.01343,0.01164,0.02671,0.001777,13.3,22.81,84.46,545.9,0.09701,0.04619,0.04833,0.05013,0.1987,0.06169]])
print(prediction)
if prediction[0]==0:
  print("The breast cancer is Malignant")
else :
  print("The breast cancer is Benign")

"""**Save the model :**"""

import pickle
with open("Breast_Cancer_Detection.pkl","wb") as file :
  pickle.dump(model,file)

with open("Breast_Cancer_Detection.pkl","rb") as f:
  model = pickle.load(f)