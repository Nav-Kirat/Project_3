# Project_3
# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The game supports two players, "X" and "O," who take turns making moves on a 3x3 board. The game continues until one player wins by completing a row, column, or diagonal, or the board is full, resulting in a draw.

## Usage

To play the game, run the script and follow the on-screen prompts. Players take turns entering their moves by specifying a position on the board (1-9). The board is displayed after each move, and the game announces the winner or declares a draw when appropriate.

## Code Structure

### `initialize_board()`

This function initializes the game board with empty spaces.

### `display_board(board)`

Displays the current state of the board on the screen.

### `is_board_full(board)`

Checks if the board is full, indicating a draw.

### `check_win(board, player)`

Checks if the specified player has won by examining rows, columns, and diagonals.

### `get_player_input(board, player)`

Prompts the current player to enter their move and ensures the input is valid.

### `play_game()`

The main game loop where players take turns making moves until there is a winner or a draw.

### Running the Game

The game is started by calling `play_game()` in the script's main section.

## Player Representation

- Player "X" is represented by red text.
- Player "O" is represented by blue text.

## Notes

- Invalid moves are handled gracefully, and players are prompted to enter a valid position.
- The game uses ANSI escape codes to colorize player tokens for a visually appealing display.

Feel free to use, modify, and share this code for educational purposes or as a starting point for more advanced Tic-Tac-Toe implementations. Enjoy the game!
