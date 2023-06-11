from flask import Flask
from flask_cors import CORS


import os
from dotenv import load_dotenv
# import pymysql

#importaciones de S3
# from botocore.exceptions import ClientError
# import boto3
# import logging


app = Flask(__name__)
CORS(app)
#Configuracion de base de datos
load_dotenv()
# app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
# app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
# app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
# app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')



load_dotenv()


#Conexion a base de datos
# def obtener_conexion():
#     return pymysql.connect(host=os.getenv('MYSQL_HOST'),
#                                 user=os.getenv('MYSQL_USER'),
#                                 password=os.getenv('MYSQL_PASSWORD'),
#                                 db=os.getenv('MYSQL_DB')
#                                 )

#Subir archivos a S3
# def upload_file(file_name, bucket, mimetype):
#     object_name = file_name
#     s3_client = boto3.client('s3')

#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name, 
#             ExtraArgs={'ContentType': mimetype})
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True

# def delete_file(file_name, bucket):
#     s3_client = boto3.client('s3')

#     try:
#         response = s3_client.delete_object(Bucket=bucket, Key=file_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True