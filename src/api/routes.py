"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/register', methods=['POST'])
def create_new_user():
    body = request.get_json()

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if "email" not in body:
        raise APIException('You need to specify the email', status_code=400)
    if "password" not in body:
        raise APIException('You need to specify the password', status_code=400)
    if "is_active" not in body:
        raise APIException('You need to specify the is_active', status_code=400)
    
    hashed_password = bcrypt.generate_password_hash(body["password"])

    new_user = User(email=body['email'], password=hashed_password, is_active=body['is_active'])
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201

@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200


