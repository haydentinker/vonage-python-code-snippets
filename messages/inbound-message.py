#!/usr/bin/env python3
from pprint import pprint
from flask import Flask, request

app = Flask(__name__)


@app.route("/webhooks/inbound-message", methods=["POST"])
def inbound_message():
    data = request.get_json()
    print(data)
    return "200"


if __name__ == "__main__":
    app.run(host="www.example.org", port=3000)
