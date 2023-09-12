from flask import Flask, render_template, request, redirect, url_for
from turma import Turma
import pymysql
from database import db
from flask_migrate import Migrate
from nota import Nota
from turma import Turma
from aluno import Aluno

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hsdaey7q6eihmsn9816}]'
conexao = 'mysql+pymysql://psi2023_alba:u0ZNtc8AMbiMIr[m@albalopes.tech/psi2023_alba'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Conexão realizada com sucesso'

@app.route('/add') 
def add():
    obj = Nota(0, 100)
    db.session.add(obj)
    db.session.commit()
    return 'Dados inseridos com sucesso' 

if __name__ == '__main__':
    app.run(debug=True)