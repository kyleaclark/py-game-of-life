from app.components.board1d import Board1d
from app.components.board2d import Board2d
from app.components.display import animate_board_grid, draw_board_grid
from app.components.user_input import get_simulate_action_key, get_restart_action_key, get_quit_action_key
from app.components.user_input import request_game_action, request_board_size

__author__ = 'kyleaclark'


def run_interactive_game_loop():
    board = _create_1d_board()
    draw_board_grid(board)

    while True:
        user_action_key = request_game_action()

        if user_action_key == get_simulate_action_key():
            board.update_board_cells()
            draw_board_grid(board)
        elif user_action_key == get_restart_action_key():
            print('\n')
            board = _create_1d_board()
            draw_board_grid(board)
        elif user_action_key == get_quit_action_key():
            break


def run_simulation_game_loop():
    board = _create_2d_board()
    animate_board_grid(board)


def _create_1d_board() -> Board1d:
    board_rows, board_columns = request_board_size()
    result = Board1d(board_rows, board_columns)

    return result


def _create_2d_board() -> Board2d:
    board_rows, board_columns = 50, 50 # TODO: read command line arg vars
    result = Board2d(board_rows, board_columns)

    return result
