from itertools import chain
from random import randint
from typing import List

from app.components.cell import Cell

__author__ = 'kyleaclark'


class Board2d:

    def __init__(self, num_rows: int, num_cols: int, pre_seeded_values: List[int] = None):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._grid = self._generate_grid(num_rows, num_cols)
        self._seed_grid_cells(pre_seeded_values)

    @property
    def grid_cells_flattened(self) -> List[Cell]:
        return list(chain.from_iterable(self._grid))

    @property
    def grid_cell_values(self) -> List[int]:
        return [cell.state for cell in self.grid_cells_flattened]

    def draw_board(self):
        print('')
        for row in self._grid:
            for col in row:
                print(col.get_text_character(), end='')

            print('')

        print('')

    def update_board_cells(self):
        alive_cells = []
        dead_cells = []

        for row in range(len(self._grid)):
            for col in range(len(self._grid[row])):
                living_neighbor_count = self._sum_living_neighbors(row, col)

                cell = self._get_cell(row, col)

                if cell.is_alive():
                    if living_neighbor_count < 2 or living_neighbor_count > 3:
                        dead_cells.append(cell)
                elif living_neighbor_count == 3:
                    alive_cells.append(cell)

        for cell in alive_cells:
            cell.set_alive()

        for cell in dead_cells:
            cell.set_dead()

        return alive_cells, dead_cells

    def _sum_living_neighbors(self, row_idx: int, col_idx: int) -> int:
        result = 0
        for neighbour_row in range(row_idx-1, row_idx+2):
            for neighbor_col in range(col_idx-1, col_idx+2):

                if neighbour_row == row_idx and neighbor_col == col_idx:
                    valid_neighbour = False
                elif neighbour_row < 0 or neighbour_row >= self._num_rows:
                    valid_neighbour = False
                elif neighbor_col < 0 or neighbor_col >= self._num_cols:
                    valid_neighbour = False
                else:
                    valid_neighbour = True

                if valid_neighbour and self._get_cell(neighbour_row, neighbor_col).is_alive():
                    result += 1

        return result

    def _get_cell(self, row_idx: int, col_idx) -> Cell:
        return self._grid[row_idx][col_idx]

    def _seed_grid_cells(self, pre_seeded_values: List[int] = None):
        for row_idx, cells in enumerate(self._grid):
            for col_idx, cell in enumerate(cells):
                try:
                    seed_idx = (row_idx * self._num_cols) + col_idx
                    seed_value = pre_seeded_values[seed_idx] if pre_seeded_values else randint(0, 2)
                except IndexError:
                    seed_value = randint(0, 2)  # 33% chance

                if seed_value == 1:
                    cell.set_alive()

    @staticmethod
    def _generate_grid(num_rows: int, num_cols: int) -> List[List[Cell]]:
        return [[Cell() for _ in range(num_cols)] for _ in range(num_rows)]
