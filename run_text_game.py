import sys

from app.animation import animate_board_grid
from app.board import Board
from app.text_display import print_board_grid
from app.user_input import get_continue_action_key, get_restart_action_key, get_quit_action_key
from app.user_input import request_game_action, request_board_size

__author__ = 'kyleaclark'


def init():
    if len(sys.argv) > 1:
        game_input = sys.argv[1]
        save_gif = True if game_input == 'gif' else False
        save_mp4 = True if game_input == 'mp4' else False
        text_game = True if not save_gif and not save_mp4 else False
    else:
        save_gif = False
        save_mp4 = False
        text_game = False

    if text_game:
        run_text_game()
    else:
        run_animated_simulation(save_gif, save_mp4)


def run_animated_simulation(save_gif: bool = False, save_mp4: bool = False):
    board = Board(num_rows=50, num_cols=50)
    animate_board_grid(board, save_gif, save_mp4)


def run_text_game():
    board = _create_board_interactively()
    print_board_grid(board)

    while True:
        user_action_key = request_game_action()

        if user_action_key == get_continue_action_key():
            board.update_board_cells()
            print_board_grid(board)
        elif user_action_key == get_restart_action_key():
            print('\n')
            board = _create_board_interactively()
            print_board_grid(board)
        elif user_action_key == get_quit_action_key():
            break


def _create_board_interactively() -> Board:
    board_rows, board_columns = request_board_size()
    result = Board(board_rows, board_columns)

    return result


if __name__ == '__main__':
    run_text_game()
