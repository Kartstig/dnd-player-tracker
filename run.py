#!/usr/bin/ python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, \
    logout_user, current_user
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
            # .one() is not safe when user isn't present
            user = db.session.query(User).filter_by(username=form.data['username']).first()
            if user:
                pass_check = user.valid_password(form.data['password'])
                if pass_check:
                    login_user(user)
                    flash("Logged in successfully.")
                    return redirect(url_for("index"))
                else:
                    flash("Invalid Password")
            else:
                flash("Invalid Username")
        else:
            error = form.errors
    return render_template("login.html", form=form, error=error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("index"))

@app.route('/races')
def races():
    flash("Logged in successfully.")
    races = db.session.query(Race).all()
    return render_template('races.html', races=races)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    error = None
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.form)
        if form.validate():
            flash("It Worked!")
        else:
            error = form.errors
    return render_template('signup.html', form=form, error=error)

@login_manager.user_loader
def load_user(userid):
    u = db.session.query(User).filter_by(id=userid).one()
    return u if u else None


if __name__ == '__main__':
    app.run()
