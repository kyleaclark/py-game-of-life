# Py-Game-of-Life

- Authored by Kyle Clark - [kyleaclark.com](https://kyleaclark.com)
- Run application as a text game or simulated animation

### Game of Life

#### Overview

- Game of Life is similar to Game of Thrones, except they're not really the same.
- Game of Life was created by mathematician John Conway in 1970 as a way to represent the interactions of cells.
- Played on a two-dimensional grid with a maximum of 8 neighbours for a grid square.
- Zero-player game determined by the initial random state of cells alive or dead.  
- Subsequent states are determined by a set of rules.

#### Rules

1. Any live cell with 2 or 3 live neighbours lives on to the next generation (survival).
2. Any live cell with fewer than 2 live neighbours dies (under-population).
3. Any live cell with more than 3 live neighbors dies (overcrowding).
4. Any dead cell with exactly 3 live neighbors evolves into a live cell (reproduction).
5. Each cell lives or dies independently (non-sequentially) in a generational evolution.

___

### App Environment

- Python 3.10.6
- Poetry dependency management
- Setup instructions are specific to macOS. Steps may vary.

#### Setup Prerequisites

1. Install pyenv for python version management - https://github.com/pyenv/pyenv
2. Update pyenv if previously installed e.g. via brew `brew upgrade pyenv`
3. Install poetry for python dependency management - https://python-poetry.org/docs/#installation
4. Update poetry if necessary (optional): `poetry self update`
4. Add pyenv path to profile e.g. add `export PYENV_ROOT="$HOME/.pyenv` + `export PATH="$PYENV_ROOT/bin:$PATH"`
5. Add poetry path to profile e.g. add `export PATH="$HOME/.poetry/bin/:PATH`
6. Install python version: `pyenv install 3.10.6`

#### Python Environment

1. Set python version within the repo directory: `pyenv local 3.10.6`
2. Set the poetry env version of python: `poetry env use ~/.pyenv/versions/3.10.6/bin/python`
3. Install python application dependencies: `poetry install`
   
#### Python Execution
4. Run text game via terminal: `poetry run python run_text_game.py`
5. Run simulated animation via terminal: `poetry run python run_simulated_animation.py`   
5. Run tests via terminal: `poetry run python -m pytest -p no:cacheprovider tests`

#### Optional: PyCharm Setup

1. Open PyCharm Preferences
2. Open Project Interpeter > Add existing Virtualenv Environment e.g. `/Users/<username>/Library/Caches/pypoetry/virtualenvs/<poetry-name>/bin/python`
3. Open Tools > Python Integrated Tools > Default test runner: pytest
4. Run text game: Right-click on `run_text_game.py` and choose Run
5. Run simulated animation: Right-click on `run_simulated_animation.py` and choose Run
6. Run tests via pytest: Right-click on `tests` and choose Run

___

### Poetry Reference

- Poetry documentation - https://python-poetry.org/docs/
- `poetry install` - Install dependencies from poetry.lock - https://python-poetry.org/docs/cli/#install
- `poetry update` - Update poetry.lock from pyproject.toml - https://python-poetry.org/docs/cli/#update
- `poetry add` - Add a dependency into pyproject.toml - https://python-poetry.org/docs/cli/#add
- `poetry remove` - Remove a dependency in pyproject.toml and update poetry.lock - https://python-poetry.org/docs/cli/#remove
