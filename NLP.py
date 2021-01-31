import json
import spacy
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from spacy.tokens import span
import numpy as np
import symptoms as s_list
from neuralNetwork import check
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
    misspelled = spell.unknown(myinp)
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
            if ent.text in s_list.symptoms and ent.text != newLst:
                newLst.append(ent.text)
                test = test.replace(ent.text, " ")
                flag = True
        if check(test) not in newLst and flag != True:
            newLst.append(check(test))
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
                else:
                    return "Any other symptom?"





                #         choice2 = int(input())
                #         symp_details["severity"] = data["symptoms"][x]["question"]["answer2"][choice2 - 1]
                #         my_symp[x] = symp_details
                # else:
                #     continue;


def severity(disease, inp):
    # symp_details["duration"] = data["symptoms"][newLst[0]]["question"]["answer1"][duration - 1]
    # newLst = []
    inp = ""
    return data["symptoms"][disease]["question"]["severity"]

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get')
def get_bot_response():
    inp = request.args.get('msg')
    if inp:
        inp = inp.lower()
        disease = ""
        final_symptoms = []
        count = 0

        if len(inp) > 1:
            doc = nlp(spellcorrection(inp))
            disease = show_ents(doc)
            durationQuestion = critical_symptoms(disease)
            flag = True
            count += 1
            if durationQuestion:
                return durationQuestion
        if len(inp) == 1 and count == 1:
            sev = severity(disease, inp)
            return sev

if __name__ == "__main__":
    app.run(debug=True)
# disease  = ""
# final_symptoms = []
# count = 0
# inp = "1"
#
# if len(inp)>1:
#     doc = nlp(spellcorrection(inp))
#     disease = show_ents(doc)
#     durationQuestion = critical_symptoms(disease)
#     flag = True
#     count += 1
#     return durationQuestion
#



# print("please wait")
# medical_history()
# warning()
