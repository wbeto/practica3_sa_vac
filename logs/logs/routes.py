from flask import request, jsonify, Blueprint
from urllib import response
from dotenv import load_dotenv
# import boto3
# import uuid

import os

load_dotenv()



user = Blueprint('user', __name__, url_prefix='')


@user.route('/logs/save', methods=['POST'])
def guardar_log():
    texto = request.form.get('texto')
    if texto:
        with open('log.txt', 'a') as archivo_log:
            archivo_log.write(texto + '\n')
        return 'Texto guardado en el log correctamente.'
    else:
        return 'No se proporcionó ningún texto.'