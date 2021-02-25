from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api,Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.sqlite3"
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key =  True)
    email = db.Column(db.String, unique = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    state = db.Column(db.String, nullable = False)
    country = db.Column(db.String, nullable = False)
    pan = db.Column(db.String, unique = True, nullable = False)
    contactNo = db.Column(db.String, nullable = False)
    dob = db.Column(db.String, nullable = False)
    account_type = db.Column(db.String, nullable = False)

    def __init__(self, email, name, username, password, address, state, country, pan, contactNo, dob, account_type):
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.state = state
        self.country = country
        self.pan = pan
        self.contactNo = contactNo
        self.dob = dob
        self.account_type = account_type

class LoanModel(db.Model):
    id = db.Column(db.Integer, primary_key =  True)
    loan_type = db.Column(db.String, nullable = False)
    loan_amount = db.Column(db.Float, nullable = False)
    date = db.Column(db.String, nullable = False)
    rate_of_interest = db.Column(db.Float, nullable = False)
    duration = db.Column(db.Integer, nullable = False)
    user_foreign_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    userModel = db.relationship("UserModel", backref = "loanModel")

    def __init__(self, loan_type, loan_amount, date, rate_of_interest, duration,user_foreign_id):
        self.loan_amount = loan_amount
        self.loan_type = loan_type
        self.date = date
        self.rate_of_interest = rate_of_interest
        self.duration = duration
        self.user_foreign_id = user_foreign_id

class UserModelSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('email','name','username','password','address','state','country','pan','contactNo','dob','account_type')

class LoanModelSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('loan_type','loan_amount','date','rate_of_interest','duration','user_foreign_id')
        include_fk = True

db.create_all()
userModelSchema = UserModelSchema()
usersModelSchema = UserModelSchema(many = True)
loanModelSchema = LoanModelSchema()
loansModelSchema = LoanModelSchema(many = True)

def check_empty_value(new_user):
    if new_user.email == "" or new_user.name == "" or new_user.username == "" or new_user.password == "" or new_user.address == "" or new_user.state == "" or new_user.country == "" or new_user.pan == "" or new_user.contactNo == "" or new_user.dob == "" or new_user.account_type == "":
        raise ValueError

def check_empty_loan(new_loan):
    if new_loan.loan_type == "" or new_loan.loan_amount == "" or new_loan.date == "" or new_loan.rate_of_interest == "" or new_loan.duration == "" or new_loan.user_foreign_id == "":
        raise ValueError

class UserLogin(Resource):
    def get(self):
        current_username = request.json['username']
        current_password = request.json['password']
        called_user = UserModel.query.filter_by(username=current_username).first()
        print(called_user)
        if called_user == None:
            return "No Such User Found",404
        elif current_password == called_user.password:
            return f"Welcome {called_user.name}! Login Succesful"
        else:
            return "Invalid username or Password",400

class UserRegistration(Resource):
    
    def post(self):
        try:
            new_user = UserModel(email = request.json['email'], 
                name = request.json['name'], username = request.json['username'], password = request.json['password'], 
                address = request.json['address'], state = request.json['state'], country = request.json['country'], 
                pan = request.json['pan'], contactNo = request.json['contactNo'], dob = request.json['dob'], 
                account_type = request.json['account_type'])
            
            check_empty_value(new_user)

            db.session.add(new_user)
            db.session.commit()
            return f"Congratulations {request.json['name']}! Your Account was created",201
        
        except ValueError:
            return "Credentials cannot be an Empty String", 400
        except:
            return "Invalid Credentials Or Already Exists",400

class UserUpdate(Resource):
    
    def get(self, userId):
        called_user = UserModel.query.get(userId)
        if called_user == None:
            return "No Such User",404
        return userModelSchema.jsonify(called_user)

    def put(self, userId):
        called_user = UserModel.query.get(userId)
        if called_user == None:
            return "No Such User",404
        try:
            called_user.email = request.json['email']
            called_user.name = request.json['name']
            called_user.username = request.json['username']
            called_user.password = request.json['password']
            called_user.address = request.json['address']
            called_user.state = request.json['state']
            called_user.country = request.json['country']
            called_user.pan = request.json['pan']
            called_user.contactNo = request.json['contactNo']
            called_user.dob = request.json['dob']
            called_user.account_type = request.json['account_type']

            check_empty_value(called_user)

            db.session.commit()
            return userModelSchema.jsonify(called_user)
        except ValueError:
            return 'Credentials Should not be Empty'
        except:
            return 'Credentials invalid or already Exists'

class LoanList(Resource):
    
    def get(self, loanId):
        called_user = UserModel.query.filter_by(id=request.json['id']).first()
        if called_user is None:
            return "No Such user"
        called_loan = LoanModel.query.filter_by(id=loanId).first()
        if called_loan is None:
            return "No Such loan"
        if called_loan.user_foreign_id != request.json['id']:
            return f"Loan of ID:{loanId} doesn't exist on User ID:{request.json['id']}'s account"
        else:
            return loanModelSchema.jsonify(called_loan)
        
class LoanInit(Resource):

    def post(self):
        current_user = UserModel.query.filter_by(id=request.json['user_foreign_id']).first()
        if current_user is None:
            return "No User Under That ID", 404
        try:
            current_loan = LoanModel(loan_type = request.json['loan_type'], loan_amount = request.json['loan_amount'], 
                date = request.json['date'], rate_of_interest = request.json['rate_of_interest'], 
                duration = request.json['duration'], user_foreign_id = request.json['user_foreign_id'])
            
            check_empty_loan(current_loan)
            db.session.add(current_loan)
            db.session.commit()

            return loanModelSchema.jsonify(current_loan)
        except ValueError:
            return "Values Should not be Blank or Empty", 400
        except:
            return "Invalid Data", 400


api.add_resource(UserRegistration,'/users/register')
api.add_resource(UserLogin,'/users/login')
api.add_resource(UserUpdate, '/users/<userId>')
api.add_resource(LoanList,'/loans/<loanId>')
api.add_resource(LoanInit,'/loans')