import json

with open('intents.json') as file:
    data = json.load(file)

import spacy

nlp = spacy.load('en_ner_bc5cdr_md')

inp = input("describe symptoms")
doc= nlp(inp)

symplst = []

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            symplst.append(str(ent.text))
        print(symplst)
    else:
        print("no ents found")


my_symp = {}
def critical_symptoms():
        critical_symptoms = ["fever", "cough", "chest discomfort", "chest pain", "wheezing", "sore throat", "headache",
                             "loss of smell"];

        if symplst.sort() == critical_symptoms.sort():
            for x in symplst:
                symp_details = {}
                if x in data["symptoms"]:
                        print(data["symptoms"][x]["question"]["duration"])
                        choice = int(input())
                        symp_details["duration"]=data["symptoms"][x]["question"]["answer1"][choice-1]
                        print(data["symptoms"][x]["question"]["severity"])
                        choice2 = int(input())
                        symp_details["severity"] = data["symptoms"][x]["question"]["answer2"][choice2 - 1]
                        my_symp[x] = symp_details


#print(my_symp)

def warning():
        concern = []
        for x in my_symp.keys():
                if my_symp[x]["severity"]=="danger" or my_symp[x]["duration"]=="danger":
                        concern.append(x)
        print(f"Caution!\nPlease seek immediate medical assistance for the following Symptom(s)")
        print(*concern, sep=",")
show_ents(doc)
critical_symptoms()
warning()


#print(data['symptoms']['fever']['question']['duration'])


