import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

decoded_token = auth.verify_id_token(id_token)
uid = decoded_token["uid"]
