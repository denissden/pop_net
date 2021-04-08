from dataclasses import *
import datetime

@dataclass()
class Event:
    type_: str
    value: None


@dataclass()
class Message:
    from_: str
    value: str
    date: datetime.datetime
    type_: str = "Message"

