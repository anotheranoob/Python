from ticTacToeAI import *
import time
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
def checkBoardFull(board):
    '''returns a boolean'''
    for x in range(3):
        for y in range(3):
            if (board[x][y] == " "):
                return False
    return True
def turn(player, board):
    '''the game function'''
    if checkThreeInRow(board,player):
        print(player + " wins!")
        return "game over"
    if checkBoardFull(board):
        print('tie')
        return "tie"
    else:
        spotX=input("Which x do you want to go to "+player.upper()+"?")
        spotY=input("Which y do you want to go to "+player.upper()+"?")
        if board[int(spotX)-1][int(spotY)-1]==' ':
            playSpot(player,int(spotX)-1,int(spotY)-1)
            if checkThreeInRow(board,player):
                return "game over"
        else:
            while not board[int(spotX)-1][int(spotY)-1]==' ':
                print("That place is already taken")
                spotX=input("Which x do you want to go to "+player.upper()+"?")
                spotY=input("Which y do you want to go to "+player.upper()+"?")
            playSpot(player,int(spotX)-1,int(spotY)-1)
            if checkThreeInRow(board,player):
                return "game over"
def playSpot(tileName,spotX,spotY):
    board[spotX][spotY] = tileName
def getSpot(spotX,spotY):
    return board[spotX][spotY]
def printBoard(board):
    print("--------")
    print("3|"+board[0][2]+"|"+board[1][2]+"|"+board[2][2]+"|")
    print("--------")
    print("2|"+board[0][1]+"|"+board[1][1]+"|"+board[2][1]+"|")
    print("--------")
    print("1|"+board[0][0]+"|"+board[1][0]+"|"+board[2][0]+"|")
    print("--------")
    print("  1 2 3")
def checkThreeInRow(board, player):
    if board[0][0]==board[0][1]==board[0][2]==player:
        return True
    if board[1][0]==board[1][1]==board[1][2]==player:
        return True
    if board[2][0]==board[2][1]==board[2][2]==player:
        return True
    if board[0][0]==board[1][0]==board[2][0]==player:
        return True
    if board[0][1]==board[1][1]==board[2][1]==player:
        return True
    if board[0][2]==board[1][2]==board[2][2]==player:
        return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        return True
    if board[2][0]==board[1][1]==board[0][2]==player:
        return True
    else:
        return False
def logic1(board):
    while (True):
        player = "x"
        printBoard(board)
        if turn(player, board)=="game over":
            print(player + " wins!")
            break
        player = "y"
        printBoard(board)
        if turn(player, board)=="game over":
            print(player + " wins!")
            break
        if checkBoardFull(board):
            print("Its a tie!")
            time.sleep(3)
            return "tie"
def logic2(board):
    while (True):
        player= "x"
        printBoard(board)
        if turn(player, board)=="game over":
            print("You win!")
            time.sleep(3)
            break
        if checkBoardFull(board):
            print("Its a tie!")
            time.sleep(3)
            return "tie"
        (x,y)=AI_move(board)
        print(x,y)
        playSpot("o",x,y)
        if checkThreeInRow(board,"o"):
            printBoard(board)
            print("The computer wins!")
            time.sleep(3)
            return "game over"
while True:
    gameMode=input("Do you want to play with one person or two people?")
    while not(gameMode.lower()=="one person" or gameMode.lower()=="two people"):
        gameMode=input("Please say \"one person\" or \"two people\"")
    if gameMode=="one person":
        logic2(board)
    elif gameMode=="two people":
        logic1(board)
