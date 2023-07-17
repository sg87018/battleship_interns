from random import randint

def ran_row(grid):
    return randint(0, len(grid - 1))

def ran_col(grid):
    return randint(0, len(grid[0] - 1))


ship_row = ran_row(grid)
ship_col = ran_col(grid)

try:
    for turn in range(4):
        print ("Turn"), turn
    if turn == 4:
        print("Game Over")
    turn = turn + 1
except ValueError:
    print(grid)
    
    
