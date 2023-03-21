# Tic Tac Toe Game1

board = [' ' for i in range(9)]  # initialize the board with empty spaces

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def check_win(player):
    # check rows
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player):
        return True
    # check columns
    if (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player):
        return True
    # check diagonals
    if (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    return False

def play_game():
    print('Welcome to Tic Tac Toe!')
    player = 'X'
    while True:
        print_board()
        position = int(input('Player ' + player + ', choose a position (1-9): '))
        if board[position - 1] == ' ':
            board[position - 1] = player
            if check_win(player):
                print_board()
                print('Congratulations, Player ' + player + ' wins!')
                break
            if ' ' not in board:
                print_board()
                print('It is a tie!')
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print('Position already occupied, try again.')

play_game()
