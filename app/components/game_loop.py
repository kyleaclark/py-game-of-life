from app.components.board import Board
from app.components.user_input import get_simulate_action_key, get_restart_action_key, get_quit_action_key
from app.components.user_input import request_game_action, request_board_size

__author__ = 'kyleaclark'


def run_game_loop():
    board = _create_game_board()
    board.draw_board()

    while True:
        user_action_key = request_game_action()

        if user_action_key == get_simulate_action_key():
            board.update_board_cells()
            board.draw_board()
        elif user_action_key == get_restart_action_key():
            print('\n')
            board = _create_game_board()
            board.draw_board()
        elif user_action_key == get_quit_action_key():
            break


def _create_game_board() -> Board:
    board_rows, board_columns = request_board_size()
    result = Board(board_rows, board_columns)

    return result
