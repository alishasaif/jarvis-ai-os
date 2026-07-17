from collections import defaultdict
from typing import Callable

from backend.events.events import Event


class EventManager:

    def __init__(self):

        self._listeners = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        callback: Callable
    ):

        if callback not in self._listeners[event_name]:
            self._listeners[event_name].append(callback)

    def unsubscribe(
        self,
        event_name: str,
        callback: Callable
    ):

        if callback in self._listeners[event_name]:
            self._listeners[event_name].remove(callback)

    def publish(
        self,
        event: Event
    ):

        listeners = self._listeners.get(
            event.name,
            []
        )

        for callback in listeners:

            try:

                callback(event)

            except Exception as e:

                print(
                    f"[EVENT ERROR] {event.name}: {e}"
                )


event_manager = EventManager()