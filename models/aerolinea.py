from config.db import  db, ma, app

class Aerolinea(db.Model):
    __tablename__ = "tblaerolinea"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    no_vuelos = db.Column(db.Integer(5))
    sede = db.Column(db.String(50))

    def __init__(self, nombre, no_vuelos, sede):
        self.nombre = nombre
        self.no_vuelos = no_vuelos
        self.sede = sede

with app.app_context():
    db.create_all()

class AerolineaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'no_vuelos', 'sede')