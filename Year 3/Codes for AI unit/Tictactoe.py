import math
#initialize empty board
board = [''for _ in range(9)]
#Display board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|' + '|'.join(row) + '|')
#check winner
def check_winner(brd,player):
    win_positions  = [
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8], #columns
        [0,4,8],[2,4,6] #diagonals
    ]
    return any(all(brd[i] == player for i in combo)for combo in win_positions)
#check for draw
def is_draw(brd):
    return '' not in brd
#minimax algorithm
def minimax(brd,depth,is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if is_draw(brd):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == '':
                brd[i]  = 'O'
                score = minimax(brd,depth+1,False)
                brd[i] = ''
                best_score = max(score,best_score)
                return best_score
    else:
        best_score  = math.inf
        for i in range(9):
            if brd[i] == '':
                brd[i]  = 'X'
                score = minimax(brd,depth+1,True)
                brd[i] = ''
                best_score = min(score,best_score)
                return best_score
#AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == '':
            board[i]  = 'O'
            score = minimax(board,0,False)
            board[i]  = ''
            if score > best_score:
                best_score  = score
                move = i
    board[move] = 'O'
#Main game loop
def play_game():
    print("You are 'X', AI is 'O'. Enter positions 1-9.")
    print_board()
    while True:
        #Player move
        move = int(input("Enter your move(1-9):")) - 1
        if board[move]!= '':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'
        print_board()
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        #AI move
        print("AI's move:")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break 
#Start the game
if __name__ == "__main__":
    play_game()