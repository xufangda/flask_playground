from . import web 
from flask import Blueprint

web = Blueprint('web',__name__)

@web.route('/')
def login():
    pass