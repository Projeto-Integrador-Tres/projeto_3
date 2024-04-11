from . import db 
from flask_login import UserMixin
from dataclasses import dataclass

#User Mixin permite o uso de imports da lib flask_login!

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(255))
    nivel_usuario = db.Column(db.String(1))

@dataclass
class ConteudoTeste(db.Model):
    id:int = db.Column(db.Integer, primary_key = True)
    titulo: str = db.Column(db.String(150))
    descricao: str = db.Column(db.String(1000))
    url: str = db.Column(db.String(500))
    nivel_conteudo: str = db.Column(db.String(1))

    