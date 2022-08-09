from functools import partial

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from app.board import Board

__author__ = 'kyleaclark'


def draw_board_grid(board: Board):
    print('')
    for row_idx, row in enumerate(board._grid):
        for cell_idx, cell in enumerate(row):
            character = ' 1 ' if cell.is_alive() else ' . '
            print(character, end='')

        # if board.is_last_col(cell_idx):
        #     print('')

    print('')


def animate_board_grid(board: Board, save_gif: bool = False, save_mp4: bool = False):
    fig, axes = plt.subplots(figsize=(7, 7))

    axes.set_title('Conway\'s Game of Life', fontweight='bold')
    axes.set_facecolor('black')
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    np_array = np.array(board.grid_cell_values)
    x_grid, y_grid = np.meshgrid(np.arange(np_array.shape[1]), np.arange(np_array.shape[0]))
    scatter = axes.scatter(x_grid[np_array >= 0], y_grid[np_array >= 0], s=60, edgecolor=None)

    _generate_cell_colors(board, scatter)
    ani = animation.FuncAnimation(fig, partial(_update_animation, board, scatter), interval=100, frames=20)

    if save_gif:
        ani.save('game-of-life-animation.gif', writer='pillow')

    if save_mp4:
        ani.save(f'game_of_life.mp4', writer=animation.FFMpegFileWriter())

    plt.show()


def _update_animation(board, scatter, _):
    board.update_board_cells()

    _generate_cell_colors(board, scatter)

    return scatter


def _generate_cell_colors(board: Board, scatter):
    cmap = mpl.cm.Blues_r
    sliced_cm = cmap(np.linspace(0, 1, 9))
    color_map = [sliced_cm[cell.live_neighbor_count] for cell in board.grid_cells_flattened]
    colors = [(r, g, b, 1) if cell_value else (r, g, b, 0) for cell_value, (r, g, b, a)
              in zip(board.grid_cell_values_flattened, color_map)]

    scatter.set_facecolor(colors)