import random
def AI_move(board):
    if check_for_win_move('o', board)!=False:
        (ox,oy)=check_for_win_move('o',board)
    if check_for_win_move("x", board)!=False:
        (xx,xy)=check_for_win_move('x',board)
    if check_for_win_move('o',board)!=False and board[ox][oy]==' ':
        return ox,oy
    elif check_for_win_move('x',board)!=False and board[xx][xy]==' ':
        return xx,xy
    elif checkBoardEmpty(board):
        return(0,2)
    else:
        (x,y)=(random.randint(0,2),random.randint(0,2))
        while board[x][y]!=' ':
            (x,y)=(random.randint(0,2),random.randint(0,2))
        return(x,y)
def check_for_win_move(player,board):
    for n in range(0,3):
        if board[n][2]==player and board[n][1]==player:
            return(n,0)
        if board[n][0]==player and board[n][1]==player:
            return(n,2)
        if board[0][n]==player and board[1][n]==player:
            return(2,n)
        if board[2][n]==player and board[1][n]==player:
            return(0,n)
        if board[2][n]==player and board[0][n]==player:
            return(1,n)
        if board[n][2]==player and board[n][0]==player:
            return(n,1)
    if board[1][1]==player:
        if board[0][0]==player:
            return(2,2)
        if board[2][2]==player:
            return(0,0)
        if board[0][2]==player:
            return(2,0)
        if board[2][0]==player:
            return(0,2)
    if board[0][0]==player:
        if board[2][2]==player:
            return(1,1)
    if board[2][2]==player:
        if board[0][0]==player:
            return(1,1)
    if board[0][2]==player:
        if board[2][0]==player:
            return(1,1)
    if board[2][0]==player:
        if board[0][2]==player:
            return(1,1)
    return False
def checkBoardEmpty(board):
    '''returns a boolean'''
    for x in range(3):
        for y in range(3):
            if (board[x][y] != " "):
                return False
    return True
