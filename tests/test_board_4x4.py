from app.board import Board

__author__ = 'kyleaclark'


def test_board_grid_cells_4x4_empty():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )
    board = Board(num_rows=4, num_cols=4, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )
    assert board.grid_cell_states == expected_cell_values


def test_board_grid_cells_4x4_one():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 0]]
    )
    board = Board(num_rows=4, num_cols=4, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )
    assert board.grid_cell_states == expected_cell_values



def test_board_grid_cells_4x4_two():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 0]]
    )
    board = Board(num_rows=4, num_cols=4, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )
    assert board.grid_cell_states == expected_cell_values


def test_board_grid_cells_4x4_many():
    # arrange
    pre_seeded_values = (
        [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    )
    board = Board(num_rows=4, num_cols=4, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )

    assert board.grid_cell_states == expected_cell_values


def test_board_grid_cells_4x4_many_multi_generation():
    # arrange
    pre_seeded_values = (
        [[0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]
    )
    board = Board(num_rows=4, num_cols=4, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()
    board.update_board_cells()

    expected_cell_values = (
        [[0, 1, 0, 0],
         [1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    )

    assert board.grid_cell_states == expected_cell_values


def test_board_grid_cells_4x4_many_multi_generation_infinite():
    # arrange
    pre_seeded_values = (
        [[1, 1, 0, 1],
         [0, 0, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 1]]
    )

    board = Board(num_rows=4, num_cols=4, pre_seeded_values=pre_seeded_values)

    # act + assert
    expected_cell_values = (
        [[0, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )

    board.update_board_cells()
    assert board.grid_cell_states == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_states == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_states == expected_cell_values
