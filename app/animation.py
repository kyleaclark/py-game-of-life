import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from app.board import Board

__author__ = 'kyleaclark'


class Animation:

    def __init__(self, board: Board):
        self._board = board

    def animate_board_grid(self, save_gif: bool = False, save_mp4: bool = False):
        fig, axes = plt.subplots(figsize=(7, 7))

        self._stylize_plot(axes)
        self._create_scatter(axes)
        self._update_scatter_colors()
        self._create_animation(fig)

        if save_gif:
            self._save_animation_gif()
        elif save_mp4:
            self._save_animation_mp4()
        else:
            plt.show()

    def _stylize_plot(self, axes):
        axes.set_title('Conway\'s Game of Life', fontweight='bold')
        axes.set_facecolor('black')
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)

    def _create_scatter(self, axes):
        np_array = np.array(self._board.grid_cell_values)
        x_grid, y_grid = np.meshgrid(np.arange(np_array.shape[1]), np.arange(np_array.shape[0]))
        self._scatter = axes.scatter(x_grid[np_array >= 0], y_grid[np_array >= 0], s=60, edgecolor=None)

    def _update_scatter_colors(self):
        sliced_cm = mpl.cm.Blues_r(np.linspace(0, 1, 9))
        color_map = [sliced_cm[cell.alive_neighbors] for cell in self._board.grid_cells_flattened]
        colors = [(r, g, b, 1) if cell_value else (r, g, b, 0) for cell_value, (r, g, b, a)
                  in zip(self._board.grid_cell_values_flattened, color_map)]

        self._scatter.set_facecolor(colors)

    def _create_animation(self, fig):
        self._ani = animation.FuncAnimation(fig, self._compute_animation, interval=100, frames=20)

    def _compute_animation(self, _):
        self._board.update_board_cells()
        self._update_scatter_colors()

        return self._scatter

    def _save_animation_gif(self):
        print('Saving animation gif...')
        self._ani.save('game-of-life-animation.gif', writer='pillow')

    def _save_animation_mp4(self):
        print('Saving animation mp4...')
        self._ani.save(f'game_of_life.mp4', writer=animation.FFMpegFileWriter())
