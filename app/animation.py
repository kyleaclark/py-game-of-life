from functools import partial

import matplotlib.animation as animation
import matplotlib.cm as colormap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

from app.board import Board


def animate_board_grid(board: Board, save_gif: bool = False, save_mp4: bool = False):
    """Animate board grid for visual display of simulation"""

    # Use matplotlib to create a figure and subplot axes object
    fig, ax = plt.subplots(figsize=(7, 7))

    # Initialize ax object color and visibility
    ax.set_facecolor('black')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Create scatter plot object
    scatter = _create_scatter_plot(ax, board.grid_cell_states)

    # Set scatter plot point colors given alive or dead cell state
    scatter.set_facecolor(_generate_plot_point_colors(board))

    # Create animated scatter plot simulating cell state interactivity
    ani = animation.FuncAnimation(
        fig, partial(_update_animation, board, scatter), interval=200, frames=20)

    # Optionally save animation as a gif
    if save_gif:
        ani.save('game-of-life.gif', writer='pillow')

    # Optionally save animation as a mp4
    if save_mp4:
        ani.save(f'game-of-life.mp4', writer=animation.FFMpegFileWriter())

    # If animation not saved, display animated plot
    if not save_gif and not save_mp4:
        plt.show()


def _create_scatter_plot(ax: Axes, grid_values: list[list[int]]):
    """Return scatter plot given an ax object and 2d list of values"""

    # Create numpy array from 2d list of grid values
    np_array = np.array(grid_values)

    # Create a rectangular grid of coordinate pairs given two 1d arrays
    # representing x-values (columns) and y-values (rows)
    x_grid, y_grid = np.meshgrid(np.arange(np_array.shape[1]), np.arange(np_array.shape[0]))

    # Create a scatter plot given two flattened x and y grids
    result = ax.scatter(x_grid[np_array >= 0], y_grid[np_array >= 0], s=60, edgecolor=None)

    return result


def _generate_plot_point_colors(board: Board) -> list[tuple]:
    """Return plot point colors given cell state & neighbor density"""

    sliced_cm = colormap.Blues_r(np.linspace(0, 1, 9))
    grid_color_map = [sliced_cm[cell.alive_neighbors] for cell in board.grid_cells_flattened]
    result = [(r, g, b, 1) if cell_value else (r, g, b, 0) for cell_value, (r, g, b, a)
              in zip(board.grid_cell_states_flattened, grid_color_map)]

    return result


def _update_animation(board: Board, scatter: plt.scatter, *_) -> plt.scatter:
    """Return updated scatter after generation of cell interactivity"""
    board.update_board_cells()
    scatter.set_facecolor(_generate_plot_point_colors(board))

    return scatter
