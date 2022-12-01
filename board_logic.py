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
        self.empty = []
        self.colors = []
        self.score = 0
        self.connected = 0
        self.connected_length = 5
        self.orientations = ['h','v','d','rd']


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
        if len(self.empty) == 0:
            return True
        return False

    def determineColRow(self,number,dimension):
        column = number % dimension
        row = int((number-column)/dimension)
        # row returns position in the row (for example, row = 2 would be the second element in a row)
        # colum returns position in the column (for example, column = 1 would be the first element in a column)
        return[row,column]

    def ComputerBalls(self):
        boxes = min(3, len(self.empty))
        for i in range(boxes):
            box = randint(0,len(self.empty)-1)
            color = randint(1,6)
            self.boardData[self.empty[box][0]][self.empty[box][1]] = color
            self.clearLine((self.empty[box][0], self.empty[box][1]), color)
            self.empty.remove(self.empty[box])

    def FindEmpty(self):
        for col in range(self.size):
            for row in range(self.size):
                if self.boardData[col][row] == 0:
                    self.empty.append((col,row))
                    print(self.empty)

    def RandomColors(self):
        for i in range(3):
            color = randint(1,6)
            self.colors.append(color)

    def ClearColors(self):
        self.colors.clear()

    def GenerateChainList(self, orientation, location):
        # orientation should be passed in as:
        # h - horizontal
        # v - vertical
        # d - diagonal in positive direction, y = x
        # rd - reverse diagonal, y = -x
        passedList = []
        if orientation == "h":
            for i in range(self.size):
                passedList.append((location[0], i))
        if orientation == "v":
            column = []
            for i in range(self.size):
                column.append((i, location[1]))
            passedList = column.copy()
        if orientation == "d":
            diagStart = (location[0],location[1])
            colors = []
            side = min(diagStart[0],diagStart[1])
            diagStart = (diagStart[0] - side,diagStart[1] - side)
            colorloc = diagStart
            for i in range(self.size - max(diagStart[0], diagStart[1])):
                colors.append(colorloc)
                colorloc = (colorloc[0] + 1, colorloc[1] + 1)
            passedList = colors.copy()
        if orientation == "rd":
            diagStart = (location[0], location[1])
            colors = []
            side = min(diagStart[0], self.size - diagStart[1] - 1)
            diagStart = (diagStart[0] - side, diagStart[1] + side)
            colorloc = diagStart
            for i in range(diagStart[0],diagStart[1]+1):
                colors.append(colorloc)
                colorloc = (colorloc[0] + 1, colorloc[1] - 1)
            passedList = colors.copy()
        return passedList

    def FindChain(self, passedList, ballColor):
        cont = 0
        maxcont = 0
        prev = self.boardData[passedList[0][0]][passedList[0][1]]
        start_point = 0
        best_start_point = 0
        for i in range(len(passedList)):
            curColor = self.boardData[passedList[i][0]][passedList[i][1]]
            if curColor == ballColor:
                if curColor != prev:
                    cont = 1
                    start_point = i
                else:
                    cont += 1
                if cont > maxcont:
                    maxcont = cont
                    best_start_point = start_point
            prev = curColor
        if maxcont >= self.connected_length:
            if self.connected >= 5:
                self.connected += maxcont - 1
                return passedList[best_start_point:best_start_point + maxcont]
            self.connected += maxcont
            return passedList[best_start_point:best_start_point + maxcont]


    def clearLine(self, location, ballColor):
        self.connected = 0
        allLocations = []
        toBeRemoved = []
        for i in self.orientations:
            chainList = self.GenerateChainList(i, location)
            allLocations.append(chainList)
        for i in range(4):
            removeChain = self.FindChain(allLocations[i], ballColor)
            if removeChain != None:
                toBeRemoved.append(removeChain)
        for i in range(len(toBeRemoved)):
            for j in range(len(toBeRemoved[i])):
                self.putBallInSpot(toBeRemoved[i][j][0], toBeRemoved[i][j][1], 0)
                self.empty.append(toBeRemoved[i][j])
        self.score += self.connected




