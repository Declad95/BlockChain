from firebase import firebase
from firebase_admin import credentials, db, firestore

cred = credentials.Certificate("medi-web-bfacf-firebase-adminsdk-ju7ib-1d5cd78c9f.json")

firebase = firebase.FirebaseApplication("https://medi-web-bfacf-default-rtdb.firebaseio.com/", cred)

result = firebase.get("/medi-web-bfacf-default-rtdb/users", " ")

print(result)