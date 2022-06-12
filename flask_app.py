from flask import Flask, request
from flask_cors import CORS
import json
from flask_restful import Resource, Api
from firebase import delete_user, get_all_users,create_account,updateUserDetails

app = Flask(__name__)
api = Api(app)
CORS(app)

class UserAuth(Resource):
    def get(self):
        data = get_all_users()
        return data


    def delete(self):
        uid = request.args.get('uid')
        data = delete_user(uid)
        return data

    def post(self):
        # data = json.load(request.json)
        email = request.get_json().get('email')
        password = request.get_json().get('password')
        contactNumber = request.get_json().get('contact')
        type = request.get_json().get('type')
        firstName = request.get_json().get('firstname')
        lastName = request.get_json().get('lastname')

        result = create_account(email,password, contactNumber, type, firstName, lastName)
        return str(result)

class UpdateUser(Resource):
    def post(self):
        # data = request.json
        email = request.form.get("email")
        password = request.form.get('password')
        uid = request.form.get('uid')
        data = updateUserDetails(email, password, uid)
        print(data)
        return data

api.add_resource(UserAuth, '/')
api.add_resource(UpdateUser,'/update')
if __name__ == '__main__':
    app.run(debug=True)


