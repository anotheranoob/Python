# -----------------------------------
# Classes:
# -----------------------------------
# -CheckerGrid-
#
# --Plan--
# --This will contain the checker pieces and the board
# --It inherits from Canvas
# --Its master will be CheckerFrame
#
# ---No Attributes---
#
# ---No methods---
# -----------------------------------
# -CheckerPiece-
#
# --Plan--
# --Inherits from Canvas
# --This will represent a checker piece
# --Its master will be a CheckerGrid
#
# ---Attributes---
# ---color: Either red or white
# ---selected: Whether or not the piece is selected
# ---position: The coordinates of the piece on the CheckerGrid
# ---pieceLocations:
#
# ---Methods---
# ---__init__: Makes a new piece - mathcomputers
# ---move: Moves the piece to a new location - Bill9000
# ---capture: Moves the piece to a new location, and 'reaches up' to the parent to remove the other piece - mathcomputers
# ---king: If the piece gets to the last row, put an asterik on it - Bill9000
# ---remove: Hides the piece
# ---select: Puts a box around the piece
# ---get_coords: returns a (row, column) coordinate tuple
# ---get_color: returns self.color
#
# -----------------------------------
# -CheckerFrame-
#
# --Plan--
# --This inherits from Frame
# --Its master will be root
# 
# --Attributes--
# --turnLabel: 'Turn' and the border
# --pieceTurnLabel: The piece to specify whose turn it is
#

from tkinter import *
from tkinter import messagebox

class CheckerPiece(Canvas):
    '''Represents a checkers piece'''

    def __init__(self, master, color, position, frozen=False):
        '''CheckerPiece.__init__(master, bg, position, frozen = False) -> CheckerPiece
        creates a new CheckerPiece with color bg'''
        Canvas.__init__(self, width=60, height=60, bg = color)
        self.color = color
        (self.row,self.column) = position
        self.pos = position
        self.master = master
        self.isKing = False
        # the frozen is mainly so that this class can also be used for the checkerFrame's turn indicator
        if not frozen:
            self.bind("<Button-1>", master.get_click)
        # make the piece invisible but not nonexistent so that python doesn't complain about deleting a nonexistent circle
        self.piece = self.create_oval(7, 7, 53, 53, fill = self.color, outline = self.color)

    def king(self):
        '''CheckerPiece.king()
        Kings the piece'''
        self.create_text(30, 35, fill = 'black', font=("Times New Roman", 20), text = '*')
        self.isKing = True

    def remove(self):
        '''CheckerPiece.remove()
        Takes the piece off the grid'''
        squareColor = ['blanched almond', 'green'][(self.pos[0] + self.pos[1]) % 2]
        self.piece = self.create_oval(7, 7, 53, 53, fill = squareColor, outline = squareColor)

    def get_coords(self):
        '''CheckerPiece.get_coords() -> tuple
        Returns the coordinates of the piece as a tuple'''
        return self.pos

    def get_color(self):
        '''CheckerPiece.get_color() -> str
        Returns the color of the piece as a string'''
        return self.color
    
    def change_color(self, number):
        '''0 means red, 1 means white --> changes the color of the piece'''
        self.color=['red', 'white'][number]
        self.piece = self.create_oval(7, 7, 53, 53, fill = self.color, outline = self.color)
    

