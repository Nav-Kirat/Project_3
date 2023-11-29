# Initialize the board
def initialize_board():
    """
    Initialize the board with empty spaces
    Parameters:
            None
    Returns:
            list: The board with empty spaces
    """
    return [" " for _ in range(9)]


# Display the board
def display_board(board):
    """
	Display the board on the screen
	Parameters:
			board (list): The current board
	Returns:
			None
	"""
    print("\n " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")


# Check if the board is full
def is_board_full(board):
    """
	Check if the board is full (no empty spaces)
	Parameters:
			board (list): The current board
	Returns:
			bool: True if the board is full, False otherwise
	"""
    if " "  not in board:
        #Board full
        return True
    else:
        #Board is not full
        return False

# Check for a win
def check_win(board, player):
    """
    Check if the player has won in any of the possible ways/conditions
    Parameters:
            board (list): The current board
            player (str): The player ("X" or "O")
    Returns:
            bool: True if the player has won, False otherwise
    """
    # Check rows
    for row in range(0, 9, 3):
        if board[row] == board[row + 1] == board[row + 2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[col] == board[col + 3] == board[col + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False
    pass


# Get player input
def get_player_input(board, player):
    """
    Get the player's move and check if it is valid
    Parameters:
		board (list): The current board
		player (str): The player ("X" or "O")
    Returns:
		int: The position of the player's move
    """

    while True:
        print("\nThe current player is: " + player)
        move = input("Enter your move (1-9): ")
        try:
            if board[int(move)-1] == " " and 0 < int(move) <= 9:
                return int(move) - 1
            else:
                print("|------------------------------|")
                print("\033[33m| Position Entered Is invalid. |\033[0m")
                print("|------------------------------|")
        except:
            print("|------------------------------|")
            print("\033[33m| Position Entered Is invalid. |\033[0m")
            print("|------------------------------|")


# Main game loop
def play_game():
    """
    The main game loop where the game is played until completion
    """
    board = initialize_board()
    player = "\033[31mX\033[0m"

    while True:
        display_board(board)
        move = get_player_input(board, player=player)
        board[move] = player


        if check_win(board, player):
            display_board(board)
            print(f"Player {player} is winner!")
            break


        if is_board_full(board):
            display_board(board)
            print("It's a draw between player")
            break

        if player == "\033[31mX\033[0m":
            player = "\033[34mO\033[0m"
        else:
            player = "\033[31mX\033[0m"


# Start the game
if __name__ == "__main__":
    play_game()
