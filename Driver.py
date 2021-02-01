from DiseaseClasses import Identification
from MedicineRecommendation import recommmendation


def driver(inputCurrentMedicine, inputCurrentIllness, inputSymptoms):
    inputSymptomsOrDiseases = [] # Symptoms from user + Diseases Identified for Medicine Recommendation
    predictions = Identification(inputSymptoms)
    predictionsString = 'You might have:' + ' '.join([str(elem) for elem in predictions])  # list turn into string
    # print(predictionsString)
    inputSymptomsOrDiseases.extend(inputSymptoms)
    inputSymptomsOrDiseases.extend(predictions)
    recommmendationString = recommmendation(inputSymptomsOrDiseases, inputCurrentMedicine, inputCurrentIllness)
    # print(recommendationString)
    # return predictionsString, recommmendationString
    return predictionsString


# inputSymptomsOrDiseases = ['Wheezing', 'Redness in one or both eyes', 'Itchiness in one or both eyes',
#                            'Watery Eyes', 'phlegm', 'Stuffy Nose']
# inputSymptomsOrDiseases = ['COUGH', 'hives']
# inputCurrentMedicine = ['Ibuprofen']
# inputCurrentIllness = ['Heart Disease']
# pred = driver(inputCurrentMedicine, inputCurrentIllness, inputSymptomsOrDiseases)
# a = pred.pop()
# print('-'.join(a))