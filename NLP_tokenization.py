#import spacy
#nlp = spacy.load("en_core_web_sm")

# If this works, it'd indicate that the problem is related to the way spaCy
# detects installed packages.
# this is a new change

import en_core_web_sm
nlp = en_core_web_sm.load()

my_string = '"We\'re moving to L.A.ss!" '

print(my_string)
doc = nlp(my_string)

for token in doc:
    print(token.text)

doc2 = nlp(u"We're here to help! send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")
for t in doc2:
    print(t)

doc3=nlp(u"A 5km NYC cab ride costs $10.30")
for t in doc3:
    print(t)

doc4 = nlp(u"Let's visit St. louis in the U.S. next year. ")
for t in doc4:
    print(t)