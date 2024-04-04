from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/conteudo')
@login_required
def conteudo():
    return render_template("conteudo.html", usuario=current_user)

@views.route('/nivelamento')
@login_required
def nivelamento():
    return render_template("nivelamento.html", usuario=current_user)