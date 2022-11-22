from flask import Flask

app: Flask = Flask(__name__)

from src.controllers import PessoaController
