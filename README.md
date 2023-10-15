# Conway's Game of Life for AMS 325

Fernando Hernandez  
Infinite orthogonal grid of square cells, each of which is alive or dead.
Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.  

## Rules

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.  

To simulate an infinite grid, we "wrap" the grid around itself. For example, the cell at the top left corner of the grid has neighbors at the top right, bottom left, bottom right, and so on.

## Usage

We will use Boolean values to determine the state of a cell. `True` means the cell is alive, and `False` means the cell is dead.  
Python will be used. The script is called `game_of_life.py` and can be ran from the command line with the number of evelutions as an argument. It can be executed as follows:

 ```bash
 python game_of_life.py 10
 ```
