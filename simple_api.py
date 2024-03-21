from flask import Flask
from flask_restful import Resource, Api
import json
from bson.json_util import dumps, loads
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)


class GetProducts(Resource):
  def get(self):       
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.Products
        collection = db.products_data
        results = dumps(collection.find())
        print(results)
        return json.loads(results)
api.add_resource(GetProducts, '/getProducts')

class GetTitles(Resource):
        def get(self):
                return {'id': '1221'}
api.add_resource(GetTitles, '/')

class insertProduct(Resource):
        def get(self):
                return {'id': '1221'}
api.add_resource(insertProduct, '/insertProduct')




if __name__ == '__main__':
        app.run(debug=True)
