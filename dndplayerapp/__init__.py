#!/usr/bin/ python
# -*- coding: utf-8 -*-
from models import *
from forms import *
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, request
from flask.ext.login import LoginManager, login_required, login_user, \
    logout_user, current_user
from config import get_config
from db import get_session
from datetime import datetime

# Main Application and Config
app = Flask(__name__)
app.config.from_object(get_config())
session = get_session()

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def index():
    if current_user.is_anonymous():
        return redirect(url_for("login"))
    else:
        user = current_user
        return render_template('main.html', 
            user=user, 
            characters=user.characters, 
            last_played=user.updated_at.strftime("%a, %b %d %Y"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.form)
        if form.validate():
            # .one() is not safe when user isn't present
            user = session.query(User).filter_by(username=form.data['username']).first()
            if user:
                pass_check = user.valid_password(form.data['password'])
                if pass_check:
                    login_user(user)
                    # Update last login
                    user.updated_at = datetime.now()
                    session.commit()
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
    races = session.query(Race).all()
    return render_template('races.html', races=races)

@app.route("/spells/")
@app.route("/spells/<id>")
def spells(id=None):
    if id:
        spells = [get_or_404(Spell, id)]
    else:
        spells = session.query(Spell).all()
    return render_template('spells.html', spells=spells)

@app.route("/characters/")
@app.route("/characters/<id>")
@login_required
def characters(id=None):
    if id:
        user = current_user
        character = get_or_404(Character, id)
        if character.user == user:
            return render_template('character.html', character=character)
        else:
            return 403
    else:
        characters = session.query(Spell).all()
        return render_template('characters.html', characters=characters)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    error = None
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.form)
        if form.validate():
            try:
                user = User(**form.data)
                session.add(user)
                session.commit()
                flash("It Worked!")
                redirect(url_for("index"))
            except:
                session.rollback()
                flash("It Failed! :(")
        else:
            error = form.errors
    return render_template('signup.html', form=form, error=error)

@login_manager.user_loader
def load_user(userid):
    u = get_or_404(User, userid)
    return u if u else None

def get_or_404(model, ident):
    rv = session.query(model).get(ident)
    if rv is None:
        abort(404)
    return rv


if __name__ == '__main__':
    pass