from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ciudad import Ciudad, CiudadSchema

ruta_ciudades = Blueprint("ruta_ciudad", __name__)

ciudad_schema = CiudadSchema()
ciudades_schema = CiudadSchema(many=True)

@ruta_ciudades.route('/ciudades', methods=['GET'])
def ciudad():
    resultall = Ciudad.query.all()#Select * from Ciudades
    resultado_ciudad = ciudades_schema.dump(resultall)
    return jsonify(resultado_ciudad)