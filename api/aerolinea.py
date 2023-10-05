from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aerolinea import Aerolinea, AerolineaSchema

ruta_aerolinea = Blueprint("ruta_aerolinea", __name__)

aerolinea_schema = AerolineaSchema()
aerolineas_schema = AerolineaSchema(many=True)

@ruta_aerolinea.route('/aerolineas', methods=['GET'])
def aerolinea():
    resultall = Aerolinea.query.all()#Select * from Aerolineas
    resultado_aerolinea = aerolineas_schema.dump(resultall)
    return jsonify(resultado_aerolinea)