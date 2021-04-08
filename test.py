from apps.functions import *
from engine import queue
from engine import event_handler
import engine.event_models as events
import json
import jsonpickle


def a():
    pass


m = events.Message(12,
               12,
               "tring",
               "datetime.datetime.now()")

print(jsonpickle.encode(m, unpicklable=False))


print(not check_email(input()))