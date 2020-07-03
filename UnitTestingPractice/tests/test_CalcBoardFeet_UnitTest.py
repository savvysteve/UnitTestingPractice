import unittest
from CalcBoardFeet.CalcBoardFeet import CalcBoardFeet
    
def test_LengthInFeetExample1():
    BoardFeet = CalcBoardFeet(8,1,LengthInFeet=8)
    assert BoardFeet == 5.333333333333333

def testLengthInInchesExample1():
    BoardFeet = CalcBoardFeet(8,1,LengthInInches=96)
    assert BoardFeet == 5.333333333333333
    
def testLengthInFeetExample2():
    BoardFeet = CalcBoardFeet(7,2,LengthInFeet=10)
    assert BoardFeet == 11.666666666666666

def testLengthInInchesExample2():
    BoardFeet = CalcBoardFeet(7,2,LengthInInches=120)
    assert BoardFeet == 11.666666666666666
