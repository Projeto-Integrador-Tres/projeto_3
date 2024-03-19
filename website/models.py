from . import db 
from flask_login import UserMixin

#User Mixin permite o uso de imports da lib flask_login!

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    