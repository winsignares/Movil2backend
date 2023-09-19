from flask import Flask
from config.db import  db, ma, app
from api.cliente import ruta_clientes

app.register_blueprint(ruta_clientes,url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')