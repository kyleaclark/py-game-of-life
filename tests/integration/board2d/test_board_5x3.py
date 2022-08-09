from app.board import Board

__author__ = 'kyleaclark'


def test_board_grid_cells_5x3_empty():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    board = Board(num_rows=5, num_cols=3, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_5x3_one():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    board = Board(num_rows=5, num_cols=3, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    assert board.grid_cell_values == expected_cell_values



def test_board_grid_cells_5x3_two():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0],
         [0, 1, 0],
         [0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    board = Board(num_rows=5, num_cols=3, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_5x3_many():
    # arrange
    pre_seeded_values = (
        [[0, 0, 1],
         [0, 0, 1],
         [0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )
    board = Board(num_rows=5, num_cols=3, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()

    # assert
    expected_cell_values = (
        [[0, 0, 0],
         [0, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )

    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_5x3_many_multi_generation_infinite():
    # arrange
    pre_seeded_values = (
        [[1, 0, 0],
         [1, 0, 0],
         [1, 1, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )

    board = Board(num_rows=5, num_cols=3, pre_seeded_values=pre_seeded_values)

    # act
    board.update_board_cells()
    board.update_board_cells()

    # act + assert
    expected_cell_values = (
        [[0, 0, 0],
         [1, 1, 0],
         [1, 1, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values


def test_board_grid_cells_5x3_many_multi_generation_rotation():
    # arrange
    pre_seeded_values = (
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )

    board = Board(num_rows=5, num_cols=3, pre_seeded_values=pre_seeded_values)

    # act + assert
    expected_cell_values = (
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0],
         [0, 0, 0],
         [0, 0, 0]]
    )

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values

    board.update_board_cells()
    assert board.grid_cell_values == pre_seeded_values

    board.update_board_cells()
    assert board.grid_cell_values == expected_cell_values
