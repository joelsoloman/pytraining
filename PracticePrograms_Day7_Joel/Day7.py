from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

groceries = [
    {
        'name' : 'carrot',
        'quantity': 5
    },
    {
        'name' : 'onion',
        'quantity': 7
    }
]

class MyClass(Resource):

    def get(self):
        return groceries
    
    def post(self):
        newDict = {}
        newDict['name'] = request.json['name']
        newDict['quantity'] = request.json['quantity']
        groceries.append(newDict)
        return request.json

class ParamClass(Resource):
    
    def get(self, item):
        
        for index in groceries:
            if item == index['name']:
                return index
        else:
            abort(404, message=f"{item} Not Found")
    
    def delete(self, item):

        for index,listItem in enumerate(groceries):
            if item == listItem["name"]:
                groceries.pop(index)
                return item + " Deleted"
        else:
            abort(404, message=f"{item} Not Found")
    
    def put(self, item):

        for index, listItem in enumerate(groceries):
            if item == listItem['name']:
                listItem['quantity'] = request.json['quantity']
                return item + ' Updated'
        else:
            abort(404, message=f"{item} Not Found")   

api.add_resource(MyClass,'/groceries')
api.add_resource(ParamClass,'/groceries/<item>')