import pandas as pd
from sklearn.ensemble import RandomForestClassifier


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


def identifierForDisease(inputSymptoms):
    diseases = pd.read_csv("Disease Dataset.csv")
    df = pd.DataFrame(diseases)
    mixedSymptoms = diseases.drop('TARGET', axis='columns')
    target = diseases['TARGET']

    # Converting symptoms to integers
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
    print(inputSymptomsIntegers)

    # Handling Distinct Symptoms
    # DiseaseClasses = pd.read_csv("Disease Classes.csv")
    # Groups = list(DiseaseClasses['Groups'])
    # models = {}
    # predictions = []
    # for i in Groups:
    #     if "-" not in i:
    #         x = i
    #         dfNew = pd.DataFrame()
    #         dfNew = dfNew.append(df.loc[(df['TARGET'] == x)])
    #         model = simpleSelection()
    #         target = dfNew['TARGET']
    #         symptoms = dfNew.drop('TARGET', axis='columns')
    #         model.fit(symptoms, target)
    #         models[i] = model
    #
    # for i in Groups:
    #     getModel = models.get(i)
    #     predictions.append(getModel.predict([inputSymptomsIntegers]))
    #
    # print(predictions)
    # Random Forest Classifier
    model = RandomForestClassifier(random_state=0)
    model.fit(mixedSymptoms, target)
    # model = DecisionTreeClassifier(random_state=0)
    # model.fit(mixedSymptoms, target)
    # prediction = model.predict([inputSymptomsIntegers])
    prediction = model.predict_proba([inputSymptomsIntegers])
    print(model.classes_)
    prediction = model.predict([inputSymptomsIntegers])
    predictionString = 'You might be having: ' + ' '.join([str(elem) for elem in prediction])  # turn list into string
    return predictionString


# inputSymptoms = ['Fever', 'Phlegm', 'Cough', 'Long_Term_Breathing_Or_Wheezing', 'Malaise', 'Chest_Pain',
#                  'Gas', 'Pain_In_One_Or_More_Areas_Of_Neck','Tobacco_History']


# print(identifierForSingleDisease(inputSymptoms))


