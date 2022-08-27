from urllib import response
from flask import Flask, jsonify, request
from Similiraty import similiraty
from Tags import Tagsfunction
import json
from checkTags import checkTags
from flask_cors import CORS

app = Flask(__name__)
response = ''
CORS(app)


@app.route('/tags', methods=['POST', 'GET'])
def index_post():
    global response
    if(request.method == 'POST'):
        response
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data["furniture_context"]
        print("Printing name:")
        print(name)
        resposta = Tagsfunction(name)
        print("Sending response:")
        print(resposta)
        tagsToSend = checkTags(resposta)
        tagsToSendV2 = list(dict.fromkeys(tagsToSend))
        print("Tags to send:")
        print(tagsToSendV2)
        return jsonify({'tags': tagsToSendV2})
    else:
        print(response)
        return jsonify({'tags': response})


@app.route('/similar', methods=['POST', 'GET'])
def similar():
    global response
    if(request.method == 'POST'):
        response
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data["tag"]
        print("Tag sent:" + name)
        response = similiraty(name)
        print(response)
        return jsonify({'similar': response})
    else:
        print(response)
        return jsonify({'similar': response})


if __name__ == "__main__":
    app.run(debug=True)
