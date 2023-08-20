from typing import Any


class Queue:
    def __init__(self) -> None:
        self._queue = []

    def pop(self, val=None):
        if val is None:
            return self._queue.pop(0)

        index = self._queue.index(val)
        return self._queue.pop(index)

    def remove(self, val):
        self._queue.remove(val)

    def push(self, val: Any) -> None:
        self._queue.append(val)

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def is_in_q(self, val) -> bool:
        return val in self._queue

    def get_queue(self):
        return self._queue

    def __str__(self) -> str:
        return str(self._queue)