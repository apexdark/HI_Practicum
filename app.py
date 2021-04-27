import main
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def dropdown():
    return render_template('index.html', symptoms=main.symptoms)

@app.route('/check_disease', methods=['POST'])
def check_disease():
    selected_symptoms = []
    if(request.form['Symptom1']!="") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if(request.form['Symptom2']!="") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if(request.form['Symptom3']!="") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if(request.form['Symptom4']!="") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])

    disease = main.check_symptoms(selected_symptoms)
    return render_template('check_disease.html',disease=disease,symptoms=main.symptoms)


if __name__ == '__main__':
    app.run()