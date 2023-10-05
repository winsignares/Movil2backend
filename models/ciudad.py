from config.db import  db, ma, app

class Ciudad(db.Model):
    __tablename__= "tblciudad"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    cant_aeropuertos = db.Column(db.Integer(5))

    def __init__(self, nombre, cant_aeropuertos):
        self.nombre = nombre
        self.cant_aeropuertos = cant_aeropuertos

with app.app_context():
    db.create_all()

class CiudadSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'cant_aeropuertos')