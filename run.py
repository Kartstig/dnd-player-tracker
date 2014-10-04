#!/usr/bin/ python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from Config import *
from models import *

# Main Application and Config
app = Flask(__name__)
app.config.from_object('Config.DevelopmentConfig')
db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/races')
def races():
	races = db.session.query(Race).all()
	return render_template('races.html', races=races)


if __name__ == '__main__':
    app.run()