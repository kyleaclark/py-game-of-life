from app.board import Board
from app.cell import Cell

__author__ = 'kyleaclark'


def draw_board_grid(board: Board):
    print('')  # return line

    for row_idx, row in enumerate(board._grid):
        for cell_idx, cell in enumerate(row):
            character = ' 1 ' if cell.is_alive() else ' . '
            print(character, end='')

        print('')  # return line

    print('')  # return line
