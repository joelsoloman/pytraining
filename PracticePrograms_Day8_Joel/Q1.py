from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Users(db.Model):
    
    username = db.Column(db.String, primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    
    def __repr__(self):
        return f"User : {self.username} | Email : {self.email}"