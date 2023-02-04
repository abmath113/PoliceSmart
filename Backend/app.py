from warnings import catch_warnings
# from pymongo import MongoClient
import random
import pandas as pd
from flask import Flask, render_template,request,redirect
import datetime
from firebase import firebase

firebase = firebase.FirebaseApplication("https://police-fir-ca11f-default-rtdb.firebaseio.com/",None)

data = {
    'Name':'Naval pimpude',
    'Email':'naval@gmail.com',
    'City':'Thane',
    'Location':'naupada',
    'Complain-type':'Noise pollution',
    'Complain':'Loud sound from tip top plaza during 12th exam after 10:30am also.'
}

result = firebase.post(data)

app = Flask(__name__)

x = datetime.datetime.now()
# client=MongoClient()
# client = MongoClient("mongodb://localhost:27017/")

# mydatabase = client['Uni_Registration']
# mycollection=mydatabase['RegistrationPass']

@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        
        "programming":"python"
        }
  
    

     


# @app.route('/login',methods=['GET', 'POST'])
# def login():
   
#     return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
