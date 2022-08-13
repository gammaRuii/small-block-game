from random import randint

class BoardLogic:
    def __init__(self, size):
        # the core data is an array to save the ball status on the board
        # initially, it is all empty, with all values set to 0
        # the length of the array is size * size, as the
        board = []
        for i in range(size):
            line = []
            for j in range(size):
                line.append(0)
            board.append(line)

        # here we have an initialized all-zero board data 
        self.boardData = board
        self.size = size


    # this function is the response to the action that the player put a ball in a given location
    # what is the logic you can think of?
    def putBallInSpot(self, col, row, ball_val):
        self.boardData[col][row] = ball_val

        '''
        A possible logic flow

        if self.IsValidAction(...) == false :
            throw an exception or return an error to indicate it

        set the corresponding element in the array = ball_val

        Detect if there are any lines, vertical/horizontal/diagonal, containing 5 or more same-value elements.
        If yes, remove them by re-setting these elements to zero.

        if self.IsGameOver(self):
            throw an exception or return an error to indicate it

        return
        '''
        pass

    # this function return the boardData array
    def GetBoardData(self):
        return self.boardData

    # this function check whether the board is in a game-over state
    def IsGameOver(self):
        pass

    # this function detects if there are any lines, vertical/horizontal/diagonal, containing 5 or more same-value elements.

    ## Question: Do you think this function is a good design? Is it efficient for our use case?
    ## can u think of a better one?
    def ClearConnectedLines(self):
        pass

    def determineColRow(self,number,dimension):
        column = number % dimension
        row = int((number-column)/dimension)
        return[row,column]

    def ComputerBalls(self):
        ballsAdded = 0
        while ballsAdded < 3:
            col = randint(0, self.size - 1)
            row = randint(0, self.size - 1)
            if self.boardData[col][row] == 0:
                color = randint(2,9)
                self.boardData[col][row] = color
                ballsAdded += 1


        



