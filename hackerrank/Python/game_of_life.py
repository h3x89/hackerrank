# This Python program simulates Conway’s Game of Life on a 20x20 grid (using a 2D list or array). Each cell can exist in one of two states: “alive” or “dead.” The initial state of the grid is randomly generated, with each cell having a 50% chance of being alive.

# The program operates by applying the following rules to each cell at every generation:

# 	1.	Any live cell with two or three live neighbors will remain alive (survival).
# 	2.	Any dead cell with exactly three live neighbors becomes alive (birth).
# 	3.	Any live cell with fewer than two or more than three live neighbors dies (due to loneliness or overcrowding).

# Each generation is displayed on the console, updating the grid every half second. The “#” symbol represents live cells, while “.” represents dead cells. With each update, the previous generation should be cleared from the console.

# The simulation runs for 100 generations or until the user stops it manually.

import random
import time
import os
import sys

# Define the dimensions of the grid
WIDTH, HEIGHT = 140, 30
generation_limit = 10000
SLIPE_TIME = 0.01

# Initialize the grid with random alive (1) or dead (0) cells
grid = [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def display_grid(grid):
    """Display the grid on the console."""
    for row in grid:
        print(''.join('#' if cell else '.' for cell in row))

def count_neighbors(grid, x, y):
    """Count the number of alive neighbors for a cell at position (x, y)."""
    count = 0
    # Define the range for neighbor coordinates
    for i in range(max(0, x - 1), min(HEIGHT, x + 2)):
        for j in range(max(0, y - 1), min(WIDTH, y + 2)):
            if (i, j) != (x, y):
                count += grid[i][j]
    return count

def next_generation(current_grid):
    """Compute the next generation of the grid based on Conway's rules."""
    new_grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for x in range(HEIGHT):
        for y in range(WIDTH):
            alive = current_grid[x][y]
            neighbors = count_neighbors(current_grid, x, y)
            if alive:
                # Survival conditions
                if neighbors == 2 or neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    # Cell dies due to loneliness or overcrowding
                    new_grid[x][y] = 0
            else:
                # Birth condition
                if neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
    return new_grid

def clear_console():
    """Clear the console output."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Introduce random new life to the grid with a given probability just for fun ;)
def introduce_random_life(grid, probability=0.05):
    """Introduce random new life to the grid with a given probability."""
    for x in range(HEIGHT):
        for y in range(WIDTH):
            if random.random() < probability:
                grid[x][y] = 1

try:
    generation = 0
    while generation < generation_limit:
        clear_console()
        generation += 1
        print(f"Generation {generation}")
        display_grid(grid)
        grid = next_generation(grid)
        if generation % 100 == 0:
            introduce_random_life(grid)
        time.sleep(SLIPE_TIME)  # Pause for animation effect
except KeyboardInterrupt:
    # Exit gracefully on user interrupt
    sys.exit()