from flask import request, jsonify, Blueprint
from urllib import response
from dotenv import load_dotenv
import requests
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
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    form_data = {
        'texto': timestamp + ' - repartidor -> Codigo:' + codigo + ' pedido entregado'
    }
    response_log = requests.post('http://localhost:8000/ESB/save', data=form_data)
    print("¡El temporizador ha terminado!")

@user.route('/repartidor/recibir_p', methods=['POST'])
def guardar_log():
    codigo = request.form.get('codigo')
    if codigo:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        form_data = {
            'texto': timestamp + ' - /repartidor/recibir_p: ' + codigo
        }
        response_log = requests.post('http://localhost:8000/ESB/save', data=form_data)
        
        t = threading.Thread(target=temporizador, args=(0.1,codigo,))
        t.start()
        response = jsonify({'message': 'Pedido recibido por repartidor', 'status': 200})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'No se proporcionó un pedido', 'status': 400})
        response.status_code = 400
        return response

@user.route('/repartidor/estadoPedido', methods=['POST'])
def estadoPedido():
    codigo = request.form.get('codigo')
    if codigo:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        lista = ['Orden en proceso', 'Orden entregada', 'Orden en proceso', 'Orden entregada', 'Orden en proceso']
        elemento = random.choice(lista)
        form_data = {
            'texto': timestamp + ' - /repartidor/estadoPedido: ' + 'Codigo: ' + codigo + ' - ' + elemento 
        }
        response_log = requests.post('http://localhost:8000/ESB/save', data=form_data)
        
        response = jsonify({'message': elemento, 'status': 200})
        response.status_code = 200
        return response