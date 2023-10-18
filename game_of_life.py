## Initialize a 20x20 grid and place the Glider Pattern for the Game of Life in the middle of the grid
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import argparse
import sys

parser = argparse.ArgumentParser(description='Game of Life: Run for K steps')
parser.add_argument('steps',  type=int, nargs='?', default=200, help='number of steps to run the simulation')
args = parser.parse_args()
steps = args.steps
if steps <= 0:
    print("Steps must be greater than 0")
    sys.exit(1)

# Initialize a 20x20 grid with all zeros
grid = np.zeros((20, 20), dtype=bool)

# Place the Glider Pattern in the middle of the grid
grid[9][10] = True
grid[10][11] = True
grid[11][9:12] = True

fig, ax = plt.subplots()
# create a variable named gen_text, set the position to be centered, above the graph.
gen_text = ax.text(0.5, -1.01, '', ha="center")
im = plt.imshow(grid, cmap='binary')

def check_life(cell, neighbors):
    """ Check if a cell lives or dies """
    ## Copilot auto-generated immediately after definition of check_life()
    # If the cell is alive
    if cell:
        # If the cell has less than 2 neighbors, it dies
        if sum(neighbors) < 2:
            return False
        # If the cell has more than 3 neighbors, it dies
        elif sum(neighbors) > 3:
            return False
        # If the cell has 2 or 3 neighbors, it lives
        else:
            return True
    # If the cell is dead
    else:
        # If the cell has exactly 3 neighbors, it lives
        if sum(neighbors) == 3:
            return True
        # If the cell does not have exactly 3 neighbors, it stays dead
        else:
            return False

import numpy as np

def evolve(grid):
    """ Evolve the grid by one step 
    
    Parameters:
    grid (numpy.ndarray): A 2D numpy array representing the current state of the grid
    
    Returns:
    numpy.ndarray: A 2D numpy array representing the new state of the grid after one step of evolution
    """
    
    # Initialize a new grid with all zeros
    new_grid = np.zeros((20, 20), dtype=bool)
    
    # Loop over the grid and check each cell
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Wrap around the bottom and right edges of the grid, if necessary
            botWrap = (j+1) if j < len(grid[i]) - 1 else 0
            rightWrap = (i+1) if i < len(grid) - 1 else 0

            neighbors = []
            # Left Side
            neighbors.append(grid[i-1][j-1])
            neighbors.append(grid[i-1][j])
            neighbors.append(grid[i-1][botWrap])

            # Top and Bottom
            neighbors.append(grid[i][botWrap])
            neighbors.append(grid[i][j-1])

            # Right Side
            neighbors.append(grid[rightWrap][botWrap])
            neighbors.append(grid[rightWrap][j])
            neighbors.append(grid[rightWrap][j-1])

            new_grid[i][j] = check_life(grid[i][j], neighbors)

    return new_grid

def nextFrame(frame):
    """ Update the grid for the next frame
     This function is called by the animation library
      and calls evolve() to update the grid """
    global grid
    grid = evolve(grid)
    im.set_array(grid)
    im.figure.canvas.draw_idle()
    # Display current generation in the plot title, 0-based indexing
    gen_text.set_text(f'Generation: {frame + 1}')
    return im,

ani = animation.FuncAnimation(fig, nextFrame, frames=steps, interval=10, blit=True, cache_frame_data=True)

try:
    writergif = animation.PillowWriter(fps=10)
    ani.save('game_of_life_anim.gif', writer=writergif)

    writervideo = animation.FFMpegWriter(fps=10)
    ani.save('game_of_life_video.mp4', writer=writervideo)
except Exception as e:
    print("Error saving animation. Error message below:")
    if hasattr(e, 'message'):
        print(e.message)
    else:
        print(e)

plt.savefig('game_of_life_final_gen.png')
plt.close()