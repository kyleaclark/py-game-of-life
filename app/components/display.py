from functools import partial
from typing import List

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.image import AxesImage

from app.components.board1d import Board1d
from app.components.board2d import Board2d

__author__ = 'kyleaclark'


def draw_board_grid(board: Board1d):
    print('')
    for cell_idx, cell in enumerate(board._grid):
        print(cell.get_text_character(), end='')

        if board.is_last_col(cell_idx):
            print('')

    print('')


def animate_board_grid(board: Board2d):
    fig, ax = plt.subplots()
    ax.set_title('Conway\'s Game of Life')
    ax.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False)
    mat = ax.matshow(board.grid_cell_values)
    _ = animation.FuncAnimation(fig, partial(_update_animated_board, board, mat))
    plt.show()


def _update_animated_board(board: Board2d, mat: AxesImage, _) -> List[AxesImage]:
    board.update_board_cells()
    mat.set_data(board.grid_cell_values)

    return [mat]


def _get_animated_colors(status, c):
    cmap = mpl.cm.Blues_r
    rescale = c / 8  # Maximum of 8 neighbors
    colors = [cmap(neighbors) for neighbors in rescale.flatten()]
    is_live = status.flatten()
    colors = [(r, g, b, 0.9) if live else (r, g, b, 0) for live, (r, g, b, a) in zip(is_live, colors)]
    return colors