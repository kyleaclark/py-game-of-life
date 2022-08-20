__author__ = 'kyleaclark'


def request_board_size() -> tuple[int, int]:
    min_length = 3
    max_length = 10

    rows_input = input(f'Input a number of rows between {min_length} to {max_length}: ')
    columns_input = input(f'Input a number of rows between {min_length} to {max_length}: ')

    board_rows = _bound_number(int(rows_input), min_length, max_length)
    board_columns = _bound_number(int(columns_input), min_length, max_length)
    result = board_rows, board_columns

    return result


def request_game_action() -> str:
    print('Press enter to continue, r to restart, or q to quit:')
    return input('')


def get_continue_action_key() -> str:
    return ''


def get_restart_action_key() -> str:
    return 'r'


def get_quit_action_key() -> str:
    return 'q'


def _bound_number(number: int, min_num: int, max_num: int) -> int:
    return max(min_num, min(number, max_num))
