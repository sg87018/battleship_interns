from random import randint

# Making the 10x10 grid
grid_size = 10
grid = [['O'] * grid_size for _ in range(grid_size)]
player_guess_grid = [['O'] * grid_size for _ in range(grid_size)]
enemy_grid = [['O'] * grid_size for _ in range(grid_size)]

def create_grid(grid, show_ships=False):
    print('', end=' ')
    for col in range(1, len(grid[0]) + 1):
        print(f'{col:2}', end='')
    print()

    for i, row in enumerate(grid):
        print(chr(65 + i) + ' ', end='')

        for column in row:
            if not show_ships and column in ['S', 'D']:
                print('O', end=' ')
            else:
                print(column, end=' ')

        print()
print("Welcome to the game, Battleship!")

# Getting valid user input and making the computer recognize to convert the ascii value to a row index
def get_valid_ship_coordinate(prompt):
    while True:
        coordinate = input(prompt).strip().upper()
        
        if len(coordinate) == 1 and 65 <= ord(coordinate) <= 74:
            row_index = ord(coordinate) - 65
            return row_index           
        elif coordinate.isdigit():
            column_index = int(coordinate) - 1
            if 0 <= column_index < grid_size:
                return column_index 

# Function to get user to place ships on a valid coordinate
def place_Carrier(grid, ship_length, ship_marker, user_ship_name1):
    print(f"Place your '{user_ship_name1}' ({Carrier_length} indices long)")
    while True:
        while True:
            row_index = get_valid_ship_coordinate(f"Please enter a row (A to {chr(64 + grid_size)}): ")
            user_ship_col = get_valid_ship_coordinate("Please enter a col (1-10): ")

            if grid[row_index][user_ship_col] != 'O':
                print("You can't place a ship there. Try again.")
                continue
            break

        orientation = input("Choose orientation (H for horizontal, V for vertical): ").upper()
        if orientation not in ['H', 'V']:
            print("Invalid orientation. Try again.")
            continue

        valid_placement = True
        if orientation == 'H' and user_ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index][user_ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index][user_ship_col + i] = ship_marker
                break

        elif orientation == 'V' and row_index + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index + i][user_ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index + i][user_ship_col] = ship_marker
                break

        print("Invalid placement. Try again.")
        
def place_Battleship(grid, ship_length, ship_marker, user_ship_name2):
    print(f"Place your '{user_ship_name2}' ({Battleship_length} indices long)")
    while True:
        while True:
            row_index = get_valid_ship_coordinate(f"Please enter a row (A to {chr(64 + grid_size)}): ")
            user_ship_col = get_valid_ship_coordinate("Please enter a col (1-10): ")

            if grid[row_index][user_ship_col] != 'O':
                print("You can't place a ship there. Try again.")
                continue
            break

        orientation = input("Choose orientation (H for horizontal, V for vertical): ").upper()
        if orientation not in ['H', 'V']:
            print("Invalid orientation. Try again.")
            continue

        valid_placement = True
        if orientation == 'H' and user_ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index][user_ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index][user_ship_col + i] = ship_marker
                break

        elif orientation == 'V' and row_index + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index + i][user_ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index + i][user_ship_col] = ship_marker
                break

        print("Invalid placement. Try again.")
        
def place_Destroyer(grid, ship_length, ship_marker, user_ship_name3):
    print(f"Place your '{user_ship_name3}' ({Destroyer_length} indices long)")
    while True:
        while True:
            row_index = get_valid_ship_coordinate(f"Please enter a row (A to {chr(64 + grid_size)}): ")
            user_ship_col = get_valid_ship_coordinate("Please enter a col (1-10): ")

            if grid[row_index][user_ship_col] != 'O':
                print("You can't place a ship there. Try again.")
                continue
            break

        orientation = input("Choose orientation (H for horizontal, V for vertical): ").upper()
        if orientation not in ['H', 'V']:
            print("Invalid orientation. Try again.")
            continue

        valid_placement = True
        if orientation == 'H' and user_ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index][user_ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index][user_ship_col + i] = ship_marker
                break

        elif orientation == 'V' and row_index + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index + i][user_ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index + i][user_ship_col] = ship_marker
                break

        print("Invalid placement. Try again.")
        
