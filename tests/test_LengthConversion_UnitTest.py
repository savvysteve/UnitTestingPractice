import pytest
from WoodworkingCalculations.LengthConversion import *


def test_ConvertInchestoMMExample1():
    Result = ConvertInchestoMM(1).__round__(7)
    assert Result == 25.4

def test_ConvertInchestoMMExample2():
    Result = ConvertInchestoMM(3.0625).__round__(7)
    assert Result == 77.7875

def test_ConvertInchestoMMExample3():
    Result = ConvertInchestoMM(7.775).__round__(7)
    assert Result == 197.485

def test_ConvertMMtoInchesExample1():
    Result = ConvertMMtoInches(1).__round__(7)
    assert Result == 0.0393701

def test_ConvertMMtoInchesExample2():
    Result = ConvertMMtoInches(47).__round__(7)
    assert Result == 1.8503937

def test_ConvertMMtoInchesExample3():
    Result = ConvertMMtoInches(7.775).__round__(8)
    assert Result == 0.30610236


