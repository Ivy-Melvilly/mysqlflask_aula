from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from models.aluno import Aluno
from database import db, lm

bp_alunos = Blueprint("alunos", __name__, template_folder='templates')

@bp_alunos.route('/login')
def login():
    return render_template('login.html')

@bp_alunos.route('/autenticar', methods=['POST'])
def autenticar():
    matricula = request.form.get('matricula')
    senha = request.form.get('senha')
    aluno = Aluno.query.filter_by(matricula=matricula).first()
    if (aluno and aluno.senha == senha):
        return 'Bem-vindo {}!'.format(aluno.nome)
    else:
        flash('Dados incorretos', 'danger')
        return redirect('/')

@bp_alunos.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('alunos/alunos_cadastrar.html')
    else:
        nome = request.form.get("nome")
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")
        aluno = Aluno(nome, matricula, senha)
        db.session.add(aluno)
        db.session.commit()
        flash('Dados cadastrados com sucesso!', 'success')
        return redirect(url_for('alunos.listar'))

@bp_alunos.route('/listar', methods=['GET'])
def listar():
    alunos = Aluno.query.all()
    return render_template('alunos/alunos_listar.html', alunos=alunos)
        
@bp_alunos.route('/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
  aluno = Aluno.query.get(id)
  if request.method == 'GET':
    return render_template('alunos/alunos_excluir.html', aluno = aluno)
  
  if request.method == 'POST':
    db.session.delete(aluno)
    db.session.commit()
    flash('Usuário excluído com sucesso', 'success')
    return redirect(url_for('alunos.listar'))
    
@bp_alunos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aluno = Aluno.query.get(id)
    if request.method == 'GET':
        return render_template('alunos/alunos_editar.html', aluno=aluno)
    else:
        aluno.nome = request.form.get("nome")
        aluno.matricula = request.form.get("matricula")
        db.session.add(aluno)
        db.session.commit()
        flash('Dados atualizados com sucesso!', 'success')
        return redirect(url_for('alunos.listar'))

@lm.user_loader
def load_user(id):
    aluno = Aluno.query.fiter_by(id=id).first()
    return aluno

