from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
import requests

BASE = "http://numberapi.com"
k = ""
response = requests.get(BASE + "/2/6?json")
data = response.json()
for info in data["text"]:
    k = k + info


app = Flask(__name__)
api = Api(app)

class Dates(Resource):
    def get(self):
        return {
            "id": 1,
            "month": 12,
            "day": 3,
            "fact": k,
                },




api.add_resource(Dates, "/dates")

if __name__ == "__main__":
    app.run(debug=True)

