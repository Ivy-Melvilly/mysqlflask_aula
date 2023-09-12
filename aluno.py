from database import db

class Aluno(db.Model):
    __tablename__ = "aluno"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    matricula = db.Column(db.String(100))

    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula