__author__ = 'kyleaclark'


class Cell:

    def __init__(self):
        self._state = 0
        self.alive_neighbors = 0

    @property
    def state(self) -> int:
        return self._state

    def set_dead(self):
        self._state = 0

    def set_alive(self):
        self._state = 1

    def is_alive(self) -> bool:
        return self._state == 1

    def set_live_neighbor_count(self, neighbors: int):
        self._live_neighbor_count = neighbors

    def get_text_character(self) -> str:
        return ' 1 ' if self.is_alive() else ' . '
