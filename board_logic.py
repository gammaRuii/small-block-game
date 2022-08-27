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

    # this function detects if there are any lines, vertical/horizontal/diagonal, containing 5 or more same-value elements.

    ## Question: Do you think this function is a good design? Is it efficient for our use case?
    ## can u think of a better one?
    # def ClearConnectedLines(self):
    #     pass

    def determineColRow(self,number,dimension):
        column = number % dimension
        row = int((number-column)/dimension)
        # row returns position in the row (for example, row = 2 would be the second element in a row)
        # colum returns position in the column (for example, column = 1 would be the first element in a column)
        return[row,column]

    def ComputerBalls(self):
        # ballsAdded = 0
        # while ballsAdded < 3:
        #     col = randint(0, self.size - 1)
        #     row = randint(0, self.size - 1)
        #     if self.boardData[col][row] == 0:
        #         color = randint(2,9)
        #         self.boardData[col][row] = color
        #         ballsAdded += 1
        boxes = min(3, len(self.empty))
        for i in range(boxes):
            box = randint(0,len(self.empty)-1)
            color = randint(2,9)
            self.boardData[self.empty[box][0]][self.empty[box][1]] = color
            self.empty.remove(self.empty[box])
            # print(box, "box")
            # print(self.empty[box])
            self.clearLine((self.empty[box][0], self.empty[box][1]), color)

    def FindEmpty(self):
        for col in range(self.size):
            for row in range(self.size):
                if self.boardData[col][row] == 0:
                    self.empty.append((col,row))

    def RandomColors(self):
        for i in range(3):
            color = randint(2,9)
            self.colors.append(color)

    def ClearColors(self):
        self.colors.clear()

    # def ChainFinder(self, list, number):
    #     cont = 0
    #     maxcont = 0
    #     prev = list[0]
    #     for i in list:
    #         if i == number:
    #             if i != prev:
    #                 cont = 1
    #             else:
    #                 cont += 1
    #             maxcont = max(maxcont, cont)
    #         prev = i
    #     return maxcont

    def GenerateChainList(self, orientation, location):
        # orientation should be passed in as:
        # h - horizontal
        # v - vertical
        # d - diagonal in positive direction, y = x
        # rd - reverse diagonal, y = -x
        passedList = []
        if orientation == "h":
            for i in range(self.size):
                # print("\n ****************************\n")
                # print(location)
                # print("infinite h fehmobe")
                passedList.append((location[0], i))
        if orientation == "v":
            column = []
            for i in range(self.size):
                column.append((i, location[1]))
            passedList = column.copy()
        if orientation == "d":
            diagStart = (location[0],location[1])
            colors = []
            # print(self.boardData)
            # while diagStart[0] > 0 and diagStart[1] > 0:
            side = min(diagStart[0],diagStart[1])
            diagStart = (diagStart[0] - side,diagStart[1] - side)
            # print("ball")
            # print(diagStart)
            colorloc = diagStart
            for i in range(self.size - max(diagStart[0], diagStart[1])):
                # print(colorloc)
                # print(i)
                # print(self.boardData[colorloc[0]][colorloc[1]])
                colors.append(colorloc)
                colorloc = (colorloc[0] + 1, colorloc[1] + 1)
            passedList = colors.copy()
        if orientation == "rd":
            diagStart = (location[0], location[1])
            colors = []
            # print(diagStart)
            side = min(diagStart[0], self.size - diagStart[1] - 1)
            # while diagStart[0] > 0 and diagStart[1] < self.size:
            diagStart = (diagStart[0] - side, diagStart[1] + side)
            # print("ball")
            # print(diagStart)
            colorloc = diagStart
            # print(colorloc)
            for i in range(diagStart[0],diagStart[1]+1):
                # print(colorloc)
                # print(i)
                # print(self.boardData[colorloc[0]][colorloc[1]])
                colors.append(colorloc)

                colorloc = (colorloc[0] + 1, colorloc[1] - 1)
                # print(colorloc)
            passedList = colors.copy()
        return passedList

    def FindChain(self, passedList, ballColor):
        # print("\n ~~~~~~~~~~~~~~~~~~~~~ \n")
        # print(passedList)
        # print(ballColor)
        cont = 0
        maxcont = 0
        # print(passedList)
        # print("\n        j           \n")
        # print(self.boardData[passedList[0][0]][passedList[0][1]])
        prev = self.boardData[passedList[0][0]][passedList[0][1]]
        # print(passedList[0])
        # print(passedList)
        start_point = 0
        best_start_point = 0

        for i in range(len(passedList)):
            curColor = self.boardData[passedList[i][0]][passedList[i][1]]
            if curColor == ballColor:
                if curColor != prev:
                    # locations.append(passedList[i])
                    cont = 1
                    start_point = i
                else:
                    cont += 1

                    # if cont == 2:
                    #     locations.append(passedList[i-1])
                    # locations.append(passedList[i])

                if cont > maxcont:
                    maxcont = cont
                    best_start_point = start_point
                #maxcont = max(maxcont, cont)
                # print(passedList[i])
            prev = curColor
        #print(locations)
        #if len(locations) >= self.connected_length:
            #
        # print(maxcont)
        if maxcont >= self.connected_length:
            if self.connected >= 5:
                self.connected += maxcont - 1
                return passedList[best_start_point:best_start_point + maxcont]
            self.connected += maxcont
            # print(self.connected)
            return passedList[best_start_point:best_start_point + maxcont]
            #return locations


    def clearLine(self, location, ballColor):
        print("\n ~~~~~~~~~~~~~~~~~~ \n")
        self.connected = 0
        allLocations = []
        toBeRemoved = []
        for i in self.orientations:
            chainList = self.GenerateChainList(i, location)
            print(location)
            print(i)
            print(chainList)
            allLocations.append(chainList)
            print(allLocations)
            # print(i)
            # print(allLocations)
        for i in range(4):
            # print(self.FindChain(allLocations[i], ballColor))
            # print("\n --------------------------- \n")
            # print(allLocations)
            print("\ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n")

            removeChain = self.FindChain(allLocations[i], ballColor)
            print(allLocations[i])
            print(ballColor)
            print(removeChain)

            if removeChain != None:
                toBeRemoved.append(removeChain)

        print("\n ===================================== \n")
        print(toBeRemoved)

        for i in range(len(toBeRemoved)):
            for j in range(len(toBeRemoved[i])):
                # print(toBeRemoved)
                self.putBallInSpot(toBeRemoved[i][j][0], toBeRemoved[i][j][1], 0)
                self.empty.append(toBeRemoved[i][j])
        self.score += self.connected




