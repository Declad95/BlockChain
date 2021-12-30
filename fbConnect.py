import firebase_admin
from firebase_admin import credentials, db, firestore


cred = credentials.Certificate("medi-web-bfacf-firebase-adminsdk-ju7ib-1d5cd78c9f.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://medi-web-bfacf-default-rtdb.firebaseio.com'})
# Get a database reference to our posts
ref = db.reference('/medi-web-bfacf-default-rtdb/')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())



"""
cred = credentials.Certificate("medi-web-bfacf-firebase-adminsdk-ju7ib-1d5cd78c9f.json")
#firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://medi-web-bfacf-default-rtdb.firebaseio.com'})   
firebase_admin.initialize_app(cred)
datab = firestore.client()
userref = datab.collection(u'users')
docs = userref.stream()
#ref = db.reference('medi-web-bfacf-default-rtdb/users')

for doc in docs:
    print('{} : {}'.format(doc.id, doc.to_dict()))
"""