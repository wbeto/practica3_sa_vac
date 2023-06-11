from flask import request, jsonify, Blueprint
from urllib import response
from dotenv import load_dotenv
import requests
# import boto3
import uuid
import threading
import time
import datetime
import random

import os

load_dotenv()



user = Blueprint('user', __name__, url_prefix='')

def temporizador(tiempo_en_minutos,codigo):
    tiempo_en_segundos = tiempo_en_minutos * 60
    time.sleep(tiempo_en_segundos)
    form_data = {
        'codigo': codigo
    }
    response_log = requests.post('http://localhost:6000/repartidor/recibir_p', data=form_data)
    print("¡El temporizador ha terminado!")


@user.route('/restaurante/recibir_p', methods=['POST'])
def guardar_log():
    pedido = request.form.get('pedido')
    direccion = request.form.get('direccion')
    if pedido:
        codigo = str(uuid.uuid4())
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        form_data = {
            'texto': timestamp + ' - Restaurante/recibir_p: ' + pedido + '|' + direccion + '|' + ' Codigo generado: ' + codigo
        }

        response_log = requests.post('http://localhost:5000/logs/save', data=form_data)

        t = threading.Thread(target=temporizador, args=(0.1,codigo,))
        t.start()
        
        response = jsonify({'message': 'Pedido recibido', 'status': 200})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'No se encuentra un pedido que procesar', 'status': 400})
        response.status_code = 400
        return response

@user.route('/restaurante/estadoPedido', methods=['POST'])
def estadoPedido():
    codigo = request.form.get('codigo')
    if codigo:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        lista = ['Orden en proceso', 'Orden despachada', 'Orden en proceso', 'Orden despachada', 'Orden en proceso']
        elemento = random.choice(lista)
        form_data = {
            'texto': timestamp + ' - /restaurante/estadoPedido: ' + 'Codigo: ' + codigo + ' - ' + elemento 
        }
        response_log = requests.post('http://localhost:5000/logs/save', data=form_data)
        
        response = jsonify({'message': elemento, 'status': 200})
        response.status_code = 200
        response.elemento = elemento
        return response

    