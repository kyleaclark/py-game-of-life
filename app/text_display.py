from app.board import Board


def print_board_grid(board: Board):
    print()  # empty line

    for row_idx, row in enumerate(board.grid):
        for cell_idx, cell in enumerate(row):
            character = ' 1 ' if cell.is_alive() else ' . '
            print(character, end='')

        print('')  # empty line

    print('')  # empty line
