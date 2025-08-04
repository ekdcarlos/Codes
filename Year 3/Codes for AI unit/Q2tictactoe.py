import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 650
BOARD_SIZE = 600
LINE_WIDTH = 10
CELL_SIZE = BOARD_SIZE // 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
FONT_SIZE = 40

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont('Arial', FONT_SIZE)

def draw_board(board):
    """Draws the Tic Tac Toe board and current moves."""
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the grid lines
    # Vertical lines
    pygame.draw.line(screen, BLACK, (CELL_SIZE, 0), (CELL_SIZE, BOARD_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, BOARD_SIZE), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE), (BOARD_SIZE, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * CELL_SIZE), (BOARD_SIZE, 2 * CELL_SIZE), LINE_WIDTH)
    
    # Draw the X's and O's
    for i in range(9):
        row = i // 3
        col = i % 3
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        
        if board[i] == "X":
            # Draw X (two lines)
            size = CELL_SIZE // 3
            pygame.draw.line(screen, RED, (center_x - size, center_y - size), 
                             (center_x + size, center_y + size), LINE_WIDTH)
            pygame.draw.line(screen, RED, (center_x + size, center_y - size), 
                             (center_x - size, center_y + size), LINE_WIDTH)
        elif board[i] == "O":
            # Draw O (circle)
            radius = CELL_SIZE // 3
            pygame.draw.circle(screen, BLUE, (center_x, center_y), radius, LINE_WIDTH)
    
    # Draw status message area
    pygame.draw.rect(screen, GRAY, (0, BOARD_SIZE, WIDTH, HEIGHT - BOARD_SIZE))
    
    pygame.display.flip()

def display_message(message, color=BLACK):
    """Displays a message below the game board."""
    # Cover the message area with gray
    pygame.draw.rect(screen, GRAY, (0, BOARD_SIZE, WIDTH, HEIGHT - BOARD_SIZE))
    
    # Render and display the message
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH//2, BOARD_SIZE + (HEIGHT - BOARD_SIZE)//2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def check_winner(board):
    """Checks if there's a winner or if the game is a tie.
    Returns:
        "X" if X wins
        "O" if O wins
        "Tie" if game is a tie
        None if game continues
    """
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # Returns the winning player (X or O)
    
    # Check for tie
    if " " not in board:
        return "Tie"
    
    return None  # No winner yet

def computer_move(board, computer_symbol):
    """Simple AI for the computer's move.
    Strategy:
    1. First try to win
    2. Then block the player from winning
    3. Take center if available
    4. Take a corner if available
    5. Take any available spot
    """
    # First, check if computer can win in the next move
    for i in range(9):
        if board[i] == " ":
            board[i] = computer_symbol
            if check_winner(board) == computer_symbol:
                return i
            board[i] = " "
    
    # Then, check if player can win in the next move and block them
    player_symbol = "X" if computer_symbol == "O" else "O"
    for i in range(9):
        if board[i] == " ":
            board[i] = player_symbol
            if check_winner(board) == player_symbol:
                board[i] = computer_symbol
                return i
            board[i] = " "
    
    # If center is empty, take it
    if board[4] == " ":
        return 4
    
    # Otherwise, choose a random available corner
    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == " "]
    if available_corners:
        return random.choice(available_corners)
    
    # Otherwise, choose any available spot
    available_spots = [i for i in range(9) if board[i] == " "]
    return random.choice(available_spots)

def get_board_position(mouse_pos):
    """Converts mouse position to board index (0-8)."""
    x, y = mouse_pos
    if y >= BOARD_SIZE:  # Clicked below the board
        return None
    
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    index = row * 3 + col
    return index

def play_game():
    """Main function to play the game with graphical interface."""
    # Initialize the board
    board = [" "] * 9
    current_player = "X"  # User goes first
    
    # Initial display
    draw_board(board)
    display_message("Your turn (X). Click on a square.")
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if current_player == "X" and event.type == pygame.MOUSEBUTTONDOWN:
                # User's turn - handle mouse click
                pos = pygame.mouse.get_pos()
                position = get_board_position(pos)
                
                if position is not None and board[position] == " ":
                    board[position] = "X"
                    draw_board(board)
                    
                    # Check for winner or tie
                    result = check_winner(board)
                    if result:
                        if result == "Tie":
                            display_message("It's a tie! Click to play again.", RED)
                        else:
                            display_message(f"{result} wins! Click to play again.", RED)
                        # Wait for click to restart
                        waiting = True
                        while waiting:
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if e.type == pygame.MOUSEBUTTONDOWN:
                                    waiting = False
                                    board = [" "] * 9
                                    current_player = "X"
                                    draw_board(board)
                                    display_message("Your turn (X). Click on a square.")
                        continue
                    
                    # Switch to computer's turn
                    current_player = "O"
                    display_message("Computer's turn...")
                    
                    # Add small delay so player can see their move
                    pygame.time.delay(500)
                    
                    # Computer's turn
                    position = computer_move(board, "O")
                    board[position] = "O"
                    draw_board(board)
                    
                    # Check for winner or tie
                    result = check_winner(board)
                    if result:
                        if result == "Tie":
                            display_message("It's a tie! Click to play again.", RED)
                        else:
                            display_message(f"{result} wins! Click to play again.", RED)
                        # Wait for click to restart
                        waiting = True
                        while waiting:
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if e.type == pygame.MOUSEBUTTONDOWN:
                                    waiting = False
                                    board = [" "] * 9
                                    current_player = "X"
                                    draw_board(board)
                                    display_message("Your turn (X). Click on a square.")
                        continue
                    
                    # Switch back to user's turn
                    current_player = "X"
                    display_message("Your turn (X). Click on a square.")

# Start the game
if __name__ == "__main__":
    play_game()