def place_Submarine(grid, ship_length, ship_marker, user_ship_name4):
    print(f"Place your '{user_ship_name4}' ({Submarine_length} indices long)")
    while True:
        while True:
            row_index = get_valid_ship_coordinate(f"Please enter a row (A to {chr(64 + grid_size)}): ")
            user_ship_col = get_valid_ship_coordinate("Please enter a col (1-10): ")

            if grid[row_index][user_ship_col] != 'O':
                print("You can't place a ship there. Try again.")
                continue
            break

        orientation = input("Choose orientation (H for horizontal, V for vertical): ").upper()
        if orientation not in ['H', 'V']:
            print("Invalid orientation. Try again.")
            continue

        valid_placement = True
        if orientation == 'H' and user_ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index][user_ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index][user_ship_col + i] = ship_marker
                break

        elif orientation == 'V' and row_index + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index + i][user_ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index + i][user_ship_col] = ship_marker
                break

        print("Invalid placement. Try again.")
        
def place_Patrol(grid, ship_length, ship_marker, user_ship_name5):
    print(f"Place your '{user_ship_name5}' ({Patrol_length} indices long)")
    while True:
        while True:
            row_index = get_valid_ship_coordinate(f"Please enter a row (A to {chr(64 + grid_size)}): ")
            user_ship_col = get_valid_ship_coordinate("Please enter a col (1-10): ")

            if grid[row_index][user_ship_col] != 'O':
                print("You can't place a ship there. Try again.")
                continue
            break

        orientation = input("Choose orientation (H for horizontal, V for vertical): ").upper()
        if orientation not in ['H', 'V']:
            print("Invalid orientation. Try again.")
            continue

        valid_placement = True
        if orientation == 'H' and user_ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index][user_ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index][user_ship_col + i] = ship_marker
                break

        elif orientation == 'V' and row_index + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[row_index + i][user_ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[row_index + i][user_ship_col] = ship_marker
                break

        print("Invalid placement. Try again.")       

# Function for computer to place ships on a random coordinate that don't overlap
def random_computer_carrier(grid, num_ships, ship_length, ship_marker, ship_name):
    ship_length = 5
    
    while True:
        ship_row = randint(0, grid_size - 1)
        ship_col = randint(0, grid_size - 1)

        orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
        valid_placement = True
        if orientation == 0 and ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row][ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row][ship_col + i] = ship_marker
                break

        elif orientation == 1 and ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row + i][ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row + i][ship_col] = ship_marker
                break
            
def random_computer_battleship(grid, num_ships, ship_length, ship_marker, ship_name):
    ship_length = 4
    
    while True:
        ship_row = randint(0, grid_size - 1)
        ship_col = randint(0, grid_size - 1)

        orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
        valid_placement = True
        if orientation == 0 and ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row][ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row][ship_col + i] = ship_marker
                break

        elif orientation == 1 and ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row + i][ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row + i][ship_col] = ship_marker
                break
            
def random_computer_destroyer(grid, num_ships, ship_length, ship_marker, ship_name):
    ship_length = 3
    
    while True:
        ship_row = randint(0, grid_size - 1)
        ship_col = randint(0, grid_size - 1)
        
        orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
        valid_placement = True
        if orientation == 0 and ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row][ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row][ship_col + i] = ship_marker
                break

        elif orientation == 1 and ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row + i][ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row + i][ship_col] = ship_marker
                break
            
def random_computer_submarine(grid, num_ships, ship_length, ship_marker, ship_name):
    ship_length = 3
    
    while True:
        ship_row = randint(0, grid_size - 1)
        ship_col = randint(0, grid_size - 1)

        orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
        valid_placement = True
        if orientation == 0 and ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row][ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row][ship_col + i] = ship_marker
                break

        elif orientation == 1 and ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row + i][ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row + i][ship_col] = ship_marker
                break
            
