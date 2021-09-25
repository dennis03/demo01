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
    text2 = ''
    for c1 in text:
        if c1.isalnum():
            text2 += c1.upper()
    outText = ''
    n2 = len(text2)//n + 1
    for i in range(len(text2)):
        n3 = n2*(i%n) + (i-(i%n))//n
        outText += text2[n3]
    return outText