class CheckerGrid(Frame):
    '''Represents a Checkerboard'''
    
    def __init__(self, master, strgrid):
        '''CheckerGrid() -> CheckerGrid
        creates a checkers grid'''
        # We will make a 480 x 480 grid
        Frame.__init__(self, master)
        row = 1
        column = 1
        self.dictgrid = {}
        self.master=master
        # set up the squares with their backgrounds
        while not (row == 9 and column == 1):
            if column > 8:
                column=2
                row+=1
            elif column==8: 
                self.dictgrid[(row,column)]=CheckerPiece(self, "blanched almond", (row, column))
                column=1
                row+=1
            else:
                self.dictgrid[(row,column)]=CheckerPiece(self, "blanched almond", (row, column))
                column+=2
        row=1
        column=2
        while not(row == 8 and column == 9):
            if column > 8:
                column = 2
                row += 1
            elif column == 8: 
                self.dictgrid[(row,column)]=CheckerPiece(self, "green", (row, column))
                column=1
                row+=1
            else:
                self.dictgrid[(row,column)] = CheckerPiece(self, "green", (row, column))
                column += 2        
        for i in self.dictgrid:
            (row, column) = i
            self.dictgrid[i].grid(row = row, column = column)
        # grid
        self.grid()
        # use this to update the board so that there are pieces on it
        self.update_board(strgrid)

    def get_click(self, event):
        #this just calls up to the checkerframe
        self.master.get_click(event)

    def update_board(self, strgrid):
        '''CheckerGrid.update_board(dictgrid)
        takes a strgrid and uses it to update the dictgrid'''
        for i in strgrid:
            if strgrid[i] == "":
                self.dictgrid[i].remove()
            elif "*" in strgrid[i]:
                self.dictgrid[i].change_color(self.get_number(strgrid[i][0]))
                self.dictgrid[i].king()
                print("KING")
            else:
                self.dictgrid[i].change_color(self.get_number(strgrid[i]))
                
    def get_color(self, number):
        '''CheckerGrid.get_color(number) -> str
        returns whose turn it is as a string'''
        return ['red', 'white'][number]
    
    def get_number(self, color):
        '''CheckerGrid.get_number(color) -> int
        returns whose turn it is as an int'''
        if color == 'r':
            return 0
        if color == 'w':
            return 1

