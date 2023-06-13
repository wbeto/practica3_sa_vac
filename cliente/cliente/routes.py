from flask import request, jsonify, Blueprint
from urllib import response
from dotenv import load_dotenv
import requests
# import boto3
# import uuid
import threading
import time
import datetime
import os
import random

load_dotenv()



user = Blueprint('user', __name__, url_prefix='')


@user.route('/cliente/solicitar_p', methods=['POST'])
def solicitar_p():
    pedido = request.form.get('pedido')
    direccion = request.form.get('direccion')
    if pedido:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        form_data = {
            'texto': timestamp + ' - cliente/solicitar_p: ' + pedido + '|' + direccion
        }
        response_log = requests.post('http://localhost:8000/ESB/save', data=form_data)
        
        response = requests.post('http://localhost:8000/ESB/recibirPedidoC', data=request.form)
        print(response.status_code)
        if response.status_code != 200:
            response = jsonify({'message': 'Pedido enviado pero restaurante no activo', 'status': 200})
            response.status_code = 200
            return response
        else:
            response = jsonify({'message': 'Pedido enviado y recibido por restaurente', 'status': 200})
            response.status_code = 200
            return response
    else:
        response = jsonify({'message': 'No se proporcionó un pedido', 'status': 400})
        response.status_code = 400
        return response

@user.route('/cliente/verificarOrdenRes', methods=['POST'])
def verificar():
    codigo = request.form.get('codigo')
    if codigo:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
       
        response = requests.post('http://localhost:8000/ESB/estadoPedidoRestaurante', data=request.form)
        json = response.json()
        #elemento = response.json().message
        form_data = {
            'texto': timestamp + ' - cliente/verificarOrdenRes: ' + 'Codigo: ' + codigo + ' - ' + json.get('message') 
        }
        response_log = requests.post('http://localhost:8000/ESB/save', data=form_data)
        
        response = jsonify({'message': json.get('message') , 'status': 200})
        response.status_code = 200
        return response

    else:
        response = jsonify({'message': 'Porfavor ingrese codigo', 'status': 400})
        response.status_code = 400
        return response

@user.route('/cliente/verificarOrdenRep', methods=['POST'])
def verificarRep():
    codigo = request.form.get('codigo')
    if codigo:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        response = requests.post('http://localhost:8000/ESB/estadoPedidoRepartidor', data=request.form)
        json = response.json()
        elemento = json.get('message')
        form_data = {
            'texto': timestamp + ' - cliente/verificarOrdenRep: ' + 'Codigo: ' + codigo + ' - ' + elemento 
        }
        response_log = requests.post('http://localhost:8000/ESB/save', data=form_data)
        
        response = jsonify({'message': elemento, 'status': 200})
        response.status_code = 200
        return response

    else:
        response = jsonify({'message': 'Porfavor ingrese codigo', 'status': 400})
        response.status_code = 400
        return response
