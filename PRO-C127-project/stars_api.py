from flask import Flask,json,jsonify,request
from data import data

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "data":data,
        "message":"success"
    }),200


@app.route("/star")
def stars():
    name = request.args.get("Name")
    stars_data = next(item for item in data if item["Name"] == name)
    return jsonify({
    "stars_data":stars_data,
    "message":"success"
    }),200

app.run()