from dataclasses import *
import datetime

@dataclass()
class Event:
    type_: str
    value: None


@dataclass()
class Message:
    from_: str
    text: str
    date: datetime.datetime
    id_: int
    type_: str = "Message"

