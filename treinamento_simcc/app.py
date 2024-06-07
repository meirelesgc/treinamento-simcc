from flask import Flask, jsonify
from rest.rest_pesquisador import rest_pesquisador

app = Flask(__name__)

app.register_blueprint(rest_pesquisador)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"Hellow World": "🪄"})


if __name__ == "__main__":
    app.run()