def random_computer_patrol(grid, num_ships, ship_length, ship_marker, ship_name):
    ship_length = 2
    
    while True:
        ship_row = randint(0, grid_size - 1)
        ship_col = randint(0, grid_size - 1)

        orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
        valid_placement = True
        if orientation == 0 and ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row][ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row][ship_col + i] = ship_marker
                break

        elif orientation == 1 and ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row + i][ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row + i][ship_col] = ship_marker
                break

# Naming and differentiating each ship
if __name__ == "__main__":
    num_ships_per_player = 5
    
    Carrier_length = 5
    Battleship_length = 4
    Destroyer_length = 3
    Submarine_length = 3
    Patrol_length = 2
    

    user_ship_marker1 = 'C'
    user_ship_name1 = "Carrier"   
    place_Carrier(grid, Carrier_length, user_ship_marker1, user_ship_name1)

    user_ship_marker2 = 'B'
    user_ship_name2 = "Battleship"
    place_Battleship(grid, Battleship_length, user_ship_marker2, user_ship_name2)
    
    user_ship_marker3 = 'D'
    user_ship_name3 = "Destroyer"
    place_Destroyer(grid, Destroyer_length, user_ship_marker3, user_ship_name3)
    
    user_ship_marker4 = 'S'
    user_ship_name4 = "Submarine"
    place_Submarine(grid, Submarine_length, user_ship_marker4, user_ship_name4)
    
    user_ship_marker5 = 'P'
    user_ship_name5 =  "Patrol Boat"
    place_Patrol(grid, Patrol_length, user_ship_marker5, user_ship_name5)

    computer_ship_marker1 = 'C'
    computer_ship_name1 = "Carrier"
    random_computer_carrier(enemy_grid, num_ships_per_player, Carrier_length, computer_ship_marker1, computer_ship_name1)

    computer_ship_marker2 = 'B'
    computer_ship_name2 = "Battleship"
    random_computer_battleship(enemy_grid, num_ships_per_player, Battleship_length, computer_ship_marker2, computer_ship_name2)
    
    computer_ship_marker3 = 'D'
    computer_ship_name3 = "Destroyer"
    random_computer_destroyer(enemy_grid, num_ships_per_player, Destroyer_length, computer_ship_marker3, computer_ship_name3)
    
    computer_ship_marker4 = 'S'
    computer_ship_name4 = "Submarine"
    random_computer_submarine(enemy_grid, num_ships_per_player, Submarine_length, computer_ship_marker4, computer_ship_name4)
    
    computer_ship_marker5 = 'P'
    computer_ship_name5 = "Patrol Boat"
    random_computer_patrol(enemy_grid, num_ships_per_player, Patrol_length, computer_ship_marker5, computer_ship_name5)
    
    # The actual Battleship game
    print()
    print("Let's play Battleship!")
    print("Your grid:")
    create_grid(grid, show_ships=True) # Show user's grid with their ships
    print()
    print("You're guessing grid:")
    create_grid(player_guess_grid, show_ships=False)
    print("\n")
    
    user_ships_remaining = ((num_ships_per_player * 2) + 7)
    computer_ships_remaining =((num_ships_per_player * 2) + 7)
    
    computer_carrier_remaining = 5
    computer_battleship_remaining = 4
    computer_destroyer_remaining = 3
    computer_submarine_remaining = 3
    computer_patrol_remaining = 2
    #computer_ships = [computer_ship_marker, computer_ship_marker]
    
    # Game logic for user attempting to sink computer's ships
    turn = 0
    for turn in range(100):
        print("Turn", turn + 1)
        while True:
            guess_row = get_valid_ship_coordinate("Which row do you want to strike? (A - J): ")
            guess_col = get_valid_ship_coordinate("Which column do you want to strike? (1-10): ")
            
            computer_guess_row = randint(0, 9)
            computer_guess_col = randint(0, 9)
            
            if player_guess_grid[guess_row][guess_col] in ['X', 'M']:
                print("You've already guessed this spot. Try again.")
            else:
                break
        
        if enemy_grid[guess_row][guess_col] not in (computer_ship_marker1, computer_ship_marker2, computer_ship_marker3, computer_ship_marker4, computer_ship_marker5):
            print()
            print(f"You struck at {chr(65 + guess_row)} , {guess_col + 1} and missed!")
            player_guess_grid[guess_row][guess_col] = "M"
        
        if enemy_grid[guess_row][guess_col] == 'C':
            print(f"You hit the enemy's {computer_ship_name1}!")
            grid[guess_row][guess_col] = "X"
            computer_ships_remaining -= 1
            computer_carrier_remaining -= 1
            
            if computer_carrier_remaining == 0:
                print("You sunk the enemy's Carrier!" )
                
            
        elif enemy_grid[guess_row][guess_col] == 'B':
            print(f"You hit the enemy's {computer_ship_name2}!")
            player_guess_grid[guess_row][guess_col] = "X"
            computer_ships_remaining -= 1
            computer_battleship_remaining -= 1
            
            if computer_battleship_remaining == 0:
                print("You sunk the enemy's Battleship!")
              
        
        elif enemy_grid[guess_row][guess_col] == 'D':
            print(f"You hit the enemy's {computer_ship_name3}!")
            player_guess_grid[guess_row][guess_col] = "X"
            computer_ships_remaining = computer_ships_remaining - 1
            computer_destroyer_remaining -= 1
            
            if computer_destroyer_remaining == 0:
                print("You sunk the enemy's Destroyer!")
                
        
        elif enemy_grid[guess_row][guess_col] == 'S':
            print(f"You hit the enemy's {computer_ship_name4}!")
            player_guess_grid[guess_row][guess_col] = "X"
            computer_ships_remaining -= 1
            computer_submarine_remaining -= 1
            
            if computer_submarine_remaining == 0:
                print("You sunk the enemy's Submarine!")
                
            
            
        elif enemy_grid[guess_row][guess_col] == 'P':
            print(f"You hit the enemy's {computer_ship_name5}!")
            player_guess_grid[guess_row][guess_col] = "X"
            computer_ships_remaining -= 1
            computer_patrol_remaining -= 1
            
            if computer_patrol_remaining == 0:
                print("You sunk the enemy's Patrol boat!")
                
        # Game logic for computer attempting to sink user's ships
        if grid[computer_guess_row][computer_guess_col] == 'O':
            print()
            enemy_grid[computer_guess_row][computer_guess_col] = 'M'
            print(f"Computer struck at {chr(65 + computer_guess_row)}, {computer_guess_col} and missed!")
            print('\n')
            
            if user_ships_remaining == 0:
                print("All your ships have sunk! You lose!")
                break
            
            
        elif grid[computer_guess_row][computer_guess_col] in (user_ship_marker1, user_ship_marker2, user_ship_marker3, user_ship_marker4, user_ship_marker5):
            print('\n')
            grid[computer_guess_row][computer_guess_col] = 'H'
            print("Computer hit your ship!")
            print('\n')
            user_ships_remaining -= 1
        
            #if grid[computer_guess_row][computer_guess_col] == 'H' or grid[computer_guess_row][computer_guess_col] == 'M': 
                #print("Computer already guessed here")
        else:
            print('Computer already guessed here!')
            
        # Ending the game
        if computer_ships_remaining == 0:
            print("Congratulations! You sunk all of the enemies ships!")
            break
        
        elif user_ships_remaining == 0:
            print("All your ships have sunk! You lose!")
            break
           
            
                
        print("You're grid:")
        create_grid(grid, show_ships=True)
        print('\n')
        print("You're guessing grid:")
        create_grid(player_guess_grid, show_ships=False)
        print('\n')
        
        if turn == 50 or (user_ships_remaining == 0 or computer_ships_remaining == 0):
            print("\nGAME OVER")
            if user_ships_remaining != 0 and computer_ships_remaining != 0:
                print("It's a tie! Both players couldn't sink any ships.")
