import pandas as pd
import re
from sklearn.tree import DecisionTreeClassifier

# inputSymptoms = ['Phlegm', 'Fever', 'Sinus_Pressure', 'Runny_Nose', 'Long_Term_Breathing_Or_Wheezing', 'Cough', 'sharp_pain_when_weight_is_put_on_joint', 'Gas']


def Identification(inputSymptoms):
    class simpleSelection:
        def fit(self, features, targetName):
            symptomsOfDataSet = []
            for index, column in enumerate(features.columns):
                symptomsOfDataSet.append(features.iat[0, index])
            self.features = symptomsOfDataSet
            self.targetName = targetName.iloc[0]
        def predict(self, inputSymptoms):
            inputSymptoms = [item for sublist in inputSymptoms for item in sublist]  # convert to List
            for index in range(len(inputSymptoms)):
                if self.features[index] == inputSymptoms[index]:
                    return self.targetName

    DiseaseClasses = pd.read_csv("Disease Classes.csv")
    Groups = list(DiseaseClasses['Groups'])
    models = {}
    predictions = []

    diseases = pd.read_csv("Disease Dataset.csv")
    df = pd.DataFrame(diseases)

    # Input data as string and Sending Input as int to models
    inputSymptoms = [x.lower() for x in inputSymptoms]
    inputSymptomsIntegers = list(df.columns.drop('TARGET'))
    inputSymptomsIntegers = [x.lower() for x in inputSymptomsIntegers]
    for i in range(len(inputSymptomsIntegers)):
        found = False
        for n in range(len(inputSymptoms)):
            if inputSymptoms[n] == inputSymptomsIntegers[i]:
                inputSymptomsIntegers[i] = 1
                found = True
        if not found:
            inputSymptomsIntegers[i] = 0
    # print(inputSymptomsIntegers)

    # Making Trees
    for i in Groups:
        # if "-" not in i:
        #     x = i
        #     dfNew = pd.DataFrame()
        #     dfNew = dfNew.append(df.loc[(df['TARGET'] == x)])
        #     model = simpleSelection()
        #     target = dfNew['TARGET']
        #     symptoms=dfNew.drop('TARGET', axis='columns')
        #     model.fit(symptoms,target)
        #     models[i] = model
        if "-" in i:
            x = re.split("-", i)
        dfNew = pd.DataFrame()
        if len(x) != 1:
            for n in x:
                dfNew = dfNew.append(df.loc[(df['TARGET'] == n)])
            model = DecisionTreeClassifier()
            target = dfNew['TARGET']
            symptoms = dfNew.drop('TARGET', axis='columns')
            model.fit(symptoms, target)
            models[i] = model

    # predicting
    for i in Groups:
        getModel = models.get(i)
        predictions.append(getModel.predict([inputSymptomsIntegers]))


    classes = []
    # turn array objects into a single list
    predictions = [item for sublist in predictions for item in sublist]

    for i in Groups:
        classes.append(re.split("-", i))

    # removing useless predictions (firstly duplicates and then those which appear together in a
    # single group of diseases(i.e. classes list's sublist) and in predictions at the same time)
    res = []
    [res.append(x) for x in predictions if x not in res]
    predictions = res
    for sublist in classes:
        count = 0
        for word in sublist:
            for i in predictions:
                if i == word:
                    count += 1
                    if count > 1:
                        predictions.remove(i)

    # print(classes)
    return predictions
    # print(predictionsString)