from flask import *
from database import db_session
from apps.pop_net import models, functions

pop_net = Blueprint('pop_net', __name__, template_folder="apps/auth/templates")


@pop_net.route('/register')
def register():
    return render_template("register.html")


@pop_net.route("/register", methods=['POST'])
def register_post():
    email = request.form.get('email')
    first_name = request.form.get('first')
    last_name = request.form.get('last')
    login = request.form.get('login')
    password = request.form.get('password')

    if not functions.check_email(email):
        return "incorrect email"

    if len(password) < 6:
        return "password is too short"

    print(email, first_name, last_name, login, password)
    return "success"
