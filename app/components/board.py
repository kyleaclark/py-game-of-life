from typing import List

from app.components.grid import Grid

__author__ = 'kyleaclark'


class Board:

    def __init__(self, num_rows: int, num_cols: int, pre_seeded_values: List[int] = None):
        self._grid = Grid(num_rows, num_cols)
        self._grid.seed_grid_cells(pre_seeded_values)

    @property
    def grid_cells(self):
        return self._grid.cells

    @property
    def grid_cell_values(self):
        return [cell.state for cell in self.grid_cells]

    def draw_board(self):
        print('')
        for cell_idx, cell in enumerate(self.grid_cells):
            print(cell.get_text_character(), end='')

            if self._grid.is_last_col(cell_idx):
                print('')

        print('')

    def update_board_cells(self):
        alive_cells = []
        dead_cells = []

        for idx, cell in enumerate(self._grid.cells):
            living_neighbor_count = self._grid.sum_living_neighbors(idx)

            if cell.is_alive():
                if living_neighbor_count < 2 or living_neighbor_count > 3:
                    dead_cells.append(cell)
            elif living_neighbor_count == 3:
                alive_cells.append(cell)

        for cell in alive_cells:
            cell.set_alive()

        for cell in dead_cells:
            cell.set_dead()
