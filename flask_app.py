from flask import Flask, request
import json
from flask_restful import Resource, Api
from firebase import delete_user, get_all_users,create_account,updateUserDetails

app = Flask(__name__)
api = Api(app)

class UserAuth(Resource):
    def get(self):
        data = get_all_users()
        print(data)
        return data
        

    def delete(self):
        uid = request.args.get('uid')
        print(uid)
        data = delete_user(uid)
        return data
    
    def post(self):
        email = request.form.get("email")
        password = request.form.get('password')
        print(email)
        print(password)
        result = create_account(email,password)
        return str(result)

class UpdateUser(Resource):
    def post(self):
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

# class Object:
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)