from random import randint
from typing import Union


class Cell:

    def __init__(self):
        self.state = 0
        self.alive_neighbors = 0

    def set_initial_state(self, seed_value: Union[int, bool] = None):
        """Randomly set initial cell state or use given seed value"""

        max_randint = 2
        initial_state = int(bool(seed_value)) * max_randint \
            if seed_value is not None else randint(0, max_randint)

        if initial_state == max_randint:
            self.set_alive()
        else:
            self.set_dead()

    def set_dead(self):
        self.state = 0

    def set_alive(self):
        self.state = 1

    def is_alive(self) -> bool:
        return self.state == 1
