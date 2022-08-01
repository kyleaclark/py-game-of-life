__author__ = 'kyleaclark'


class Cell:

    def __init__(self):
        self._state = 0

    @property
    def state(self) -> int:
        return self._state

    def set_dead(self):
        self._state = 0

    def set_alive(self):
        self._state = 1

    def is_alive(self) -> bool:
        return self._state == 1

    def get_text_character(self) -> str:
        return ' 1 ' if self.is_alive() else ' . '
