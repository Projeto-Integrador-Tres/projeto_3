from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #DB importado do arquivo init
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            if check_password_hash(usuario.senha, senha):
                login_user(usuario)
                print('Usuário logado')
                return redirect(url_for('views.nivelamento')) #Futuramente redirecionar para página de conteúdos 
            else: 
                print('Senha incorreta')
        else: 
            print('E-mail incorreto')

    return render_template("login.html", usuario = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/cadastro-usuario', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            print("Usuário já cadastrado!")
        else:
            novo_usuario = Usuario(nome=nome, email=email, senha=generate_password_hash(senha, method='scrypt'))
            db.session.add(novo_usuario)
            db.session.commit()
            #flash('Conta criada com sucesso!') #Futuramente usar flash para criar alertas no html
            return redirect(url_for('auth.login'))


    return render_template("cadastro_usuario.html")