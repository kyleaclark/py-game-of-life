from app.board import Board

__author__ = 'kyleaclark'


def test_board_grid_cells_3x5_empty():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    )
    board = Board(num_rows=3, num_cols=5, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    )
    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_3x5_one():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]
    )
    board = Board(num_rows=3, num_cols=5, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    )
    assert board.grid_cell_values == expected_cell_values



def test_board_grid_cells_3x5_two():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0]]
    )
    board = Board(num_rows=3, num_cols=5, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    )
    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_3x5_many():
    # arrange
    pre_seeded_values = (
        [[0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0]]
    )
    board = Board(num_rows=3, num_cols=5, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0]]
    )

    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_3x5_many_multi_generation_infinite():
    # arrange
    pre_seeded_values = (
        [[1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0]]
    )

    board = Board(num_rows=3, num_cols=5, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()
    board.update_board_cells()

    # act + assert
    expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0]]
    )

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_3x5_many_multi_generation_rotation():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
    )

    board = Board(num_rows=3, num_cols=5, pre_seeded_values=pre_seeded_values)

    # act + assert
    expected_cell_values = (
        [[0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0]]
    )

    rotated_expected_cell_values = (
        [[0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 1, 0, 1, 0]]
    )

    second_rotated_expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]
    )

    final_expected_cell_values = (
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    )

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == rotated_expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == second_rotated_expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == final_expected_cell_values
