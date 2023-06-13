from flask import Flask, request, jsonify
import requests

import uuid
import threading
import time
import datetime
import random

app = Flask(__name__)
# CORS(app, resources={r"/": {"origins": ""}})


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, Bearer"
    return response



@app.route('/ESB/recibirPedidoC', methods=['POST'])
def pedido():
    _json = request.form
    pedido = _json['pedido']
    direccion = _json['direccion']

   
    
    response = requests.post(
            'http://localhost:4000/restaurante/recibir_p', 
            data = {
                'pedido': pedido,
                'direccion': direccion
            }
            )
    
    if response.status_code != 200:
        response = jsonify({'message': 'Se ha enviado el pedido, pero el restaurante aún no ha abierto', 'status': 200})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': 'Pedido recibido por el restaurente', 'status': 200})
        response.status_code = 200
        return response
    

@app.route('/ESB/save', methods=['POST'])
def guardar_info():
    _json = request.form
    texto = _json['texto']

    response_log = requests.post(
        'http://localhost:5000/logs/save',
         data={
             'texto': texto
             }
            )

    response = jsonify({'message': 'Texto guardado en el log correctamente.', 'status': 200})
    response.status_code = 200
    return response

@app.route('/ESB/estadoPedidoRepartidor', methods=['POST'])
def estado_pedido_repartidor():
    _json = request.form
    codigo = _json['codigo']

    respuesta_repartidor = requests.post(
        'http://localhost:6000/repartidor/estadoPedido', 
        data={
            'codigo': codigo
        }
        )

    response = respuesta_repartidor.status_code
    response = respuesta_repartidor.text
    return response


@app.route('/ESB/estadoPedidoRestaurante', methods=['POST'])
def estado_pedido_restaurante():
    _json = request.form
    codigo = _json['codigo']

    respuesta_restaurante = requests.post(
        'http://localhost:4000/restaurante/estadoPedido',
        data={
            'codigo': codigo
        }
        )
    
    response = respuesta_restaurante.status_code
    response = respuesta_restaurante.text
    return response

@app.route('/ESB/repatidorReciboPedido', methods=['POST'])
def repatidor_recibo_pedido():
    _json = request.form
    codigo = _json['codigo']

    response_log = requests.post(
        'http://localhost:6000/repartidor/estadoPedido', 
        data = {
            'codigo': codigo
        } 
        )
    
    response = response_log.status_code
    response = response_log.text
    return response

if __name__ == '__main__':
    app.run(debug=True,port=8000)