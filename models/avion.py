from config.db import  db, ma, app

class Avion(db.Model):
    __tablename__ = "tblavion"

    id = db.Column(db.Integer, primary_key =True)
    idaerolinea = db.Column(db.Integer, db.ForeignKey('tblaerolinea'))
    modelo = db.Column(db.String(20))
    cap_pasajeros = db.Column(db.String(20))

    def __init__(self, idaerolinea, modelo, cap_pasajeros):
        self.idaerolinea = idaerolinea
        self.modelo = modelo
        self.cap_pasajeros = cap_pasajeros

with app.app_context():
    db.create_all()

class AvionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idaerolinea','modelo', 'cap_pasajeros')