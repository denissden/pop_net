from dataclasses import *
from time import time, sleep


__engine = None

EVENT_EXPIRE = 60


def global_init():
    global __engine

    if __engine:
        return

    __engine = EventHandler()


def get_engine():
    return __engine


def wait_event(name, interval=1, timeout=20):
    e = get_engine()
    print(e)
    e.wait_event(name)
    while timeout > 0:
        print("waiting event", name)
        print(e)
        timeout -= 1
        res = e.get_changes(name)
        print(res)
        if res:
            tmp = res.events.copy()
            res.clear()
            return tmp
        sleep(interval)


@dataclass(unsafe_hash=True)
class EventContainer:
    name: str = field(hash=True, compare=True)
    changed: bool = field(default=False, hash=False, compare=False)
    events: list = field(default_factory=list, hash=False, compare=False)
    expires_at: float = field(default=lambda: time() + EVENT_EXPIRE, hash=False, compare=False)

    def __post_init__(self):
        self.update_expiration()

    def update_expiration(self):
        self.expires_at = time() + EVENT_EXPIRE

    def clear(self):
        self.events.clear()


@dataclass()
class EventHandler:
    events: dict[str, EventContainer] = field(default_factory=dict)
    changes: set[EventContainer] = field(default_factory=set)

    def wait_event(self, name):
        if name not in self.events:
            self.events[name] = EventContainer(name)

    def add_event(self, name, event):
        if name in self.events:
            res = self.events[name]
            res.events.append(event)
            res.changed = True
            print("event change")

    def clean_events(self):
        remove = set()
        time_now = time()
        for name, event in self.events:
            if event.expires_at < time_now:
                remove.add(event)
        self.events -= remove

    def get_changes(self, name):
        if name in self.events:
            res = self.events[name]
            if res.changed:
                res.update_expiration()
                res.changed = False
                return res
