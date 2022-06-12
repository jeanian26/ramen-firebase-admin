import firebase_admin
from firebase_admin import credentials, auth,db

import datetime

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "uniqueco-33e4c",
  "private_key_id": "3727d173995971febf9bad66cc8a019ede627f10",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDsbYcUzgSHWuL6\naM5t6AsfCaEpdqmuHZyU2FKwGuBmz7KWvHHm23R2YX2Z6gElAvciMwmGy9kOT1KD\nvNxzqGBurSrAd7T05pZn/48JvZXKqoxHnrRFfnU4vYFWdekIuXRu6sU2/FXi4ubV\nmVdjEJJDJE7V1Qm1OrOdENaGCU6MDbbsX/b4XScV94FebuwU5gZrP4ZbOUS/9w6y\n3hIUjHf78nFcwqCix2XuQBDvPpZu8EnaGmPgWKLhFj8yHQMhuldo4phrv4nnURi6\n47+evUkp+qLPnM5deex47SCGybJPvLKcjEAIFhUTY0jO6xpR5hkoJqOliqzuQf3M\njEfa34OhAgMBAAECggEABAKBiX1K/16vvc58PcnzMlYP+SuNiinvZ2jZ0inKh4Pb\nRAozJlavfXh+0FbzKQUJWvehoDsh1cfLnvdbh8yhwg7GzFfbZlHo2B+x9djUywik\nc2yCIzGXXFx+bpB2YNMAYgcyTBHwhPYTMyk0HbaAvInHmoHP9dZmiHHqKYDL570l\ndJnYeHkQ1gN3kGNH2G9wOAP1BC6GKiOdQHdV/W0xBzWXnyihpJRmQUqr+2ejxPER\n0avKlt2hWbkh8WiosKPQVFNsYbQqVhRn3GpmBwaGw5JPExXGnhk/1+kSUKOn6OX8\n+gJ7mTt2AdHFEIEVFjl9WfIIwqUEK7U2h2JK+gFNqQKBgQD/1tlTuSYa9yJ0yT06\nWXDTr2Szu4DvTzFD1+AZh+ahIjcrDBEuq6QK8qUX36TNfyMvOIyaQXU72uODCi/H\n0FMlYa81NH2U3BFAAaOqmxOMofnllBtosCd7SNFIxxNf1ycTlgzIt1MepxL7gLq4\n219otKhokfr8QfmB0VOkJgbWLQKBgQDsk45zuk/3Qh3P7VO6Ucp++uv5Zpdu9+fn\noHiCy7apuxJCV4tffcACufsu8CJS/pQntC8uduCWu+yQgDsOkTNhcRblM61G3bSh\n1WeYUFjT4tjcPB2fSSnrVeaWSiQO3BsevOuTeuV0ktQSR9JGNvC73e1P/oncCVvk\nSy7iDepfxQKBgEoUy29r4HXUc/y/POSFe59AXXeR5t7k3o4Xl4OtD4I/Jxxm7R7H\ngsPMyTNlhhIfK3AD/uq345uGYXTTYUyJrVnYtGRCo86T/sa68sp3By0kxfjNbzZc\nM8KGLlvVkW2iHmWUgHUqaH4qwNtkxiy7ESB/l3hYNQYQkJAfrgmNHVOtAoGBANH0\nOi42oRU81hxb8Tyfreh3Y8jY5XgUBvmnjov1osyLOy8pZoV+olNJHsSPVMb3LCD4\nZg8EbVkYul+bjc3lywWlSb5r2FHWHKKrM98XH14cKn151IgydENo3tVuQwX1DRSA\ncUlXfh+w1wjKOLEbvRXdZOjjaxGeNLEskBUKaIBJAoGAH3NAeAkyj+BpCHVnxJsZ\np7UqLSAfL8RZCC1ltggAMjXB0CcFOVhVqVNtvvLFxvI1tJGYQfe/1PShRyw201Y7\n2HnZ9qKEuW+VXIfYlIfvuTZIIgCEmsdwkX3nOkIHBMheICMpOOS9MOVgfmx7PYM7\nMFbuDD1hDx5GiJaYJyY1cBA=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ppfbc@uniqueco-33e4c.iam.gserviceaccount.com",
  "client_id": "118353167285977030781",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ppfbc%40uniqueco-33e4c.iam.gserviceaccount.com"
}

)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://uniqueco-33e4c-default-rtdb.asia-southeast1.firebasedatabase.app"
})

def get_all_users():
    page = auth.list_users()
    arrayUsers = []
    data = get_account_data()
    for user in auth.list_users().iterate_all():
        users = {}
        users['email'] = user.email
        users['uid'] = user.uid
        users['data'] = data[user.uid]
        arrayUsers.append(users)
    return arrayUsers

def get_account_data():
    ref = db.reference('Account/')
    return ref.get()

def delete_user(uid):
    try:
        auth.delete_user(uid)
        deleteRecord(uid)
        return 'success'
    except Exception as e:
        print(e)
        return 'Error'

def create_account(email, password, contact, type, first_name, last_name):
    try:
        user = auth.create_user(
        email= email,
        email_verified=False,
        password=password,
        disabled=False)
        createRecord(email,contact,type, first_name, last_name, user.uid)
        return "Success"
    except Exception as e:
        return e

def updateUserDetails(email,password,uid):
    try:
        user = auth.update_user(
        uid,
        email=email,
        password=password)
        print('Sucessfully updated user: {0}'.format(user.uid))
        return 'Success'
    except Exception as e:
        return e

def createRecord(email,contactNumber,accountType,firstName, lastName,uid):
    ref = db.reference('/Account')
    users_ref = ref.child(uid)
    users_ref.set({
        'Uid':uid,
        'contactNumber':contactNumber,
        'type':accountType,
        'email':email,
        'firstName':firstName,
        'lastName':lastName,
        'dateCreated': int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
    })
    if accountType == 'university':
        createUniRecord(uid)

def createUniRecord(uid):
    ref = db.reference('/university')
    users_ref = ref.child(uid)
    users_ref.set({
        'Address':{
            "Barangay":" ",
            "City":"",
            "Country":"",
            "Lot":"",
            "Province":"",
            "ZipCode":""
        },
        "ProgramsOffered":{
            'random1':{
                "Field":''
            }
        },
    })

def deleteRecord(uid):
    ref = db.reference('/Account')
    users_ref = ref.child(uid)
    users_ref.set({})

