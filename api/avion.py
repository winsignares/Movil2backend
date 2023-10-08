from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.avion import Avion, AvionSchema

ruta_avion = Blueprint("ruta_avion", __name__)

avion_schema = AvionSchema()
aviones_schema = AvionSchema()

@ruta_avion.route('/aviones', methods=['GET'])
def avion():
    resultall = Avion.query.all()
    resultado_avion = aviones_schema.dump(resultall)
    return jsonify(resultado_avion)

@ruta_avion.route('/saveaviones', methods=['POST'])
def save():
    nombre = request.json['nombre']
    new_avion = Avion(nombre)
    db.session.add(new_avion)
    db.session.commit()
    return "Datos guardados con exito"

@ruta_avion.route('/updateaviones', methods=['PUT'])
def update():
    id = request.json['id']
    nombre = request.json['nombre']
    avion = Avion.query.get(id)
    if avion:
        print(avion)
        ciudad.nombre = nombre
        db.session.commit()
        return "Datos actualizados con exito"
    else:
        return "Error"
    
@ruta_avion.route('/deleteaviones/<id>', methods=['GET'])
def eliminar(id):
    avion = Avion.query.get(id)
    db.session.delete(avion)
    db.session.commit()
    return jsonify(avion_schema.dump(cliente))