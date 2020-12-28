import json
from typing import Dict, Any, List
import spacy
from nltk.tokenize import WordPunctTokenizer, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from spellchecker import SpellChecker
from spacy.tokens import Span
import numpy as np
import symptoms as s_list



with open('intents.json') as file:
    data = json.load(file)


#disease_model = 'en_ner_bc5cdr_md'en_core_sci_lg;
#medicine_model = 'en_ner_bionlp13cg_md';

nlp = spacy.load('en_core_sci_lg')
inp: str = input("Please describe your symptoms\n")



#Spelling Correction
myinp = word_tokenize(inp) #tokenize input
spell = SpellChecker() #initialize spellchecker method
spell.word_frequency.load_text_file("strings.txt")
misspelled = spell.unknown(myinp)
mistake = list(misspelled)
correct_spell=[]
print("Mistake")
print(mistake)

# with open('strings.txt') as f:
#     df = f.readlines()

for i in range(len(mistake)):
    for word in list(spell.candidates(mistake[i])):
        if word in s_list.symptoms:
            inp = inp.replace(mistake[i],word)
print(inp)
doc = nlp(inp)

my_symp = {} #user-entered-symptoms
symplst =[] #NER symptoms
medical_details = [] #medical_details extracted from user via NER
drug_history = []
final_symps=[]
testlst = []


def show_ents(doc):
    temp_lst = []
    if doc.ents:
        for ent in doc.ents:
            symplst.append(ent.text)

        x: str = ' '.join(symplst)
        x = x.split(' ')
        list(x)
        print(x)
        xlst = []
        for split_word in range(len(x)):
            if x[split_word] in s_list.symptoms:
                xlst.append(x[split_word])
            elif len(x) > split_word:
                if x[split_word-1]+' '+x[split_word] in s_list.symptoms:
                   xlst.append(x[split_word-1]+' '+x[split_word])

        print(xlst)

        for i in xlst:
            temp_lst=str(i).split(" ")
            if len(temp_lst) > 1:
                s = "_"
                s = s.join(temp_lst)
                temp_lst=[]
                final_symps.append(s)
            else:
                final_symps.append(i)
    else:
        print("no ents found")
    print(final_symps)
    if len(final_symps) > 0:
        critical_symptoms(xlst)


def critical_symptoms(myList):
        critical_symptoms = ["fever", "cough", "chest discomfort", "chest pain", "wheezing", "sore throat", "headache",
                             "loss of smell","high fever"];

        if myList.sort() == critical_symptoms.sort():
            for x in myList:
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

# print("Please wait")
# medical_history()
# warning()

#print(data['symptoms']['fever']['question']['duration'])


