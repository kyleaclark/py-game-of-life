from app.components.game_loop import run_game_loop

__author__ = 'kyleaclark'


def init():
    print('Game of Life is played on a board of cells with rows and columns')

    run_game_loop()


if __name__ == '__main__':
    init()
