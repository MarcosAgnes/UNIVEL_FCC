from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('listagem'))
    return render_template('cadastro.html')

@app.route('/listagem')
def listagem():
    usuarios = Usuario.query.all()
    return render_template('listagem.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)