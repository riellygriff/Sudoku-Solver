board = [
    [7, 0, 0, 0, 0, 4, 8, 0, 0],
    [0, 0, 0, 0, 0, 5, 4, 0, 0],
    [0, 0, 9, 0, 0, 0, 7, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 9, 0],
    [8, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 0, 0],
    [0, 3, 0, 0, 5, 0, 0, 0, 1],
    [0, 1, 0, 2, 0, 0, 0, 7, 5],
    [0, 0, 0, 1, 4, 3, 0, 0, 0]
]


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(str(board[row][col]) + ' ', end='')
            if col % 3 == 2:
                print('|', end='')
        if row % 3 == 2:
            print('')
            print('- - - - - - - - - - -')
        else:
            print('')


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return [row, col]

def valid(board,pos,num):
    for i in range(len(board)):
        if num == board[pos[0]][i]and pos[1] != i:
            return False
        if num == board[i][pos[1]] and pos[0] != i:
            return False
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for row in range(box_x*3, box_x*3+3):
        for col in range(box_y*3, box_y*3+3):
            if num == board[row][col] and row != pos[0] and col != pos[1]:
                return False
    return True

def solve(board):
    space = find_empty(board)
    if not space:
        return True
    for i in range(1,len(board) + 1):
        if valid(board, space, i):
            board[space[0]][space[1]] = i
            if solve(board):
                return True
            board[space[0]][space[1]] = 0

print_board(board)
print('-------------------')
solve(board)

print_board(board)