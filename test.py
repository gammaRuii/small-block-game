import unittest 

def ChainFinder(list, number):
    cont = 0
    maxcont = 0
    prev = list[0]
    for i in list:
        if i == number:
            if i != prev:
                cont = 1
        if i == prev == 1:
            cont += 1
        maxcont = max(maxcont,cont)
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
 

if __name__ == '__main__':
    unittest.main()
