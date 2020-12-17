import json
from typing import Dict, Any
import spacy
from nltk.tokenize import WordPunctTokenizer, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from spellchecker import SpellChecker


with open('intents.json') as file:
    data = json.load(file)


#disease_model = 'en_ner_bc5cdr_md';
#medicine_model = 'en_ner_bionlp13cg_md';

nlp = spacy.load('en_core_sci_lg')
inp: str = input("Please describe your symptoms\n")



#Spelling Correction
arr= []
myinp = word_tokenize(inp) #tokenize input
spell = SpellChecker() #initialize spellchecker method
spell.word_frequency.load_text_file("strings.txt")
misspelled = spell.unknown(myinp)
mistake = list(misspelled)
print(mistake)
#print(misspelled)
correct_spell = []

for i in range(len(mistake)):
    for x in spell.candidates(mistake[i]):
        if x in data["symptoms"]:
            inp = inp.replace(mistake[i],x)
        # else:
        #     inp = inp.replace(mistake[])
        # #     if word in data["symptoms"]:
        #         print(word)
        #     # correct_spell.append(correct)
print(inp)
# for w in range(len(correct_spell)):
#     inp=inp.replace(mistake[w],correct_spell[w])
# print(inp)

doc = nlp(inp)

my_symp = {} #user-entered-symptoms
symplst = [] #NER symptoms
medical_details = [] #medical_details extracted from user via NER
drug_history = []


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            symplst.append(str(ent.text))
        print(symplst)
    else:
        print("no ents found")



def critical_symptoms():
        critical_symptoms = ["fever", "cough", "chest discomfort", "chest pain", "wheezing", "sore throat", "headache",
                             "loss of smell","high fever"];

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
                else:
                    continue;


def medical_history():
    nlp = spacy.load('en_core_sci_lg')
    med_hist = input("mention your medical condition(s) if any\n")
    drg_hist = input("\nPlease mention drug names you are currently taking if any\n")
    for i in range(2):
        if i == 0:
            doc = nlp(med_hist)
            if doc.ents:
                for ent in doc.ents:
                    medical_details.append(str(ent.text))
        elif i == 1:
            doc = nlp(drg_hist)
            if doc.ents:
                for ent in doc.ents:
                    drug_history.append(str(ent.text));
    print(medical_details)
    print(drug_history)


#print(my_symp)

def warning():
        concern = []
        for x in my_symp.keys():
                if my_symp[x]["severity"]=="danger" or my_symp[x]["duration"]=="danger":
                        concern.append(x)
        if len(concern)>=1:
            print(f"\nCaution!\nPlease seek immediate medical assistance for the following Symptom(s)")
            print(*concern, sep=",")



show_ents(doc)
critical_symptoms()

print("Please wait")
medical_history()
warning()

#print(data['symptoms']['fever']['question']['duration'])


