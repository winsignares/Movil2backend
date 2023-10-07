from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.cliente import Cliente, ruta_clientes
from api.reserva import Reserva, ruta_reservas
#from api.aerolinea import Aerolinea, ruta_aerolinea
#from api.aeropuerto import Aeropuerto, ruta_aeropuertos
#from api.avion import Avion, ruta_avion
#from api.ciudad import Ciudad, ruta_ciudades

app.register_blueprint(ruta_clientes,url_prefix = '/api')
app.register_blueprint(ruta_reservas, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

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

if __name__ == "__main__":
    app.run(debug=True, port=5500, host='0.0.0.0')