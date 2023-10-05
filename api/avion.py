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