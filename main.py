import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

train = pd.read_csv('Datasets/Training.csv')
test = pd.read_csv('Datasets/Testing.csv')
df = train.copy()

# Making the column names more readable
old_colnames = list(df)
new_colnames = []
for word in old_colnames:
    word = word.capitalize()
    if "_" in word:
        word = word.replace("_", " ")
    new_colnames.append(word)

df.rename(columns={i:j for i,j in zip(old_colnames, new_colnames)}, inplace=True)

x = df[df.columns[:-1]]
y = df['Prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)


svc_classifier = SVC()
svc_classifier.fit(x_train,y_train)

indices = [i for i in range(132)]
symptoms = sorted(df.columns.values[:-1])
symptoms_dictionary = dict(zip(symptoms,indices))

def check_symptoms(symptoms):
    symptom_label = [0 for i in range(132)]
    for symptom in symptoms:
        idx = symptoms_dictionary[symptom]
        symptom_label[idx] = 1
    symptom_label= np.array(symptom_label)
    symptom_label = symptom_label.reshape((-1,1)).transpose()
    return(svc_classifier.predict(symptom_label))
