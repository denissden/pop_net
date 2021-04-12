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

    def to_dict(self):
        return {
            "id_from": self.from_,
            "text": self.text,
            "date": self.date,
            "id": self.id_,
            "type": "Message"
        }
