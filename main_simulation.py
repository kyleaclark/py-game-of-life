import sys

from app.animation import animate_board_grid
from app.board import Board


def run_animated_simulation(num_rows: int = 50, num_cols: int = 50):
    game_input = sys.argv[1] if len(sys.argv) > 1 else ''
    save_gif = True if game_input == 'gif' else False
    save_mp4 = True if game_input == 'mp4' else False

    board = Board(num_rows, num_cols)
    animate_board_grid(board, save_gif, save_mp4)


if __name__ == '__main__':
    run_animated_simulation(40, 50)
