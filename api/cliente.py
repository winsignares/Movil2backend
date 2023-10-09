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

@ruta_clientes.route('/savecliente', methods=['POST'])
def save():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    telefono = request.json['telefono']
    new_cliente = Cliente(nombre, apellido, email, telefono)
    db.session.add(new_cliente)
    db.session.commit()    
    return "Datos guardados con éxito"

@ruta_clientes.route('/updatecliente', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    telefono = request.json['telefono']
    cliente = Cliente.query.get(id)   
    if cliente :
        print(cliente) 
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.email = email
        cliente.telefono = telefono
        db.session.commit()
        return "Datos actualizados con éxitos"
    else:
        return "Error"

@ruta_clientes.route('/deletecliente/<id>', methods=['GET'])
def eliminar(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify(cliente_schema.dump(cliente))