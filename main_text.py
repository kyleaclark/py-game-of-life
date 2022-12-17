from app.board import Board
from app.text_display import print_board_grid
from app.user_input import request_game_action, request_board_size


def run_text_game():
    board = _create_board_interactively()
    print_board_grid(board)

    while True:
        user_action_key = request_game_action()

        if user_action_key == '':
            board.update_board_cells()
            print_board_grid(board)
        elif user_action_key == 'r':
            print('\n')
            board = _create_board_interactively()
            print_board_grid(board)
        elif user_action_key == 'q':
            break


def _create_board_interactively() -> Board:
    board_rows, board_columns = request_board_size()
    result = Board(board_rows, board_columns)

    return result


if __name__ == '__main__':
    run_text_game()
