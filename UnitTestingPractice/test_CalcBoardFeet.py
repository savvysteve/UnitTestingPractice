import unittest
from CalcBoardFeet import CalcBoardFeet

class CalcBoardFeetTest(unittest.TestCase):
    
    def testLengthInFeetExample1(self):
        BoardFeet = CalcBoardFeet(8,1,LengthInFeet=8)
        self.assertEqual(BoardFeet, 5.333333333333333)

    def testLengthInInchesExample1(self):
        BoardFeet = CalcBoardFeet(8,1,LengthInInches=96)
        self.assertEqual(BoardFeet, 5.333333333333333)
    
    def testLengthInFeetExample2(self):
        BoardFeet = CalcBoardFeet(7,2,LengthInFeet=10)
        self.assertEqual(BoardFeet, 11.666666666666666)

    def testLengthInInchesExample2(self):
        BoardFeet = CalcBoardFeet(7,2,LengthInInches=120)
        self.assertEqual(BoardFeet, 11.666666666666666)

if __name__ == '__main__':
    unittest.main()