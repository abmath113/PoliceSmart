from warnings import catch_warnings
import pickle
import numpy as np
# from pymongo import MongoClient
import pyrebase

import random
import pandas as pd
from flask import Flask, render_template,request,redirect

app = Flask(__name__)


firebaseConfig={"apiKey": "AIzaSyBVO6-S0Qkg_uy-T-LvpcGYqPpbaTu7zlc",
  "authDomain": "fir-policedata.firebaseapp.com",
  "databaseURL": "https://fir-policedata-default-rtdb.firebaseio.com",
  "projectId": "fir-policedata",
  "storageBucket": "fir-policedata.appspot.com",
  "messagingSenderId": "244873735032",
  "appId": "1:244873735032:web:f469112a967e44a6a4b68d",
  "measurementId": "G-530QMD84LL"}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()




model = pickle.load(open("model_rank.pkl","rb"))
@app.route('/')
def hello_world(): 
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html',prediction = 'NULL')
    else:
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)

        if prediction[0] == 0:
            rank = 'ASP'
        elif prediction[0] == 1:
            rank = 'DSP'    
        elif prediction[0] == 2:
            rank = 'Inspector'
      

        return render_template('predict.html',prediction = rank)



@app.route('/CitizenSignUp', methods=['GET', 'POST'])
def CitizenSignUp():
    if request.method == "POST":
        first = request.form.get("firstname")
        last = request.form.get("lastname")
        mobile = request.form.get("phone")
        email = request.form.get("email")
        aadhar = request.form.get("aadhar")
        password = request.form.get("password")
        data={'first':first,'last':last,'mobile':mobile,'email':email,'aadhar':aadhar,'password':password}
        db.push(data)


        return redirect('/CitizenLogin')

    return render_template('signup.html')
  
  
@app.route('/CitizenLogin', methods=['GET', 'POST'])
def CitizenLogin():
    if request.method == "POST":
        password = request.form.get("password")
        aadhar = request.form.get("aadhar")
        data={'password':password,'aadhar':aadhar}
        db.push(data)
        return redirect('/complains')

    return render_template('login.html')
    

@app.route('/PoliceSignUp', methods=['GET', 'POST'])
def PoliceSignUp():
    if request.method == "POST":
        first = request.form.get("firstname")
        last = request.form.get("lastname")
        mobile = request.form.get("phone")
        email = request.form.get("email")
        aadhar = request.form.get("aadhar")
        password = request.form.get("password")
        data={'first':first,'last':last,'mobile':mobile,'email':email,'aadhar':aadhar,'password':password}
        db.push(data)

        return redirect('/policeLogin')

    return render_template('sign_police.html')


@app.route('/policeLogin', methods=['GET', 'POST'])
def policeLogin():
    if request.method == "POST":
        password = request.form.get("password")
        police = request.form.get("Police")
        data={'password':password,'police':police}
        db.push(data)
        return redirect('/complains')

    return render_template('login_police.html')

@app.route('/complains', methods=['GET', 'POST'])
def complain():
    if request.method == "POST":
        name = request.form.get("name")
        aadhar = request.form.get("aadhar")
        date = request.form.get("date")
        victimname = request.form.get("victim")
        place = request.form.get("place")
        crimetype = request.form.get("crimetype")
        description = request.form.get("describe")
        proof = request.form.get("proof")
        data={'name':name,'aadhar':aadhar,'date':date,'victimname':victimname,'place':place,'crimetype':crimetype,'description':description,'proof':proof}
        db.push(data)

        return render_template('Complain.html',message='done')

    return render_template('Complain.html')
     
     

if __name__ == '__main__':
    app.run(debug=True)
