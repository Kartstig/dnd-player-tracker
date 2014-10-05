#!/usr/bin/ python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, \
    current_user
from Config import *
from models import *

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
    if request.form:
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    else:
        return render_template("login.html")

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