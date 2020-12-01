import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"3 days")

from spacy import displacy

displacy.render(doc,style='ent',jupyter=False)
