from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reserva import Reserva, ReservasSchema

ruta_reservas = Blueprint("ruta_reserva", __name__)

reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)

@ruta_reservas.route('/reservas', methods=['GET'])
def reserva():
    resultall = Reserva.query.all() #Select * from Clientes
    resultado_reserva= reservas_schema.dump(resultall)
    return jsonify(resultado_reserva)

@ruta_reservas.route('/savereservas', methods=['POST'])
def save():
    nombre = request.json['n_cliente']
    new_reserva = Reserva('n_cliente')
    db.session.add(new_reserva)
    db.session.commit()
    return "datos guardados con exito"

@ruta_reservas.route('/updatereservas', methods=['PUT'])
def update():
    id = request.json['id']
    nombre = request.json['n_cliente']
    reserva = Reserva.query.get(id)
    if reserva:
        print(reserva)
        reserva.nombre = nombre
        db.session.commit()
        return "datos actualizados con exito"
    else:
        return "Error"

@ruta_reservas.route('/deletereservas/<id>', methods=['GET'])
def eliminar(id):
    reserva = Reseva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify(reserva_schema.dump(reserva))