from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ciudad import Ciudad, CiudadSchema

ruta_ciudades = Blueprint("ruta_ciudad", __name__)

ciudad_schema = CiudadSchema()
ciudades_schema = CiudadSchema(many=True)

@ruta_ciudades.route('/ciudades', methods=['GET'])
def ciudad():
    resultall = Ciudad.query.all() #Select * from Ciudades
    resultado_ciudad = ciudades_schema.dump(resultall)
    return jsonify(resultado_ciudad)

@ruta_ciudades.route('/saveciudad', methods=['POST'])
def save():
    nombre = request.json['nombre']
    new_ciudad = Ciudad(nombre)
    db.session.add(new_ciudad)
    db.session.commit()
    return "Datos guardados con exito"

@ruta_ciudades.route('/updateciudad', methods=['PUT'])
def update():
    id = request.json['id']
    nombre = request.json['nombre']
    ciudad = Ciudad.query.get(id)
    if ciudad:
        print(ciudad)
        ciudad.nombre = nombre
        db.session.commit()
        return "Datos actualizados con exito"
    else:
        return "error"
    
@ruta_ciudades.route('/deleteciudad/<id>', methods=['GET'])
def eliminar(id):
    ciudad = Ciudad.query.get(id)
    db.session.delete(ciudad)
    db.session.commit()
    return jsonify(cliente_schema.dump(cliente))