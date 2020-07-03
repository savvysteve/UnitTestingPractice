import pytest
from WoodworkingCalculations.CalcBoardFeet import CalcBoardFeet


def test_LengthInFeetExample1():
    BoardFeet = CalcBoardFeet(8,1,LengthInFeet=8)
    assert BoardFeet == 5.333333333333333

def test_LengthInInchesExample1():
    BoardFeet = CalcBoardFeet(8,1,LengthInInches=96)
    assert BoardFeet == 5.333333333333333
    
def test_LengthInFeetExample2():
    BoardFeet = CalcBoardFeet(7,2,LengthInFeet=10)
    assert BoardFeet == 11.666666666666666

def test_LengthInInchesExample2():
    BoardFeet = CalcBoardFeet(7,2,LengthInInches=120)
    assert BoardFeet == 11.666666666666666
