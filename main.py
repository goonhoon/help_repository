import spacy
from spacy.tokens import SpanGroup, Span
from spacy import displacy
from spacy.tokens import DocBin
import re



nlp = spacy.blank("en")
ruler = nlp.add_pipe("span_ruler", "ruler1")
nlp.add_pipe("sentencizer")

patterns = [{"label": "Governing Law", "pattern": "the laws of the"},
            {"label": "Governing Law", "pattern": "shall be governed by"},
            {"label": "Governing Law", "pattern": "governed in accordance with"},
            {"label": "Governing Law", "pattern": "governed under"},
            {"label": "Governing Law", "pattern": "in accordance with the laws of"},
            {"label": "Assignment", "pattern": "may be assigned"},
            {"label": "Assignment", "pattern": "may not be assigned"},
            {"label": "Assignment", "pattern": "shall not assign"},
            {"label": "Assignment", "pattern": "shall not be assigned"},
            {"label": "Assignment", "pattern": "shall not be assignable"},
            {"label": "Assignment", "pattern": "the right to assign"},
            {"label": "Assignment", "pattern": "no assignment"},
            {"label": "Pricing", "pattern": "calculated as follows"},
            {"label": "Pricing", "pattern": "the price shall be"},
            {"label": "Pricing", "pattern": "shall pay"},
            {"label": "Pricing", "pattern": "undertakes to pay"},
            {"label": "Notices", "pattern": "Notices under this"},
            {"label": "Notices", "pattern": "any notice required"},
            {"label": "Notices", "pattern": "any notice served"},
            {"label": "Notices", "pattern": "any notice given"},
            {"label": "Notices", "pattern": "all notices provided"},
            {"label": "Notices", "pattern": "every notice"},
            {"label": "Term", "pattern": "term of this"},
            {"label": "Term", "pattern": "shall commence on the Effective Date"},
            {"label": "Term", "pattern": "come into force on the date"},
            {"label": "Term", "pattern": "effective until terminated"},
            {"label": "Term", "pattern": "this agreement commences"},
            {"label": "License Grant", "pattern": "grant to each other a limited license"},
            {"label": "License Grant", "pattern": "Licensor hereby grants"},
            {"label": "License Grant", "pattern": "irrevocable, worldwide"},
            {"label": "License Grant", "pattern": "fully paid, limited, non exclusive"},
            {"label": "Termination/Convenience", "pattern": "may terminate this Agreement"},
            {"label": "Termination/Convenience", "pattern": "may terminate this Agreement at any time"},
            {"label": "Termination/Convenience", "pattern": "to terminate this Agreement"},
            {"label": "Termination/Convenience", "pattern": "right to terminate this Agreement immediately upon written notice"},
            {"label": "Termination/Convenience", "pattern": "may terminate  this  Agreement  for no reason or for any reason "},
            {"label": "Termination/Convenience", "pattern": "may terminate this Agreement for any reason"},
            {"label": "Termination/Convenience", "pattern": "shall have the right to terminate"},
            {"label": "Non-solicit", "pattern": "employee of the other"},
            {"label": "Non-solicit", "pattern": "any employee of the"},
            {"label": "Insurance", "pattern": "any employee of the"},
            {"label": "Insurance", "pattern": "as an additional insured"},
            {"label": "Covenant Not to Sue", "pattern": "shall not now or in the future contest the validity of"},
            {"label": "Covenant Not to Sue", "pattern": "contest the validity of"},
            {"label": "IP Assignment", "pattern": "right, title and interest in and to"},
            {"label": "Warranty", "pattern": "represents and warrants that"},
            {"label": "Warranty", "pattern": "be free from defects"}

            ]

ruler.add_patterns(patterns)

for i in range(1,400):

    text_open = open(f"inputfiles/ ({i}).txt", "r", encoding='utf8')
    text = text_open.read()
    doc = nlp(text)


    doc.spans["sentences"] = SpanGroup(doc)
    db = DocBin()
    for sentence in doc.sents:
        for span in doc.spans["ruler"]:
            if span.start >= sentence.start and span.end <= sentence.end:
                doc.spans["sentences"] += [
                    Span(doc, start=sentence.start, end=sentence.end, label=span.label_)


                ]
                doc.set_ents(entities=[span], default="unmodified")
                for span in doc.spans["sentences"]:
                    print(span.label_)

    text_open.close()


    db.add(doc)
    db.to_disk(f"./train/{i}.spacy")




