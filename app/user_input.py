def request_board_size() -> tuple[int, int]:
    """Return row/col board size tuple given user input value for row and column length"""

    min_length = 3
    max_length = 10

    rows_input = input(f'Input a number of rows between {min_length} to {max_length}: ')
    columns_input = input(f'Input a number of rows between {min_length} to {max_length}: ')

    board_rows = _bound_number(int(rows_input), min_length, max_length)
    board_columns = _bound_number(int(columns_input), min_length, max_length)
    result = board_rows, board_columns

    return result


def request_game_action() -> str:
    """Return user input value for next game action"""

    return input('Press enter to continue, r to restart, or q to quit: ')


def _bound_number(number: int, min_num: int, max_num: int) -> int:
    """Return a bounded number between min-max"""

    return max(min_num, min(number, max_num))
