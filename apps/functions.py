import re
from database.models import User, Message, Post
from database.db_session import create_session
from sqlalchemy import or_, and_, literal

email_pattern = \
    re.compile(
        r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")


def check_email(email):
    return email_pattern.match(email)


def get_last_id():
    s = create_session()
    query = s.query(User).order_by(User.user_id.desc()).first()
    if query is not None:
        return query.user_id
    return 0


def id_exists(user_id):
    return 0 < user_id <= get_last_id()


def _get_messages(from_, to, last_id=18446744073709552, limit=20):
    s = create_session()
    messages = s.query(Message).filter(and_(
        or_(
            and_(Message.id_from == from_, Message.id_to == to),
            and_(Message.id_from == to, Message.id_to == from_)),
        Message.message_id < last_id)) \
        .order_by(Message.message_id.desc()).limit(limit)

    return messages


def _get_posts(author_id, last_id=18446744073709552, limit=10):
    s = create_session()
    posts = s.query(Post).filter(and_(
        Post.author_id == author_id,
        Post.post_id < last_id)) \
        .order_by(Message.message_id.desc()).limit(limit)

    return posts


def _get_dialogs(id_to, last_id=18446744073709552, limit=1000):
    s = create_session()
    messages = s.query(Message.id_to).distinct().filter(or_(Message.id_to == id_to, Message.id_from == id_to))
    list_users = [i[0] for i in messages]
    list_users.sort()
    return s.query(User).filter(User.user_id.in_(list_users))


def search_login(pattern):
    s = create_session()
    users = s.query(User).filter(User.login.like(pattern + "%"))
    return users