from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from . import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))

    user = User.query.filter_by(name="admin").first()

    if not user or not check_password_hash(user.password, password):
        flash("Incorrect password!")
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)
    return redirect("/")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")
