import unittest
from board_logic import BoardLogic

def ChainFinder(list, number):
    cont = 0
    maxcont = 0
    prev = list[0]
    for i in list:
        if i == number:
            if i != prev:
                cont = 1
            else:
               cont += 1
            maxcont = max(maxcont, cont)
        prev = i
    return maxcont

class TestChainFinder(unittest.TestCase):

    def test_Chainfinder_OneElement(self):
        number = 1 
        numList = [1]
        self.assertEqual(ChainFinder(numList, number), 1)
 
        numList = [0]
        self.assertEqual(ChainFinder(numList, number), 0)

    def test_Chainfinder_LongSeries(self):
        number = 1 
        numList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,18,19,20]
        self.assertEqual(ChainFinder(numList, number), 1)
 
        numList = [0,1,1,4,5,6,3,4,1,1,1,1,1]
        self.assertEqual(ChainFinder(numList, number), 5)

        numList = [0,1,1,4,5,6,3,4,1,1,1,1,1,0]
        self.assertEqual(ChainFinder(numList, number), 5)

        numList = [1,1,1,1,1,1,1,1,0]
        self.assertEqual(ChainFinder(numList, number), 8)

    def test_Chainfinder_otherNum(self):
        number = 2
        numList = [0,1,2,2,4,5,6,7,8,9,10,11,12,13,14,15,16,1,18,19,20]
        self.assertEqual(ChainFinder(numList, number), 2)

    def test_GenerateChainList(self):
        size = 4
        boardData = BoardLogic(size)

        for i in range(size):
            for j in range(size):
                boardData.putBallInSpot(i, j, i + j )

        # print(boardData.GetBoardData())
        # print(boardData.GenerateChainList("rd", (2, 2)))
        # print("\n ------------------- \n")
        self.assertEqual(boardData.GenerateChainList("h", (1, 1)), [1, 2, 3, 4])
        self.assertEqual(boardData.GenerateChainList("v", (2, 2)), [2, 3, 4, 5])
        self.assertEqual(boardData.GenerateChainList("d", (1, 2)), [1,3,5])
        self.assertEqual(boardData.GenerateChainList("d", (2, 2)), [0,2,4,6])
        self.assertEqual(boardData.GenerateChainList("rd", (1, 1)), [2,2,2])
        self.assertEqual(boardData.GenerateChainList("rd", (1, 2)), [3, 3, 3, 3])
        self.assertEqual(boardData.GenerateChainList("d", (0, 0)), [0,2,4,6])
        self.assertEqual(boardData.GenerateChainList("rd", (0,0)), [0])

if __name__ == '__main__':
    unittest.main()
