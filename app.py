from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.reserva import Reserva, ruta_reservas
from api.vuelo import Vuelo, ruta_vuelos
from api.ciudad import Ciudad, ruta_ciudades
from api.aeropuerto import Aeropuerto, ruta_aeropuertos
from api.aerolinea import Aerolinea, ruta_aerolineas
from api.avion import Avion, ruta_aviones
from api.escala import Escala, ruta_escalas
from api.escala_reserva import Escala_reserva, ruta_escala_reservas
from api.aero import Aero, ruta_aeros

app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_ciudades, url_prefix = '/api')
app.register_blueprint(ruta_aeropuertos, url_prefix = '/api')
app.register_blueprint(ruta_aerolineas, url_prefix = '/api')
app.register_blueprint(ruta_aeros, url_prefix = '/api')
app.register_blueprint(ruta_aviones, url_prefix = '/api')
app.register_blueprint(ruta_vuelos, url_prefix = '/api')
app.register_blueprint(ruta_escalas, url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')
app.register_blueprint(ruta_escala_reservas, url_prefix = '/api')

# CONSULTA 01
@app.route('/dostablas', methods=['GET'])
def dostabla():
    datos = {}
    resultado = db.session.query(Cliente, Reserva). \
        select_from(Cliente).join(Reserva).all()
    i=0
    for clientes, reservas in resultado:
        i+=1
        datos[i]={
            'cliente':clientes.nombre,
            'reserva': reservas.id
        }
    return datos

# CONSULTA 02
@app.route('/consultaaereo', methods=['GET'])
def consultaaereo():
    datos = {}
    resultado = db.session.query( Ciudad,Aeropuerto). \
        select_from(Ciudad).join(Aeropuerto).all()
    i=0
    for ciudades, aeropuertos in resultado:
        i+=1
        datos[i]={
            'ciudad':ciudades.nombre,
            'departamento':ciudades.departamento,
            'aerepuerto': aeropuertos.nombre,
            'direccion': aeropuertos.dirección
        }
    return datos

#Consulta 03

@app.route('/consultaraereolinea', methods=['GET'])
def consultaraereolinea():
    datos = {}
    resultado = db.session.query( Aeropuerto, Aerolinea, Aero ). \
        select_from(Aeropuerto).join(Aero).all()
    
    i=0
    for aeropuertos, aerolineas, aeros in resultado:
        i+=1
        datos[i]={
            'nombre_aeropuerto':aeropuertos.nombre,
            'direccion_aeropuerto': aeropuertos.direccion,
            'aerolinea': aerolineas.nombre
        }
    return datos
 
#Consulta 04

@app.route('/consultaravion', methods=['GET'])
def consultaravion():
    datos = {}
    resultado = db.session.query( Ciudad, Aeropuerto, Aerolinea, Aero, Avion, Vuelo). \
        select_from(Aeropuerto).join(Vuelo).all()
    
    i=0
    for ciudades, aeropuertos, aerolineas, aeros, aviones, vuelos in resultado:
        i+=1
        datos[i]={
            'nombre_ciudad': ciudades.nombre,
            'nombre_aeropuerto': aeropuertos.nombre,
            'nombre_aerolinea':aerolineas.nombre,
            'modelo_avion': aviones.modelo,
            'matricula_avion': aviones.matricula,
            'vuelo': vuelos.nombre
            
        }
    return datos


@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')