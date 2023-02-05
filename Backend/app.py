from warnings import catch_warnings
# from pymongo import MongoClient
import random
import pandas as pd
from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/CitizenSignUp', methods=['GET', 'POST'])
def CitizenSignUp():
    if request.method == "POST":
        first = request.form.get("firstname")
        last = request.form.get("lastname")
        mobile = request.form.get("phone")
        email = request.form.get("email")
        aadhar = request.form.get("aadhar")
        password = request.form.get("password")

        return redirect('/CitizenLogin')

    return render_template('signup.html')
  
  
@app.route('/CitizenLogin', methods=['GET', 'POST'])
def CitizenLogin():
    if request.method == "POST":
        password = request.form.get("password")
        aadhar = request.form.get("aadhar")
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

        return redirect('/policeLogin')

    return render_template('sign_police.html')


@app.route('/policeLogin', methods=['GET', 'POST'])
def policeLogin():
    if request.method == "POST":
        password = request.form.get("password")
        police = request.form.get("Police")
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

        return render_template('Complain.html',message='done')

    return render_template('Complain.html')
     

if __name__ == '__main__':
    app.run(debug=True)
