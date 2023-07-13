from random import randint

def ran_row(grid):
    return randint(0, len(grid - 1))

def ran_col(grid):
    return randint(0, len(grid[0] - 1))


ship_row = ran_row(grid)
ship_col = ran_col(grid)

for turn in range(4):
    print ("Turn"), turn
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Miss")
        elif(grid[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            grid[guess_row][guess_col] = "X"
    if turn == 4:
        print("Game Over")
    turn = turn + 1
    print_grid(grid)
    
    
