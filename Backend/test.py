from firebase import firebase

firebase = firebase.FirebaseApplication("https://police-fir-ca11f-default-rtdb.firebaseio.com/",None)

data = {
    'Name':'Naval pimpude',
    'Email':'naval@gmail.com',
    'City':'Thane',
    'Location':'naupada',
    'Complain type':'Noise pollution',
    'Complain':'Loud sound from tip top plaza during 12th exam after 10:30am also.'
}

result = firebase.post("https://police-fir-ca11f-default-rtdb.firebaseio.com/complains",data)
print(result)