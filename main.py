from app.animation import Animation
from app.board import Board
from app.display import draw_board_grid
from app.user_input import get_continue_action_key, get_restart_action_key, get_quit_action_key
from app.user_input import request_game_action, request_board_size

__author__ = 'kyleaclark'


def run_text_game():
    board = _create_board_interactively()
    draw_board_grid(board)

    while True:
        user_action_key = request_game_action()

        if user_action_key == get_continue_action_key():
            board.update_board_cells()
            draw_board_grid(board)
        elif user_action_key == get_restart_action_key():
            print('\n')
            board = _create_board_interactively()
            draw_board_grid(board)
        elif user_action_key == get_quit_action_key():
            break


def run_animated_simulation(save_gif: bool = False, save_mp4: bool = False):
    board = Board(num_rows=50, num_cols=50)
    animation = Animation(board)
    animation.animate_board_grid(save_gif, save_mp4)


def _create_board_interactively() -> Board:
    board_rows, board_columns = request_board_size()
    result = Board(board_rows, board_columns)

    return result


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        game_input = sys.argv[1]
        run_text_game()
    else:
        save_gif = False
        save_mp4 = False
        run_animated_simulation(save_gif, save_mp4)
