#!/usr/bin/ python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, \
    current_user
from Config import *
from models import *
from forms import *

# Main Application and Config
app = Flask(__name__)
app.config.from_object('Config.DevelopmentConfig')
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    if current_user.is_anonymous():
        return redirect(url_for("login"))
    else:
        return render_template('main.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.form)
        if form.validate():
            # login and validate the user...
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for("index"))
        else:
            error = form.errors
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)

@app.route('/races')
def races():
    races = db.session.query(Race).all()
    return render_template('races.html', races=races)


if __name__ == '__main__':
    app.run()