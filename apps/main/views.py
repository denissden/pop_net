from flask import *
from flask_login import login_required, current_user
from apps.functions import id_exists
from database.db_session import create_session
from database.models import *
from engine.event_handler import wait_event, get_engine
import jsonpickle
import engine.event_models as events

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


@main.route("/message")
@login_required
def message():
    # receiver_id = int(request.args.get("to"))
    return render_template("message.html")


@main.route("/message", methods=["POST"])
@login_required
def message_post():
    receiver_id = int(request.values.get("to"))
    message_ = request.values.get("message")

    if len(message_) > 256:
        return "message too long"

    if not id_exists(receiver_id):
        return "user does not exist"

    s = create_session()

    new_message = Message(id_from=current_user.user_id,
                          id_to=receiver_id,
                          text=message_)

    s.add(new_message)
    s.commit()

    e = get_engine()
    e.add_event(str(receiver_id), events.Message(current_user.user_id,
                                               message_,
                                               datetime.datetime.now()))

    return "success"


@main.route("/get_status")
@login_required
def get_status():
    id_ = str(current_user.user_id)
    status = wait_event(id_)
    print("status", status)
    return jsonpickle.dumps(status, unpicklable=False)
