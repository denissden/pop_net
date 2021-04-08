import datetime
import enum
# from sqlalchemy import *
from sqlalchemy import *
from flask_login import UserMixin
from database.db_session import SqlAlchemyBase


# meta = MetaData()
#
# users = Table(name="users", meta=meta,
#               Column())


class User(UserMixin, SqlAlchemyBase):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(16), index=True, unique=True)
    email = Column(String, index=True, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    created_date = Column(DateTime, default=datetime.datetime.now)

    def get_id(self):
        return self.user_id


class Friend(SqlAlchemyBase):
    __tablename__ = 'friend'

    friend_id = Column(Integer, primary_key=True, autoincrement=True)
    id_from = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    id_to = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    date = Column(DateTime, nullable=False)


class FriendStatusEnum(enum.Enum):
    pending = 0
    accepted = 1
    rejected = 2


class FriendRequest(SqlAlchemyBase):
    __tablename__ = 'friend_request'

    request_id = Column(Integer, primary_key=True, autoincrement=True)
    id_from = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    id_to = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    date = Column(DateTime, nullable=False)
    status = Column(Enum(FriendStatusEnum), nullable=False)


class PostStatusEnum(enum.Enum):
    posted = 0
    deleted = 1


class Post(SqlAlchemyBase):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    date = Column(DateTime, nullable=False)
    text = Column(UnicodeText, nullable=False)
    likes = Column(Integer)
    views = Column(Integer)
    status = Column(Enum(PostStatusEnum), nullable=False)


class CommentStatusEnum(enum.Enum):
    posted = 0
    deleted = 1


class Comment(SqlAlchemyBase):
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("post.post_id"), nullable=False, index=True)
    author_id = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    date = Column(DateTime, nullable=False)
    text = Column(Unicode(256), nullable=False)
    likes = Column(Integer)
    status = Column(Enum(CommentStatusEnum), nullable=False)


class MessageStatusEnum(enum.Enum):
    sent = 0
    received = 1
    read = 2
    deleted = 3


class Message(SqlAlchemyBase):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    id_from = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    id_to = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now())
    text = Column(Unicode(256), nullable=False)
    status = Column(Enum(MessageStatusEnum), nullable=False, default="sent")


class Photo(SqlAlchemyBase):
    __tablename__ = 'photo'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("user.user_id"), nullable=False, index=True)
    date = Column(DateTime, nullable=False)
    status = Column(Enum(CommentStatusEnum), nullable=False)
