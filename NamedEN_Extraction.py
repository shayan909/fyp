import spacy

nlp = spacy.load('en_ner_bc5cdr_md')

doc = nlp(u"I am having fever and cough")

symlst = []


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            symlst.append(ent.text)
        print(symlst)
    else:
        print("no ents found")



show_ents(doc)

# from spacy import displacy

# displacy.render(doc,style='ent',jupyter=False)
