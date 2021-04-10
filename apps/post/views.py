from flask import *
from flask_login import login_required, current_user
from apps.functions import id_exists
from database.db_session import create_session
from database.models import *
from engine.event_handler import get_engine
import engine.event_models as events

post = Blueprint('post', __name__)


@post.route("/posts")
def posts():
    pass


@post.route("/post", methods=["POST"])
@login_required
def new_post():
    text_ = request.values.get("text")

    receiver_id = int(request.args.get("to"))
    message_ = request.values.get("message")

    if len(text_) > 5000:
        return "text too long"

    s = create_session()

    new_message = Post(id_from=current_user.user_id,
                       text=message_)

    s.add(new_message)
    s.commit()

    e = get_engine()
    e.add_event(str(receiver_id), events.Message(current_user.user_id,
                                                 message_,
                                                 datetime.datetime.now(),
                                                 new_message.message_id))

    return "success"
