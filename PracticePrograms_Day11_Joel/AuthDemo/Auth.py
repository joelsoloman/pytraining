from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from marshmallow import fields
from marshmallow.validate import Range, Length
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SECRET_KEY'] = "MYKEY"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserSchema(ma.SQLAlchemySchema):
    username = fields.Str(required=True, validate=Length(min=3, max=12))
    password = fields.Str(required=True, validate=Length(min=3, max=12))

    class Meta:
        fields = ("username", "password")

db.create_all()
userSchema = UserSchema()
usersSchema = UserSchema(many = True)

def token_check(f):
    @wraps(f)

    def wrapper(*args, **kwargs):
        token = None
        
        if 'Bearer' in request.headers:
            token = request.headers['Bearer']
        if not token:
            return "Invalid Token"

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms = "HS256")
            current_user = User.query.filter_by(id = data['public_id']).first()
            print(data)
            print(current_user)
        except:
            return "Invalid Token"
        return f(current_user, *args, *kwargs)
    
    return wrapper

class Register(Resource):

    def post(self):
        errors = userSchema.validate(request.json)
        if errors:
            abort(400, str(errors))
        this_item = User.query.filter_by(username = request.json['username']).first()
        if this_item is not None:
            abort(400, f"{this_item.username} Already Exists")
        this_user = User(request.json['username'],generate_password_hash(request.json['password'], method='sha256'))
        db.session.add(this_user)
        db.session.commit()
        return f"{this_user.username} was Created"

class Login(Resource):

    def post(self):
        auth = request.authorization

        this_user = User.query.filter_by(username = auth.username).first()
        print(this_user)
        if this_user is None:
            return "No Such User"
        print(this_user.password, auth.password)
        if check_password_hash(this_user.password, auth.password):
            token = jwt.encode({'public_id':this_user.id, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return token
        
        return "Not Verified", 401

@token_check
def get_current_user_id(current_user):
    this_user = User.query.filter_by(username = current_user.username).first()
    return this_user

class View(Resource):
    def get(self):
        this_user = get_current_user_id()
        return userSchema.jsonify(this_user)

api.add_resource(Register,"/user/register")
api.add_resource(Login,"/user/login")
api.add_resource(View,"/user/view")