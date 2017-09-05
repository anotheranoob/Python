import random
wordsUsed=[]
inFile= open('C:/Users/kevin/Documents/python_kevin/wordlist.txt','r')
fileString=inFile.read()
inFile.close()
fileString=fileString.split()
def convert_linear(index):
    '''converts a linear list index into nested list indexes'''
    column=index%4
    row=index//4
    return(column, row)
def convert_nested(column, row):
    '''converts nested list indexes into a linear list index'''
    i=column+row*4
    return(i)
def roll(sides):
    '''returns a roll of a die that has sides sides assuming sides is a list'''
    side=random.randrange(6)
    return sides[side]
def scramble_grid(grid):
    """scrambles a grid"""
    return(random.shuffle(grid))
def neighbors(index, grid):
    '''takes a index in a grid and returns all neighboring indexes'''
    initialIndexes = convert_linear(int(index))
    endLetters=[]
#    print(initialIndexes)
    for i in [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1, 1]]:
        
        column=i[0]
        row=i[1]
        column+=initialIndexes[0]
        row+=initialIndexes[1]
#        print(column, row)
        if column>3 or row>3 or column<0 or row<0:
            pass
        else:
            if 0<=convert_nested(column,row)<16:
                endLetters.append(convert_nested(column,row))
    return endLetters
def is_in_grid(word, grid):
    """First part of a 2 part search to see if word is in grid"""
    wordLength=len(word)
    letterList=[]
    isIn=False
    for letter in word:
        letterList.append(letter)
    for i in range(16):
        if letterList[0].lower()==grid[i].lower():
            if recurse(wordLength, letterList, 0, grid, i, [i])==True:
                isIn=True
    return isIn

def recurse(wordLength, letterList, currentLetterInWord, grid, currentLetter, positionsUsed):
    "2nd part of a 2 part search to see if a word is in a grid"
    #print('positionsUsed = '+ str(positionsUsed))
    if currentLetterInWord+1 == wordLength:
        return(True)
        
    if currentLetterInWord+1 < wordLength:
        for j in neighbors(currentLetter, grid):
            #print("neighbor of "+str(currentLetter)+" ="+str(j))
            if grid[j].lower()==letterList[currentLetterInWord+1].lower():
                if j not in positionsUsed:
                    positionsUsed.append(j)
                    if recurse(wordLength, letterList, currentLetterInWord+1, grid, j, positionsUsed) :
                        return (True)
    else:
        return(False)
def is_word(word):
    '''Returns whether or not word is in the dictionary'''
    return(word.lower() in fileString or word.upper() in fileString)
grid=["O", "E", "B", "I", "T", "A", "N", "T", "L", "O", "R", "T", "G", "X", "N", "A"]
dice=[["A","A","E","E","G","N"],["E","L","R","T","T","Y"], ["A","O","O","T","T","W"],["A","B","B","J","O","O"],
["E","H","R","T","V","W"], ["C","I","M","O","T","U"], ["D","I","S","T","T","Y"], ["E","I","O","S","S","T"],
["D","E","L","R","V","Y"], ["A","C","H","O","P","S"], ["H","I","M","N","Q","U"], ["E","E","I","N","S","U"],
["E","E","G","H","N","W"], ["A","F","F","K","P","S"], ["H","L","N","N","R","Z"], ["D","E","L","I","R","X"]]
totalScore=0
scoreList=[]
wordList=[]
def start_game():
    """Starts up the game by generating grid. Then it initializes the rest of the game"""
    global grid
    grid=[]
    for i in dice:
        grid.append(roll(i))
    scramble_grid(grid)
    main_game()
def main_game():
    """actually runs the game"""
    global totalScore
    global scoreList
    global wordList
    global wordsUsed
    while True:
        score = ask_for_word()
        if score== "game over":
            break
        elif score == "invalid":
            pass
        else:
            totalScore+=int(score[1])
            scoreList.append(score[1])
            wordList.append(score[0])
            wordsUsed.append(score[0])
    game_over()
def score(word):
    "scores a word"
    if len(word)<3:
        return 0
    elif len(word)==3:
        return 1
    elif len(word)==4:
        return 1
    elif len(word)==5:
        return 2
    elif len(word)==6:
        return 3
    elif len(word)==7:
        return 5
    elif len(word)>=8:
        return 11
def ask_for_word():
    """asks user for word, tells user whether its valid, and returns score to game"""
    global wordsUsed
    for i in range(4):
        for n in range(4):
            print(grid[convert_nested(n,i)], end="    ")
        print("\n")
    word=input("Enter your word (leave blank to quit):")
    if word=="":
        return("game over")
    else:
        if is_in_grid(word, grid) and is_word(word):
            if word in wordsUsed:
                print(word + " has already been used")
                return "invalid"
            else:
                print(word + " is a valid word")
                return [word, score(word)]
        elif not (is_in_grid(word, grid)) and not (is_word(word)):
            print(word + " is not in the dictionary or in the grid")
            return "invalid"
        elif not (is_in_grid(word, grid)):
            print(word + " is not in the grid")
            return "invalid"
        elif not (is_word(word)):
            print(word + " is not a word")
            return "invalid"   
def game_over():
    print("Here's your score:")
    for i in range(len(scoreList)):
        print(wordList[i] + " scores " + str(scoreList[i]))
    print("your total score was " + str(totalScore))
start_game()
#
