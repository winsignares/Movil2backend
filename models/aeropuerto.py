from config.db import  db, ma, app

class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuerto"

    id = db.Column(db.Integer, primary_key = True)
    idciudad = db.Column(db.Integer, db.ForeignKey('tblciudad'))
    nombre = db.Column(db.String(50))
    no_vuelos_totales = db.Column(db.Integer(10))

    def __init__(self, idciudad, nombre, no_vuelos_totales):
        self.idciudad = idciudad
        self.nombre = nombre
        self.no_vuelos_totales = no_vuelos_totales

with app.app_context():
    db.create_all()

class AeropuertoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idciudad', 'nombre', 'no_vuelos_totales')
