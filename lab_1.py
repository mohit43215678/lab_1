def initialize_board():
    return [[' ']*3 for _ in range(3)]

def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-'*5)

def get_player_move():
    row = int(input("Enter the row (0, 1, or 2): "))
    col = int(input("Enter the column (0, 1, or 2): "))
    return row, col

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, player, row, col):
    board[row][col] = player

def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    game_board = initialize_board()
    current_player = 'X'

    while True:
        display_board(game_board)
        player_move = get_player_move()

        if is_valid_move(game_board, *player_move):
            make_move(game_board, current_player, *player_move)

            if check_winner(game_board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(game_board):
                print("The game ends in a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

play_game()
