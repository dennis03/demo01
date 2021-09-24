import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evalEncryption():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = []
    for inputCase in data:
        result.append(encrypt(inputCase['n'], inputCase['text']))
    logging.info("My result :{}".format(result))
    return jsonify(result)

def encrypt(n, text):
    outText = ''
    n2 = len(text)//n + 1
    for i in range(len(text)):
        n3 = n2*(i%n) + (i-(i%n))//n
        outText += text[n3]
    return outText




