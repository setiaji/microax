from flask import Flask

app = Flask(__name__)

from app import views

app.secret_key = 'you-will-never-guess'

