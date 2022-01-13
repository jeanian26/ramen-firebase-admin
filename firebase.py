import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("ramen-nado-86f76-firebase-adminsdk-mxqf0-bc33a83401.json")
firebase_admin.initialize_app(cred)

def get_all_users():
    page = auth.list_users()
    arrayUsers = []
    for user in auth.list_users().iterate_all():
        users = {}
        users['email'] = user.email
        users['uid'] = user.uid
        arrayUsers.append(users)

    return arrayUsers

def delete_user(uid):
    try:
        auth.delete_user(uid)
        return 'success'
    except Exception as e:
        print(e)
        return 'Error'

def create_account(email, password):
    try:
        user = auth.create_user(
        email= email,
        email_verified=False,
        password=password,
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False)
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
