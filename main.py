from flask import Flask, render_template, request, flash, redirect, url_for
import pymysql
from database import db, lm
from flask_migrate import Migrate
from models.nota import Nota
from models.turma import Turma
from models.aluno import Aluno
from controllers.aluno import bp_alunos

app = Flask(__name__)
app.register_blueprint(bp_alunos, url_prefix='/alunos')

app.config['SECRET_KEY'] = 'hsdaey7q6eihmsn9816}]'
conexao = 'mysql+pymysql://psi2023_alba:u0ZNtc8AMbiMIr[m@albalopes.tech/psi2023_alba'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
lm.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return redirect(url_for('alunos.login'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add', methods=['GET', 'POST']) 
def add():
    if request.method == 'GET':
        return render_template('nota_add.html')
    else:
        valor = request.form.get('valor')
        obj = Nota(0, valor)
        db.session.add(obj)
        db.session.commit()
        flash('Dados inseridos com sucesso')
        return redirect(url_for('add'))

@app.route('/get')
def get():
    notas = Nota.query.all()
    return render_template('nota_get.html', notas=notas)

if __name__ == '__main__':
    app.run(debug=True)