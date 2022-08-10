from random import randint
from typing import Union

__author__ = 'kyleaclark'


class Cell:

    def __init__(self):
        self._state = 0
        self.alive_neighbors = 0

    @property
    def state(self) -> int:
        return self._state

    def set_initial_state(self, seed_value: Union[int, bool] = None):
        max_randint = 2
        initial_state = int(bool(seed_value)) * max_randint if seed_value is not None else randint(0, max_randint)

        if initial_state == max_randint:
            self.set_alive()
        else:
            self.set_dead()

    def set_dead(self):
        self._state = 0

    def set_alive(self):
        self._state = 1

    def is_alive(self) -> bool:
        return self._state == 1
