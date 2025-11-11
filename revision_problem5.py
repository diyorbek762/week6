def check_winner(board):
    for i in range(3):
        if board[i][0]!=0 and board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            return board[i][0]
    for j in range(3):
        if board[0][j]!=0 and board[0][j]==board[1][j] and board[1][j]==board[2][j]:
            return board[0][j]
    if board[0][0]!=0 and board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        return board[0][0]
    if board[0][2]!=0 and board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        return board[0][0]
    return 'No Winner'
    


    








board_x_wins_row = [
	['X', 'X', 'X'],
	['O', ' ', 'O'],
	[' ', 'O', ' ']
]
print(check_winner(board_x_wins_row))
# Case 2: 'O' wins on the middle column
board_o_wins_col = [
	['X', 'O', 'X'],
	['X', 'O', ' '],
	[' ', 'O', ' ']
]
# Expected Output: 'O'
print(check_winner(board_o_wins_col))
# Case 3: 'X' wins on a diagonal
board_x_wins_diag = [
	['X', 'O', 'O'],
	[' ', 'X', ' '],
	['O', ' ', 'X']
]
# Expected Output: 'X'
print(check_winner(board_x_wins_diag))
# Case 4: No winner
board_no_winner = [
	['X', 'O', 'X'],
	['X', 'O', 'O'],
	['O', 'X', 'X']
]
# Expected Output: 'No Winner'
print(check_winner(board_no_winner))