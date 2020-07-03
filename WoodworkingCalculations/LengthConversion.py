def ConvertInchestoMM(LengthInInches):

    LengthInMM = LengthInInches * 25.4

    return LengthInMM

def ConvertMMtoInches(LengthInMM):

    LengthInInches = LengthInMM / 25.4

    return LengthInInches


if __name__ == '__main__':

    Result = ConvertInchestoMM(1).__round__(7)
    print(Result)

    Result = ConvertInchestoMM(3.0625).__round__(7)
    print(Result)

    Result = ConvertMMtoInches(1).__round__(7)
    print(Result)

    Result = ConvertMMtoInches(47).__round__(7)
    print(Result)

