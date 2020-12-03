import json

with open('intents.json') as file:
    data = json.load(file)

critical_symptoms = ["fever","cough","chest discomfort","chest pain","wheezing","sore throat","headache", "loss of smell"];

symplst = ["fever"]
my_symp = {}
if symplst.sort() == critical_symptoms.sort():
        for x in symplst:
                symp_details = {}
                if x in data["symptoms"]:
                        print(data["symptoms"][x]["question"]["duration"])
                        choice = int(input())
                        symp_details["duration"]=data["symptoms"][x]["question"]["answer1"][choice-1]
                        print(symp_details)
                        print(data["symptoms"][x]["question"]["severity"])
                        choice2 = int(input())
                        symp_details["severity"] = data["symptoms"][x]["question"]["answer2"][choice2 - 1]
                        my_symp[x] = symp_details

print(my_symp)
#print(my_symp)



#print(data['symptoms']['fever']['question']['duration'])


