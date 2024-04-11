from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import ConteudoTeste
from . import db #DB importado do arquivo init
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/conteudo')
@login_required
def conteudo():

    nivel_conteudo = current_user.nivel_usuario


    #conteudos = ConteudoTeste.query.all()
    conteudos = ConteudoTeste.query.filter_by(nivel_conteudo=nivel_conteudo).all()
    
    return render_template("conteudo.html", usuario=current_user, conteudos=conteudos)
    #return jsonify(conteudos)

@views.route('/nivelamento')
@login_required
def nivelamento():
    return render_template("nivelamento.html", usuario=current_user)

@views.route('/conteudo-post', methods=['POST'])
def conteudo_postagem():

    titulo = request.form.get('titulo')
    descricao = request.form.get('titulo')
    url = request.form.get('url')
    nivel_conteudo = request.form.get('nivel_conteudo')

    novo_conteudo = ConteudoTeste(titulo = titulo, descricao = descricao, url = url, nivel_conteudo = nivel_conteudo)
    db.session.add(novo_conteudo)
    db.session.commit()
    return 'Novo conteúdo postado!'
