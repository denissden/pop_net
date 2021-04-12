from flask import *
from flask_login import login_required, current_user
from engine.event_handler import wait_event, get_engine
import jsonpickle
from apps.functions import search_login

main = Blueprint('main', __name__)


@main.route("/home")
@login_required
def home():
    return current_user.login


@main.route("/test")
def test():
    from apps.functions import get_last_id
    get_last_id()
    return "test"


@main.route("/get_status")
@login_required
def get_status():
    id_ = str(current_user.user_id)
    status = wait_event(id_)
    return jsonpickle.dumps([i.to_dict() for i in status] if status is not None else None, unpicklable=False)


@main.route("/get_id")
@login_required
def get_me():
    return str(current_user.user_id)

