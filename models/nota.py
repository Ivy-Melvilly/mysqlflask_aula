from database import db

class Nota(db.Model):
    __tablename__ = "nota"
    id = db.Column(db.Integer, primary_key = True)
    valor = db.Column(db.Float)

    def __init__(self, id, valor):
        self.id = id
        self.valor = valor