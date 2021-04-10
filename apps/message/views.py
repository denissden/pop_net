from flask import *
from flask_login import login_required, current_user
from apps.functions import id_exists, _get_messages
from database.db_session import create_session
from database.models import *
from engine.event_handler import get_engine
import engine.event_models as events
import jsonpickle

message__ = Blueprint('message', __name__)


@message__.route("/message")
@login_required
def message():
    receiver_id = int(request.args.get("to"))
    return render_template("message.html")


@message__.route("/message", methods=["POST"])
@login_required
def message_post():
    receiver_id = int(request.args.get("to"))
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
                                                 datetime.datetime.now(),
                                                 new_message.message_id))

    return "success"


@message__.route("/get_messages")
@login_required
def get_messages():
    receiver_id = int(request.args.get("to"))
    from_id = int(request.args.get("less"))
    m = _get_messages(current_user.user_id, receiver_id, from_id)
    for mm in m:
        print(mm.id_from, mm.id_to, mm.text, mm.date, mm.message_id)
    return jsonpickle.dumps(list(map(Message.to_dict, m)), unpicklable=False)
