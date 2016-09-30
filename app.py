# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
import views



