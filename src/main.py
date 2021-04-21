"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorites
#from models import Person
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import datetime

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/login', methods=["POST"])
#se debe enviar la data como objeto
def login():
    username = request.json["email"]
    password = request.json["password"]
    if not username:
        return jsonify({"error": "user or password not foundd"}), 410
    if not password:
        return jsonify({"error": "user or password not found"}), 410
    user = User.query.filter_by(email=username).first()
    if not user:
        return jsonify({"error": "user or password not found"}), 410
    elif user.password != password:
        return jsonify({"error": "user or password not found"}), 410
    else:
        tiempodeVida= datetime.timedelta(days=1)
        tokenDeUsuario = create_access_token(identity=username, expires_delta=tiempodeVida) 
        requestToken= {
            "user": user.serialize(),
            "token":tokenDeUsuario
        }
        return jsonify(requestToken), 200

@app.route('/user', methods=['POST']) 
#se debe enviar la data como objeto
def add_user():
    data = request.get_json()
    validacion = User.query.filter_by(email=data["email"]).first()
    if validacion is None:
        user1 = User(email=data["email"],password=data["password"],is_active=True)
        db.session.add(user1)
        db.session.commit()
        return jsonify("Message : Se adiciono un usuario!"),200
    else:
        return jsonify({"error": "El usuario ya existe"}),420

@app.route('/planets', methods=['GET'])
def getPlanets():
    planeta = Planets.query.all()
    request = list(map(lambda planeta:planeta.serialize(),planeta))    
    return jsonify(request), 200

@app.route('/planets/<int:position>', methods=['GET'])
def listPlanetsid(position):
    planeta = Planets.query.filter_by(id=position).first()
    request = planeta.serialize()
    return jsonify(request), 200

@app.route('/characters', methods=['GET'])
def getCharacters():
    personaje = Characters.query.all()
    request = list(map(lambda person:person.serialize(),personaje))    
    return jsonify(request), 200

@app.route('/characters/<int:position>', methods=['GET'])
def listCharactersid(position):
    character = Characters.query.filter_by(id=position).first()
    request = character.serialize()
    return jsonify(request), 200

@app.route('/favorites/<int:user>', methods=['GET'])
def getFavorites(user):
    favorito = Favorites.query.filter_by(user_id=user).all()
    request = list(map(lambda todo:todo.serialize(),favorito)) 
    return jsonify(request), 200

@app.route('/favorites/<int:id>', methods=['DELETE'])
def delFavorites(id):
    favorito = Favorites.query.get(id)
    db.session.delete(favorito)
    db.session.commit()
    return jsonify("Message : favorito eliminado"), 200

@app.route('/favorites', methods=['POST'])
#se debe enviar la data como objeto
def add_newFavorite():
    data = request.get_json()
    favorito = Favorites(name=data["name"],user_id=data["user id"])
    db.session.add(favorito)
    db.session.commit()
    return jsonify("Message : favorito agregado"), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
