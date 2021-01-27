import json
import spacy
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from spacy.tokens import span
import numpy as np
import symptoms as s_list
from neuralNetwork import check

nlp = spacy.load('en_core_sci_lg')
#disease_model = 'en_ner_bc5cdr_md'en_core_sci_lg;
#medicine_model = 'en_ner_bionlp13cg_md';


with open('intents.json') as file:
    data = json.load(file)
my_symp = {} #user-entered-symptoms
symplst =[] #ner symptoms
medical_details = [] #medical_details extracted from user via ner
drug_history = []
final_symps=[]
testlst = []



inp: str = input("please describe your symptoms\n")


def spellcorrection(inp):

    myinp = word_tokenize(inp) #tokenize input
    spell = SpellChecker() #initialize spellchecker method
    spell.word_frequency.load_text_file("strings.txt")
    misspelled = spell.unknown(myinp)
    mistake = list(misspelled)
    correct_spell=[]
    print("mistake")
    print(mistake)

    for i in range(len(mistake)):
        for word in list(spell.candidates(mistake[i])):
            if word in s_list.symptoms:
                inp = inp.replace(mistake[i],word)

    # for symtom in x:
    #     newLst.append(check(symtom))
    #     print(newLst)

    doc = nlp(inp)
    show_ents(doc)


def show_ents(doc):
    temp_lst = []
    newLst = []

    if doc.ents:
        for ent in doc.ents:
            symplst.append(ent.text)
            test = inp.replace(ent.text," ")
        symplst.append(check(test))

    else:
        symplst.append(check(inp))

    x: str = ' '.join(symplst)
    x = x.split(' ')
    list(x)

    xlst = []
    for split_word in range(len(x)):
        if x[split_word] in s_list.symptoms:
            xlst.append(x[split_word])
        elif len(x) > split_word:
            if x[split_word - 1] + ' ' + x[split_word] in s_list.symptoms:
                xlst.append(x[split_word - 1] + ' ' + x[split_word])

    for i in xlst:
        temp_lst = str(i).split(" ")
        if len(temp_lst) > 1:
            s = "_"
            s = s.join(temp_lst)
            temp_lst = []
            final_symps.append(s)
        else:
            final_symps.append(i)

    print(symplst)

    print(final_symps)
    if len(final_symps) > 0:
        critical_symptoms(xlst)


def critical_symptoms(mylist):
        critical_symptoms = ["fever", "cough", "chest discomfort", "chest pain", "wheezing", "sore throat", "headache",
                             "loss of smell","high fever"];

        if mylist.sort() == critical_symptoms.sort():
            for x in mylist:
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



spellcorrection(inp)


# print("please wait")
# medical_history()
# warning()



def medical_history():
    nlp = spacy.load('en_core_sci_lg')
    med_hist = input("mention your medical condition(s) if any\n")
    drg_hist = input("\nplease mention drug names you are currently taking if any\n")
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



def warning():
        concern = []
        for x in my_symp.keys():
                if my_symp[x]["severity"]=="danger" or my_symp[x]["duration"]=="danger":
                        concern.append(x)
        if len(concern)>=1:
            print(f"\ncaution!\nplease seek immediate medical assistance for the following symptom(s)")
            print(*concern, sep=",")
