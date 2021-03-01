from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow.validate import Range, Length
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shoppinglist.sqlite3"
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class ShoppingModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String, unique = True, nullable = False)
    item_quantity = db.Column(db.Integer, nullable = False)

    def __init__(self, item_name, item_quantity):
        self.item_name = item_name
        self.item_quantity = item_quantity

class ShoppingSchema(ma.SQLAlchemySchema):
    item_name = fields.Str(required = True, validate = Length(min=3))
    item_quantity = fields.Integer(required = True, validate = Range(min=1))

    class Meta:
        fields = ("item_name","item_quantity")

db.create_all()
shoppingSchema = ShoppingSchema()
shoppingSchemas = ShoppingSchema(many = True)

class Create(Resource):
    def get(self):
        all_items = ShoppingModel.query.all()
        return shoppingSchemas.jsonify(all_items)

    def post(self):
        errors = shoppingSchema.validate(request.json)
        if errors:
            abort(400, str(errors))
        this_item = ShoppingModel.query.filter_by(item_name = request.json['item_name']).first()
        if this_item is not None:
            abort(400, f"{this_item.item_name} Already Exists")
        new_list_item = ShoppingModel(item_name = request.json['item_name'], item_quantity = request.json['item_quantity'])
        db.session.add(new_list_item)
        db.session.commit()
        return f"{new_list_item.item_quantity} {new_list_item.item_name} was Added To Your List"

class EditItems(Resource):
    def delete(self,list_item_name):
        this_item = ShoppingModel.query.filter_by(item_name=list_item_name).first()
        if this_item is None:
            abort(404, f"{list_item_name} Was not Found")
        db.session.delete(this_item)
        db.session.commit()
        return f"{list_item_name} Was Deleted"

    def put(self, list_item_name):
        this_item = ShoppingModel.query.filter_by(item_name = list_item_name).first()
        if this_item is None:
            abort(404, f"{list_item_name} Does Not Exists")
        errors = shoppingSchema.validate(request.json)
        if errors:
            abort(400, str(errors))
        this_item.item_name = request.json['item_name']
        this_item.item_quantity = request.json['item_quantity']
        db.session.commit()

        return f"{list_item_name} has been updated to {this_item.item_quantity} items"
        

api.add_resource(Create, '/list')
api.add_resource(EditItems, '/list/<list_item_name>')