from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db2.sqlite3"

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Users(db.Model):
    username = db.Column(db.String, primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

class UsersScehma(ma.SQLAlchemySchema):
    class Meta:
        model = Users
        load_instance = True
    
    username = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

db.create_all()
user_schema = UsersScehma()
user = Users(username = 'JohnDoe97', email = 'john_d@email.com', password = '********')
db.session.add(user)
db.session.commit()
user_schema.dump(user)