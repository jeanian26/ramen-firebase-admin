import firebase_admin
from firebase_admin import credentials, auth,db

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "ramen-nado-86f76",
  "private_key_id": "bc33a83401cbbaba64f9d0b3eebe9855ee54d617",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCedoQ6GlwBdc/A\nDGZ+wCJP9BOIlsWTrcOSc3A5polgKrDykzGL9QgF7WDh9SduNfkMCJ5MSH795MWd\nbhXD5d7z6V7AbKGuYbeGxUp1NDtzSdpjmd9IpAMhlpJVijVwUno9zDMfaNKxoWQh\nLByLbe0mK/iS1KEsPPCwJi0+CAb+f7wKkdktoSFks7MufvVcIMDOZJxpyfGm6sO2\nXY9FjlujvstuHd2nobd5WWl9bMYUT5dtq3GgxjHXdFMP/6cj2bGIZCYEJeWwSIhz\nMbhbgK0rSgZjj2rSYNIAvRe4sQJCT7/batsRisSZtm5VAeckEdqihE8L75AvnVFl\ngtF5rTnJAgMBAAECggEACRRy7q5ge7/vq8o6HESvoqOyc9bp0tS32l4tfcwuXnmL\nwpaPFf0wHMDVlpT40a6biuY6hdX4mt0/Oo5ahmtXS2QhpwaCfC7CuKD4637W8jv2\n3NKuEeg9+rB5SZf+CGXddcmL216jBgUgqurvZsjheBi4aVdwNcv3IazKVl3Y4r/B\nX+Of47A7pGLvye9uB2dVTg1/ew1YRDratQ5JBwreBLP1YHthKgS0N72dDp46auY1\nL4kNgZhlhws0dwwqs7Uz8gk5lXMc6Dhl37SQjv1MpP45KIEvpwGLkICFDuYG8yWx\nMRniZEkacZOkUm0aBKx3uoz+tfAJYmeCAaaYy8yNAQKBgQDTEycg9TeZag7mZJLl\nbADA+nC6qFhhnUlc5t71eEn0S1ELUzm6iidwXKzqsoLH9j0IVYlKCSmW2OWdGpGy\nXjvR2GQoZd07m25ei4BCIrEKmMSVHFLcvkKAxc+GJaUV7zd5cci2FWbWcfXInOA5\nZAiAKlFd47cvdOXXCnG1IYg8gQKBgQDAMLKjaCQKyqD4bVSoChLT/A0ALHNDIqh6\niQGI9U7UaiNElTT6cOCJGwPe2N6jw84ksk2t3Mcv4mdo0qLbZ1wCinFrYQ18Bq+V\nl2z/+aj9aFlteq6uEmaS8awaZk2q5wRHG8J1R2+RU/BOUbFEpTqqNijv5omU+Dbp\nwPVv07t5SQKBgQC+eak017Udz5S0movpVwZzH019VA+1vx+GI52OPMfYGeN/6dHN\noYCnqCou/XqBgpdfHvlug0gxpXfHx0M1iE5JNxJjVlFHyiLWVOMgS3gijOvRd6bb\nJyKSXG/CqdQJMD+Ka4Dpt/R+joZzTAYYJEp7hjS5Gpajz8TdwsIL57+ugQKBgQCF\ncIpnuIPl1kCjnE1+Cth9xPBF4Zb50xOFWKDvNdtQ0ozALpTFGiBcMZyjWpJixC3Z\n/s6+W58VGS5RcoZOrdoNjZAoTQ9uwLmitKuiovZ5U71brSWhiPcdKZ0kC0n70kB/\nGsAOa9YD4nLj/gaFse8khUwxHTEDdL+z1xzSUwFEuQKBgQCmu0Md1gaxzAOfyD3s\nnGUjnUZCg2uEO7AQiCFN0VH82E+h/EKbA/qT6gGTnlsYU1U1sUSDfcLEm9XSiffR\niY2rSvapNT8yK5ndYXXNAHBK9LwHxtdtyTtjbr/c4i5gvQJDM3zbKTZKli8KznmG\nRiLaZWiIuOi+NIGxp12oRhQV8A==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-mxqf0@ramen-nado-86f76.iam.gserviceaccount.com",
  "client_id": "102689171191973104130",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mxqf0%40ramen-nado-86f76.iam.gserviceaccount.com",
}
)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://ramen-nado-86f76-default-rtdb.asia-southeast1.firebasedatabase.app"
})

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
        createRecord(email, user.uid)


        return user.uid
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

def createRecord(email,uid):
    ref = db.reference('/accounts')
    users_ref = ref.child(uid)
    users_ref.set({
        'alanisawesome':False,
        'email':email,
        'name':'',
        'phone':'',
        'rider':False
    })
