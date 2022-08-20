from functools import partial

import matplotlib.animation as animation
import matplotlib.cm as colormap
import matplotlib.pyplot as plt
import numpy as np

from app.board import Board

__author__ = 'kyleaclark'


def animate_board_grid(board: Board, save_gif: bool = False, save_mp4: bool = False):
    fig, axes = plt.subplots(figsize=(7, 7))

    axes.set_facecolor('black')
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    np_array = np.array(board.grid_cell_values)
    x_grid, y_grid = np.meshgrid(np.arange(np_array.shape[1]), np.arange(np_array.shape[0]))
    scatter = axes.scatter(x_grid[np_array >= 0], y_grid[np_array >= 0], s=60, edgecolor=None)

    colors = _generate_cell_colors(board)
    scatter.set_facecolor(colors)

    ani = animation.FuncAnimation(fig, partial(_update_animation, board, scatter), interval=200, frames=20)

    if save_gif:
        ani.save('game-of-life.gif', writer='pillow')

    if save_mp4:
        ani.save(f'game-of-life.mp4', writer=animation.FFMpegFileWriter())

    if not save_gif and not save_mp4:
        plt.show()


def _update_animation(board: Board, scatter: plt.scatter, *_) -> plt.scatter:
    board.update_board_cells()
    scatter.set_facecolor(_generate_cell_colors(board))

    return scatter


def _generate_cell_colors(board: Board) -> list[tuple]:
    sliced_cm = colormap.Blues_r(np.linspace(0, 1, 9))
    grid_color_map = [sliced_cm[cell.alive_neighbors] for cell in board.grid_cells_flattened]
    result = [(r, g, b, 1) if cell_value else (r, g, b, 0) for cell_value, (r, g, b, a)
              in zip(board.grid_cell_values_flattened, grid_color_map)]

    return result
