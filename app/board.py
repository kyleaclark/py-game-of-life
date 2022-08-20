from itertools import chain

from app.cell import Cell

__author__ = 'kyleaclark'


class Board:

    def __init__(self, num_rows: int, num_cols: int, pre_seeded_values: list[list[int]] = None):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._grid = self._generate_grid(num_rows, num_cols)
        self._seed_grid_cells(pre_seeded_values)
        self._update_alive_neighbors()

    @property
    def grid_cells_flattened(self) -> list[Cell]:
        return list(chain.from_iterable(self._grid))

    @property
    def grid_cell_values(self) -> list[list[int]]:
        return [[cell.state for cell in row] for row in self._grid]

    @property
    def grid_cell_values_flattened(self) -> list[int]:
        return list(chain.from_iterable(self.grid_cell_values))

    def update_board_cells(self):
        self._update_cell_states()
        self._update_alive_neighbors()

    def _update_cell_states(self):
        alive_cells = []
        dead_cells = []

        for row in range(len(self._grid)):
            for col in range(len(self._grid[row])):
                cell = self._get_cell(row, col)

                alive_neighbors = self._sum_alive_neighbors(row, col)

                if cell.is_alive():
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        dead_cells.append(cell)
                elif alive_neighbors == 3:
                    alive_cells.append(cell)

        for cell in alive_cells:
            cell.set_alive()

        for cell in dead_cells:
            cell.set_dead()

    def _sum_alive_neighbors(self, cell_row_idx: int, cell_col_idx: int) -> int:
        result = 0
        for neighbour_row_idx in range(cell_row_idx - 1, cell_row_idx + 2):
            if self._is_invalid_row(neighbour_row_idx):
                continue

            for neighbor_col_idx in range(cell_col_idx - 1, cell_col_idx + 2):
                if self._is_invalid_col(cell_row_idx, cell_col_idx, neighbour_row_idx, neighbor_col_idx):
                    continue

                if self._get_cell(neighbour_row_idx, neighbor_col_idx).is_alive():
                    result += 1

        return result

    def _update_alive_neighbors(self):
        for row in range(len(self._grid)):
            for col in range(len(self._grid[row])):
                cell = self._get_cell(row, col)
                cell.alive_neighbors = self._sum_alive_neighbors(row, col)

    def _get_cell(self, row_idx: int, col_idx) -> Cell:
        return self._grid[row_idx][col_idx]

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

    def _seed_grid_cells(self, pre_seeded_values: list[list[int]] = None):
        for row_idx, cells in enumerate(self._grid):
            for col_idx, cell in enumerate(cells):
                try:
                    seed_value = pre_seeded_values[row_idx][col_idx] if pre_seeded_values else None
                except IndexError:
                    seed_value = None

                cell.set_initial_state(seed_value)

    @staticmethod
    def _generate_grid(num_rows: int, num_cols: int) -> list[list[Cell]]:
        return [[Cell() for _ in range(num_cols)] for _ in range(num_rows)]
