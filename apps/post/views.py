import jsonpickle
from flask import *
from flask_login import login_required, current_user
from apps.functions import _get_posts
from database.db_session import create_session
from database.models import *
from engine.event_handler import get_engine
import engine.event_models as events

post = Blueprint('post', __name__)


@post.route("/post")
@login_required
def posts():
    pass


@post.route("/post", methods=["POST"])
@login_required
def new_post():
    text_ = request.values.get("text")

    if len(text_) > 5000:
        return "text too long"

    s = create_session()

    new_post_ = Post(author_id=current_user.user_id,
                     text=text_,
                     date=datetime.datetime.now())

    s.add(new_post_)
    s.commit()

    return "success"


@post.route("/get_posts")
@login_required
def get_posts():
    author_id = int(request.args.get("author"))
    less_than_id = request.args.get("less")
    if less_than_id is not None:
        posts_ = _get_posts(author_id, int(less_than_id))
    else:
        posts_ = _get_posts(author_id)

    return jsonpickle.dumps(posts_)
