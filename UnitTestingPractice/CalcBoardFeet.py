def CalcBoardFeet(WidthInInches, ThicknesInInches, LengthInInches=0, LengthInFeet=0): 

    if LengthInInches > 0:  
        BoardFeet = (WidthInInches * LengthInInches * ThicknesInInches) / 144
    elif LengthInFeet > 0:
        BoardFeet = (WidthInInches * LengthInFeet * ThicknesInInches) / 12
    else:
       raise ValueError("Either LengthInInches or LengthInFeet must be greater than zero.")

    return BoardFeet




if __name__ == '__main__':

    BoardFeet = CalcBoardFeet(8,1,LengthInFeet=8)
    print(BoardFeet)

    BoardFeet = CalcBoardFeet(7,2,LengthInInches=120)
    print(BoardFeet)