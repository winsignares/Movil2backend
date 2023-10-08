from config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    idcliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idavion = db.Column(db.Integer, db.ForeignKey('tblavion'))
    idciudad = db.Column(db.Integer, db.ForeignKey('tblciudad'))
    n_cliente = db.Column(db.String(50))

    def __init__(self, idavion, idcliente, idciudad, n_cliente) :
       self.idcliente = idcliente
       self.idavion = idavion
       self.idciudad = idciudad
       self.n_cliente = n_cliente

with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','idcliente', 'idavion','idciudad', 'n_cliente')
