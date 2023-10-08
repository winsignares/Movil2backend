from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aeropuerto import Aeropuerto, AeropuertoSchema

ruta_aeropuertos = Blueprint("ruta_aeropuerto", __name__)

aeropuesto_schema = AeropuertoSchema()
aeropuestos_schema = AeropuertoSchema()

@ruta_aeropuestos.route('/aeropuerto', methods=['GET'])
def aeropuerto():
    resultall = Aeropuerto.query.all()
    resultado_aeropuerto = aeropuestos_schema(resultall)
    return jsonify(resultado_aeropuerto)

@ruta_aeropuestos.route('/saveaeropuerto', methods=['POST'])
def save():
    nombre = request.json['nombre']
    new_aeropuerto = Aeropuerto(nombre)
    db.session.add(new_aeropuerto)
    db.session.commit()
    return "Datos guardados con exito"

