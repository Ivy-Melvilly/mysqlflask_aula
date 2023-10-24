from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from aluno import Aluno
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
        return 'Usuário não localizado'

@lm.user_loader
def load_user(id):
    aluno = Aluno.query.fiter_by(id=id).first()
    return aluno

