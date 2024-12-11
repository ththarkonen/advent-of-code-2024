from collections import Counter

def parse( line ):

    data = [ int(d) for d in line.split(" ") ]
    return Counter( data )


def operate( stone ):

    if stone == 0: return [1]

    stoneStr = str( stone )
    stoneEngravingLength = len( stoneStr )

    if stoneEngravingLength % 2 == 0:

        midPoint = stoneEngravingLength // 2
        
        leftStone = int( stoneStr[0:midPoint] )
        rightStone = int( stoneStr[midPoint:] )
        return [ leftStone, rightStone]
    
    else: return [ 2024 * stone ]


def blink( stones ):

    newStones = Counter()

    for stone in stones:

        stoneAmount = stones[ stone ]
        nextStones = operate( stone )

        for nextStone in nextStones:
            newStones[ nextStone ] += stoneAmount
        
    return newStones