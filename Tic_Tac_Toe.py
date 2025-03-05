# Initialize empty board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--|---|--")

# Function to check if a player has won
def check_winner(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pattern in win_patterns:
        count = 0  
        for i in pattern:
            if board[i] == player:
                count += 1
        if count == 3:  
            return True

    return False  


def tic_tac_toe():
    current_player = "X"
    
    for turn in range(9):  
        print_board()
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                if check_winner(current_player):
                    print_board()
                    print(f"Congrats!! Player {current_player} wins!")
                    return
                
                if current_player == "X":
                    current_player = "O"
                else:
                     current_player = "X"

            else:
                print("Spot taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input, enter a number between 1-9.")

    print_board()
    print("It's a draw!")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
