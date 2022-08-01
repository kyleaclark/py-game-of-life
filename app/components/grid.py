from math import floor
from random import randint
from typing import List

from app.components.cell import Cell

__author__ = 'kyleaclark'


class Grid:

    def __init__(self, num_rows: int, num_cols: int):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._row_indices = num_rows - 1
        self._col_indices = num_cols - 1
        self._grid = self._generate_grid(num_rows, num_cols)

    @property
    def cells(self):
        return self._grid

    def seed_grid_cells(self, pre_seeded_values: List[int] = None):
        for idx, cell in enumerate(self._grid):
            try:
                seed_value = pre_seeded_values[idx] if pre_seeded_values else randint(0, 2)
            except IndexError:
                seed_value = randint(0, 2)  # 33% chance

            if seed_value == 1:
                cell.set_alive()

    def sum_living_neighbors(self, cell_idx: int) -> int:
        row_idx = self._get_row_idx(cell_idx)
        col_idx = self._get_col_idx(cell_idx)

        result = 0
        for neighbour_row in range(row_idx-1, row_idx+2):
            if neighbour_row < 0 or neighbour_row >= self._num_rows:
                continue

            for neighbor_col in range(col_idx-1, col_idx+2):
                if (
                    neighbor_col < 0 or
                    neighbor_col >= self._num_cols or
                    (neighbour_row == row_idx and neighbor_col == col_idx)
                ):
                    continue

                if self._get_cell(neighbour_row, neighbor_col).is_alive():
                    result += 1

        return result

    def is_last_row(self, col_idx: int) -> bool:
        return col_idx % self._row_indices == 0

    def is_last_col(self, cell_idx: int) -> bool:
        row_idx = self._get_row_idx(cell_idx)

        return ((row_idx * self._num_rows) + self._col_indices) - cell_idx == 0

    def _get_cell(self, row_idx: int, col_idx: int) -> Cell:
        cell_idx = (row_idx * self._num_cols) + col_idx

        return self._grid[cell_idx]

    def _get_row_idx(self, cell_idx: int):
        return floor(cell_idx / self._num_cols)

    def _get_col_idx(self, cell_idx: int):
        return cell_idx % self._num_cols

    @staticmethod
    def _generate_grid(num_rows: int, num_cols: int) -> List[Cell]:
        return [Cell() for _ in range(num_rows * num_cols)]
