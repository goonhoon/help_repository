import spacy
from spacy.tokens import SpanGroup
from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("span_ruler", name="ruler")

patterns = [{"label": "Effective Date", "pattern": [
    {"ENT_TYPE": "DATE", "OP": "{4,}"},
    {"TEXT": '('},
    {"TEXT": 'the'},
    {"TEXT": '"'},
    {"TEXT": 'Effective'},
    {"TEXT": 'Date'},
    {"TEXT": '"'},
    {"TEXT": ')'}
]}]

ruler.add_patterns(patterns)


for i in range(1, 510):

    text_open = open(f"inputfiles/ ({i}).txt", "r", encoding='utf8')
    text = text_open.read()
    doc = nlp(text)

    doc.spans["Hovno"] = SpanGroup(doc)
    db = DocBin()
    for span in doc.spans["ruler"]:
        doc.spans["Hovno"].append(span)
        for span in doc.spans["Hovno"]:
            doc.set_ents(entities=[span], default="unmodified")
            print(span.text, span.label_)

    text_open.close()


    db.add(doc)
    db.to_disk(f"./train/{i}.spacy")




