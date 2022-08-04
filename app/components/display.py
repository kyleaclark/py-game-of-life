from functools import partial
from typing import List

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
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
    fig, axes = plt.subplots(figsize=(7, 7))

    axes.set_title('Conway\'s Game of Life', fontweight='bold')
    axes.set_facecolor('black')
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    data = np.array(board.grid_cell_values)
    X, Y = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
    scatter = axes.scatter(X[data >= 0], Y[data >= 0], s=60, edgecolor=None)

    cmap = mpl.cm.Blues_r
    slicedCM = cmap(np.linspace(0, 1, 9))
    color_map = [slicedCM[cell.alive_neighbors] for cell in board.grid_cells_flattened]
    colors = [(r, g, b, 1) if cell_value else (r, g, b, 0) for cell_value, (r, g, b, a)
              in zip(board.grid_cell_values_flattened, color_map)]
    scatter.set_facecolor(colors)

    _ = animation.FuncAnimation(fig, partial(_update_v2, board, scatter))
    plt.show()


def _update_v2(board, scatter, *kwargs):
    board.update_board_cells()

    cmap = mpl.cm.Blues_r
    slicedCM = cmap(np.linspace(0, 1, 9))
    color_map = [slicedCM[cell.alive_neighbors] for cell in board.grid_cells_flattened]
    colors = [(r, g, b, 1) if cell_value else (r, g, b, 0) for cell_value, (r, g, b, a)
              in zip(board.grid_cell_values_flattened, color_map)]

    scatter.set_facecolor(colors)

    return scatter

def _update_animated_board(board: Board2d, mat: AxesImage, _) -> List[AxesImage]:
    board.update_board_cells()
    mat.set_data(board.grid_cell_values)

    return [mat]
