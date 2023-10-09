from config.db import  db, ma, app

class Cliente(db.Model):
    __tablename__ = "tblcliente"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telefono = db.Column(db.String(10))

    def __init__(self, nombre, apellido, email, telefono) :
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

with app.app_context():
    db.create_all()

class ClientesSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'apellido', 'email', 'telefono')