class CheckerFrame(Frame):
    '''Does the thinking for checkers'''
    
    def __init__(self, master):
        '''CheckerFrame.__init__(master)
        creates a new CheckerFrame'''
        self.master = master
        Frame.__init__(self, master)
        self.grid()
        self.dictgrid= {}
        #f irst we make dictgrid have all the necessary keys in it
        for row in range(1,9):
            for column in range(1,9):
                self.dictgrid[(row,column)] = ""
        row = 1
        column = 2
        # now we set up all the pieces inside of it
        # first we do red
        while not(row == 4 and column == 1):
            if column > 8:
                column = 2
                row += 1
            elif column == 8: 
                self.dictgrid[(row, column)] = "r"
                column = 1
                row += 1
            else:
                self.dictgrid[(row, column)] = "r"
                column += 2
        # now we do white
        row = 6
        column = 1
        while not (row == 8 and column == 9):
            if column > 8:
                column = 2
                row += 1
            elif column == 8: 
                self.dictgrid[(row, column)] = "w"
                column = 1
                row += 1
            else:
                self.dictgrid[(row, column)] = "w"
                column += 2
        self.tkgrid = CheckerGrid(self, self.dictgrid)
        self.turnIndicator = CheckerPiece(self, "grey", (9,3), frozen=True)
        self.turnIndicator.change_color(0)
        self.turnIndicator.grid(row=9, column = 0, columnspan = 9)
        self.currentTurn = 0
        self.lastpos = None
        # we also need an attribute saying whether we are already in a jump
        self.injump = False
        # we also need an attribute for where the first click was located
        self.firstClick = False
        self.firstClickPos = None
        
    def get_color(self, number):
        '''CheckerFrame.get_color(number) -> str
        returns whose turn it is as a string'''
        return ['r', 'w'][number]
    
    def get_number(self, color):
        '''CheckerFrame.get_number(color) -> int
        returns whose turn it is as an int'''
        if color == 'r':
            return 0
        if color == 'w':
            return 1
        if color == "r*":
            return 2
        if color == "w*":
            return 3
        
    def validate_move(self, startpos, endpos):
        '''CheckerFrame.validate_move(startpos, endpos) -> bool
        this is the function that checkergrid calls after a player tries to make a move. it validates the move based off of self.dictgrid,
        then calls methods on the checkergrid to make the move if the move is valid'''
        # First we unpack the startpos and endpos tuples
        (startRow, startCol) = startpos
        (endRow, endCol) = endpos
        # Now we see if this is jump and whether it is a valid jump in the case that it is a jump
        if (startRow-endRow == 2 * (self.currentTurn*2 - 1) or ("*" in self.dictgrid[startpos] and abs(startRow-endRow) == 2)) \
           and abs(startCol - endCol) == 2 and (startpos == self.lastpos or not (self.injump)):
            if self.dictgrid[(endRow, endCol)] != "" and self.dictgrid[(startRow - (startRow - endRow)/2, startCol - (startCol - endCol)/2)] != self.get_color(1-self.currentTurn):
                # this means that we are trying to jump onto a different piece which is illegal and jump over a nonexisting piece
                self.errorMessage.set("You cannot make that jump because you can't jump onto a different piece and there is no piece in the way")
            elif self.dictgrid[(endRow, endCol)] != "":
                # this means that we are trying to jump onto a different piece which is illegal
                messagebox.showerror.set('Checkers', "You cannot make that jump because you can't jump onto a different piece", parent = self)
            elif self.dictgrid[(startRow-(startRow-endRow)/2,startCol-(startCol-endCol)/2)] != self.get_color(1-self.currentTurn):
                # this is when we are trying to jump over a piece that isn't there
                messagebox.showerror('Checkers', "You cannot make that jump because there is no piece in the way", parent = self)
            else:
                # it is a perfectly legal jump so now we have to see if we can make a second jump or if we have to king the piece.
                self.dictgrid[(startRow-(startRow-endRow)/2,startCol-(startCol-endCol)/2)]=""
                self.dictgrid[endpos]=self.dictgrid[startpos]
                self.dictgrid[startpos] = ""
                if endRow==8:
                    #this means we have to king the piece
                    self.dictgrid[endpos]+="*"
                elif self.can_jump(endpos):
                    self.injump = True
                    messagebox.showerror('Checkers', "You must continue your jump", parent = self)
                    self.lastpos = endpos
                    self.update_display()
                else:
                    self.currentTurn = 1-self.currentTurn
                    self.update_display()
        else:
            # this means that the move they gave us wasn't a jump so we now have to do two things
            # First of all, we must check to make sure that the move is legal and second of all we must check to see if there is a possible jump on the board
            if (startRow-endRow == (self.currentTurn*2 - 1) or ("*" in self.dictgrid[startpos])) and abs(startCol-endCol)==1 and self.dictgrid[endpos]=="":
                # this means that the move is legal, now we have to check to see if there is a jump possible
                for i in self.dictgrid:
                    if self.dictgrid[i] == self.get_color(self.currentTurn) and self.can_jump(i):
                        messagebox.showerror('Checkers', "You must make a jump", parent = self)
                        break
                else:
                    self.dictgrid[endpos] = self.dictgrid[startpos]
                    self.dictgrid[startpos] = "" # remove the piece
                    self.currentTurn = 1 - self.currentTurn
                    self.update_display()
                    if endRow==8:
                        #this means we have to king the piece
                        self.dictgrid[endpos]+="*"
                        print("KING")
            else:
                messagebox.showerror('Checkers', "That is an illegal move", parent = self)
                
    def can_jump(self, pos):
        '''CheckerFrame.can_jump(pos) -> bool
        (row,column) denotes the position of a piece. this returns a boolean.'''
        pieceColor = self.dictgrid[pos]
        if pieceColor == "":
            return False
        (posRow,posCol)=pos
        # now we check for any pieces that are diagonal to the starting piece that have the opposite color
        if "*" in pieceColor:
            possibleRows=[-1,1]
        else:
            possibleRows=[-1*(self.get_number(pieceColor)*2-1)]
        for i in possibleRows:
            for x in [-1, 1]:
                try:
                    if self.dictgrid[(posRow+i),(posCol+x)] == self.get_color(1-self.get_number(pieceColor)) and self.dictgrid[(posRow+2*i),(posCol+2*x)] == "":
                        return True
                except KeyError:
                    pass
        return False

    def update_display(self):
        '''CheckerFrame.update_display()
        updates the display'''
        self.tkgrid.update_board(self.dictgrid)
        self.turnIndicator.change_color(self.currentTurn)
        
    def get_click(self, event):
        '''CheckerFrame.get_click(event)
        this just handles knowing when to tell validate_move to validate moves'''
        if self.firstClick:
            self.validate_move(self.firstClickPos, event.widget.get_coords())
            self.firstClick=False
        else:
            if not (self.get_color(self.currentTurn) in self.dictgrid[event.widget.get_coords()]):
                pass
            else:
                self.firstClick = True
                self.firstClickPos = event.widget.get_coords()
                
root = Tk()
root.title('Checkers')
checkerTest = CheckerFrame(root)
root.mainloop()
