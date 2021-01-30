from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('heartpred.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = int(request.form['age'])
        sex=int(request.form['sex'])
        cp=int(request.form['cp'])
        trestbps=int(request.form['trestbps'])
        chol=int(request.form['chol'])
        fbs=int(request.form['fbs'])
        restecg=int(request.form['restecg'])
        thalach=int(request.form['thalach'])
        exang=int(request.form['exang'])
        oldpeak=float(request.form['oldpeak'])
        slope=int(request.form['slope'])
        ca=int(request.form['ca'])
        thal=int(request.form['thal'])
        
        prediction=model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        output=round(prediction[0])
        print("output1",prediction)
        print("output ",output)
        if output==0:
            print("if")
            return render_template('index.html',prediction_text="person has less chance of heart attack")
        else:
            print("else")
            return render_template('index.html',prediction_text="person has more chance of heart attack")
            
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

