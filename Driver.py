# from DiseaseClasses import Identification
from MedicineRecommendation import recommmendation
from Identifier import identifierForDisease

def driver(inputCurrentMedicine, inputCurrentIllness, inputSymptoms):
    inputSymptomsOrDiseases = [] # Symptoms from user + Diseases Identified for Medicine Recommendation
    predictionString = identifierForDisease(inputSymptoms)
    # predictionsString = 'You might be having: ' + ' '.join([str(elem) for elem in predictions])  # turn list into string
    # print(predictionsString)
    inputSymptomsOrDiseases.extend(inputSymptoms)
    inputSymptomsOrDiseases.extend(predictionString)
    recommmendationString = recommmendation(inputSymptomsOrDiseases, inputCurrentMedicine, inputCurrentIllness)
    # print(recommendationString)
    return predictionString, recommmendationString


# inputCurrentMedicine = ['']  # To be taken from chatbot
# inputCurrentIllness = ['']  # To be taken from chatbot
# inputSymptoms = ['sore throat']  # To be taken from chatbot
# predictionDisease, recommmendationDrug = driver(inputCurrentMedicine, inputCurrentIllness, inputSymptoms)
# print(predictionDisease, recommmendationDrug)
