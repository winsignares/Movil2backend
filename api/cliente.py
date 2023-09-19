from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.cliente import Cliente, ClientesSchema

ruta_clientes = Blueprint("ruta_cliente", __name__)

cliente_schema = ClientesSchema()
clientes_schema = ClientesSchema(many=True)

@ruta_clientes.route('/clientes', methods=['GET'])
def cliente():
    resultall = Cliente.query.all() #Select * from Clientes
    resultado_cliente= clientes_schema.dump(resultall)
    return jsonify(resultado_cliente)
