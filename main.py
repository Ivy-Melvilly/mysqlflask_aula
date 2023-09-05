from flask import Flask, render_template, request, redirect, url_for
from turma import Turma
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db = pymysql.connect(
            host="albalopes.tech", 
            user="psi2023_alba", 
            password="u0ZNtc8AMbiMIr[m", 
            db="psi2023_alba", 
            charset="utf8mb4", 
            cursorclass=pymysql.cursors.DictCursor)
        
        cmd = db.cursor()
        cmd.execute("SELECT * FROM turma")
        recordset = cmd.fetchall()
        print(recordset)
        lista = []
        for r in recordset:
            lista.append(Turma(r['id'], r['turma'], r['cargahoraria']))

        return render_template('index.html', lista=lista)
        #for r in recordset:
        #    print(r['turma'])

    finally:
        db.close()
    
    return 'Conexão realizada com sucesso'
  
if __name__ == '__main__':
    app.run(debug=True)