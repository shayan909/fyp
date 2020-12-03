import sqlite3

conn = sqlite3.connect('chatbot.db')
# print("Connection Opened!")
# command = "SELECT * from medicine"
# result=conn.execute(command)
# for i in result:
#     print(i)
import pandas as pd
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

diseases = pd.read_csv("Disease Dataset.csv")
mixedSymptoms = []
for col_name in diseases.columns:
    mixedSymptoms.append(col_name)
del mixedSymptoms[-1]

inputSymptoms=['Fever','Sore_Throat']
# print(mixedSymptoms)

class MixedSymptoms:
    def predictDisease(inputSymptoms, mixedSymptoms):
        print(mixedSymptoms)
MixedSymptoms1 = MixedSymptoms.predictDisease(inputSymptoms, mixedSymptoms)

# for col_name in diseases.columns:
#     print(col_name)

# features = ['Age', 'Experience', 'Rank', 'Nationality']
#
# X = pd[features]
# y = pd['TARGET']
#
# print(X)
# print(y)