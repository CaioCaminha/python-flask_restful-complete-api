from flask import request, jsonify
from flask_restful import Resource
from models.user import UserModel

from flask_jwt_extended import create_access_token


class Security(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = UserModel.find_by_username(username)

        if username != user.username or password != user.password:
            return {"msg": "Bad username or password"}, 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

