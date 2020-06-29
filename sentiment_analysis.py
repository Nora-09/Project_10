import requests

r = requests.get('http://127.0.0.1:3000/get_data')
r.json()
get_data_1 = r.json()

t = list()
n = list()

for i in get_data_1:
    t.append(i[0])
    n.append(i[1])

import re 
def clean_text(text):
    text = text.lower()
    text = re.sub("@[a-z0-9_]+", ' ', text)
    text = re.sub("[^ ]+\.[^ ]+", ' ', text)
    text = re.sub("[^ ]+@[^ ]+\.[^ ]", ' ', text)
    text = re.sub("[^a-z\' ]", ' ', text)
    text = re.sub(' +', ' ', text)
    return text

texts = []
for text in t:
    clean_1 = clean_text(text)
    texts.append(clean_1)
t = texts

import pickle
with open('model.pickle', 'rb') as file:
    model = pickle.load(file)
with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)

example_test = vectorizer.transform(texts)
example_result = model.predict(example_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(n, example_result))
