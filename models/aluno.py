from database import db
from flask_login import UserMixin

class Aluno(db.Model, UserMixin):
    __tablename__ = "aluno"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    matricula = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome, matricula, senha):
        self.nome = nome
        self.matricula = matricula
        self.senha = senha