from database import db

class Turma(db.Model):
    __tablename__ = "turma"
    id = db.Column(db.Integer, primary_key = True)
    turma = db.Column(db.String(100))
    cargahoraria = db.Column(db.Integer)
    
    def __init__(self, id, turma, cargahoraria):
        self.id = id
        self.turma = turma
        self.cargahoraria = cargahoraria