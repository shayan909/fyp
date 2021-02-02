import json
from typing import List, Any
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from spellchecker import SpellChecker
from spacy.tokens import span
import numpy as np
import symptoms as s_list
from neuralNetwork import check
from Driver import driver
from flask import Flask, render_template, request

app = Flask(__name__)

nlp = spacy.load('en_core_sci_lg')
#disease_model = 'en_ner_bc5cdr_md'en_core_sci_lg;
#medicine_model = 'en_ner_bionlp13cg_md';

inp = ""


with open('intents.json') as file:
    data = json.load(file)
my_symp = {} #user-entered-symptoms
symplst =[] #ner symptoms
medical_details = [] #medical_details extracted from user via ner
drug_history = []
final_symps=[]
testlst = []



# inp: str = input("please describe your symptoms\n")


def spellcorrection(inp):

    myinp = word_tokenize(inp) #tokenize input
    spell = SpellChecker() #initialize spellchecker method
    spell.word_frequency.load_text_file("strings.txt")

    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in myinp if not w in stop_words]
    filtered_sentence = []

    for w in myinp:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(filtered_sentence)

    misspelled = spell.unknown(filtered_sentence)
    mistake = list(misspelled)
    correct_spell=[]
    print("mistake")
    print(mistake)


    for i in range(len(mistake)):
        for word in list(spell.candidates(mistake[i])):
            if word in s_list.symptoms:
                inp = inp.replace(mistake[i],word)


    return inp


def show_ents(doc):
    temp_lst = []
    newLst = []
    flag = False

    test = inp
    if doc.ents:
        for ent in doc.ents:
            if ent.text in s_list.symptoms and ent.text not in newLst:
                newLst.append(ent.text)
                test = test.replace(ent.text, " ")
                flag = True
            elif check(inp) not in newLst and flag != True:
                print(check(inp))
                newLst.append(check(inp))
                flag = False


        # x: str = ' '.join(symplst)
        # x = x.split(' ')
        # list(x)
        #
        # xlst = []
        # for split_word in range(len(x)):
        #     if x[split_word] in s_list.symptoms:
        #         xlst.append(x[split_word])
        #     elif len(x) > split_word:
        #         if x[split_word - 1] + ' ' + x[split_word] in s_list.symptoms:
        #             xlst.append(x[split_word - 1] + ' ' + x[split_word])
        #
        # for i in xlst:
        #     temp_lst = str(i).split(" ")
        #     if len(temp_lst) > 1:
        #         s = "_"
        #         s = s.join(temp_lst)
        #         temp_lst = []
        #         final_symps.append(s)
        #     else:
        #         final_symps.append(i)

        print(newLst)

        # print(final_symps)

    return newLst


def critical_symptoms(newLst):
        symp_details = {}
        mylist = []

        critical_symptoms = ["fever", "cough", "chest discomfort", "chest pain", "wheezing", "sore throat", "headache",
                             "loss of smell","high fever"];


        if newLst.sort() == critical_symptoms.sort():
            for x in newLst:
                if x in data["symptoms"]:
                    return data["symptoms"][x]["question"]["duration"]

                #         choice2 = int(input())
                #         symp_details["severity"] = data["symptoms"][x]["question"]["answer2"][choice2 - 1]
                #         my_symp[x] = symp_details
                # else:
                #     continue;


def severity(disease):
    sym = disease.pop()
    disease.append(sym)
    return data["symptoms"][sym]["question"]["severity"]

    # symp_details["duration"] = data["symptoms"][newLst[0]]["question"]["answer1"][duration - 1]
    # newLst = []

def medical_history(med):

    nlp = spacy.load('en_core_sci_lg')
    doc = nlp(med)
    if doc.ents:
        for ent in doc.ents:
            medical_details.append(str(ent.text))

    return medical_details.pop()


# def drug_history():
#     drg_hist = input("\nplease mention drug names you are currently taking if any\n")
#
#     # if i == 1:
#     # doc = nlp(drg_hist)
#     # if doc.ents:
#     #     for ent in doc.ents:
#     #         drug_history.append(str(ent.text));
#     # print(drug_history)


def warning():
        concern = []
        for x in my_symp.keys():
                if my_symp[x]["severity"]=="danger" or my_symp[x]["duration"]=="danger":
                        concern.append(x)
        if len(concern)>=1:
            return f"\ncaution!\nplease seek immediate medical assistance for the following symptom(s) \n {concern}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get')
def get_bot_response():

    inp = request.args.get('msg')
    global disease
    global array
    global count
    global medHistory
    global duration
    global degree
    medHistory = []
    global medicine
    medicine = []
    array = []
    if inp: #I am having xyz
        inp = inp.lower()
        if len(inp) > 3 and 'count' not in globals():
            doc = nlp(spellcorrection(inp))
            print(doc)
            disease = show_ents(doc)
            durationQuestion = critical_symptoms(disease)
            flag = True
            count = 1
            print(count)
            array.append(disease)
            if durationQuestion:
                return durationQuestion
            else:
                count = 2
                return f"You have {str(disease)}, enter any other symptom or press Enter"

        elif len(inp)==1 and count == 1: #duration, return severity Question
            print(disease)
            count = 2
            if severity(disease):
                sev = severity(disease)
                if inp == "1":
                    duration = "mild"
                elif inp == "2":
                    duration = "moderate"
                elif inp == "3":
                    duration = "severe"
                elif inp == "4":
                    duration = "severe"

                print(duration)

                return sev


        elif len(inp) == 1 and count == 2:#severity,
            print(duration)

            if inp == "1":
                degree = "mild"
            elif inp == "2":
                degree = "moderate"
            elif inp == "3":
                degree = "severe"
            elif inp == "4":
                degree = "severe"

            print(degree)
            count = 3
            return "\n Do you have any other symptoms?"

        elif inp == "no" and count == 3:
            count = 4
            print(duration)
            return "mention your major medical condition"

        elif inp == "yes" and count == 3:
            count = 7
            return "Please mention other symptom"

        if len(inp) > 3 and count == 7:
            doc = nlp(spellcorrection(inp))
            print(doc)
            disease = show_ents(doc)
            durationQuestion = critical_symptoms(disease)
            flag = True
            count = 1
            print(count)
            array.append(disease)
            if durationQuestion:
                return durationQuestion
            else:
                count = 2
                return f"You have {str(disease)}, enter any other symptom or press Enter"

        elif len(inp)>3 and count == 4:
            cond = medical_history(inp)
            medHistory.append(cond)
            count = 5
            return "mention medicine you are taking"

        elif len(inp)>3 and count == 5:
            count = 6

            if duration == "severe":
                s = f"\nYour symptom's duration is alarming please seek medical attention"
            else:
                s = ""

            if degree == "severe":
                d = f"\nYour symptom is severe please seek medical attention immediately"
            else:
                d = ""

            med = medical_history(inp)
            medicine.append(med)
            a, b = driver(medicine, medHistory, disease)
            return a + f"\n {b}"+f"\n{s}\n{d}"



if __name__ == "__main__":
    app.run(debug=False)


# inp = "i have temperature"
# doc = nlp(spellcorrection(inp))
# disease = show_ents(doc)


