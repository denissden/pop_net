from apps.functions import *
from engine import queue
from engine import event_handler
import engine.event_models as events
import json
import jsonpickle


def a():
    pass


from apps.functions import _get_dialogs

from database import db_session

db_session.global_init("database/data.sqlite/")  # init database

print(search_login("1").all())
