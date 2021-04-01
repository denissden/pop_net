from flask import *
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
    return current_user.login
