from math import floor
from random import randint
from typing import List

from app.cell import Cell

__author__ = 'kyleaclark'


class Board1d:

    def __init__(self, num_rows: int, num_cols: int, pre_seeded_values: List[int] = None):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._row_indices = num_rows - 1
        self._col_indices = num_cols - 1
        self._grid = self._generate_grid(num_rows, num_cols)

        self._seed_grid_cells(pre_seeded_values)

    @property
    def grid_cell_values(self):
        return [cell.state for cell in self._grid]

    def update_board_cells(self):
        alive_cells = []
        dead_cells = []

        for idx, cell in enumerate(self._grid):
            alive_neighbors = self._sum_living_neighbors(idx)
            cell.alive_neighbors = alive_neighbors

            if cell.is_alive():
                if alive_neighbors < 2 or alive_neighbors > 3:
                    dead_cells.append(cell)
            elif alive_neighbors == 3:
                alive_cells.append(cell)

        for cell in alive_cells:
            cell.set_alive()

        for cell in dead_cells:
            cell.set_dead()

    def is_last_col(self, cell_idx: int) -> bool:
        row_idx = self._get_row_idx(cell_idx)

        return ((row_idx * self._num_rows) + self._col_indices) - cell_idx == 0

    def _sum_living_neighbors(self, cell_idx: int) -> int:
        cell_row_idx = self._get_row_idx(cell_idx)
        cell_col_idx = self._get_col_idx(cell_idx)

        result = 0
        for neighbour_row_idx in range(cell_row_idx-1, cell_row_idx+2):
            if self._is_invalid_row(neighbour_row_idx):
                continue

            for neighbor_col_idx in range(cell_col_idx-1, cell_col_idx+2):
                if self._is_invalid_col(cell_row_idx, cell_col_idx, neighbour_row_idx, neighbor_col_idx):
                    continue

                if self._get_cell(neighbour_row_idx, neighbor_col_idx).is_alive():
                    result += 1

        return result

    def _get_cell(self, row_idx: int, col_idx: int) -> Cell:
        cell_idx = (row_idx * self._num_cols) + col_idx

        return self._grid[cell_idx]

    def _get_row_idx(self, cell_idx: int):
        return floor(cell_idx / self._num_cols)

    def _get_col_idx(self, cell_idx: int):
        return cell_idx % self._num_cols

    def _is_invalid_row(self, neighbor_row_idx: int):
        return neighbor_row_idx < 0 or neighbor_row_idx >= self._num_rows

    def _is_invalid_col(self,
                        cell_row_idx: int,
                        cell_col_idx: int,
                        neighbor_row_idx: int,
                        neighbor_col_idx: int) -> bool:
        result = ((neighbor_col_idx < 0) or
                  (neighbor_col_idx >= self._num_cols) or
                  (cell_row_idx == neighbor_row_idx and cell_col_idx == neighbor_col_idx))

        return result

    def _seed_grid_cells(self, pre_seeded_values: List[int] = None):
        for idx, cell in enumerate(self._grid):
            try:
                seed_value = pre_seeded_values[idx] if pre_seeded_values else randint(0, 2)
            except IndexError:
                seed_value = randint(0, 2)  # 33% chance

            if seed_value == 1:
                cell.set_alive()

    @staticmethod
    def _generate_grid(num_rows: int, num_cols: int) -> List[Cell]:
        return [Cell() for _ in range(num_rows * num_cols)]
