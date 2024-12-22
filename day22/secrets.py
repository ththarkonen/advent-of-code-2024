import numpy as np
from collections import Counter

def parse( lines ):

    secretNumbers = []

    for line in lines:

        secretNumber = line.replace("\n","")
        secretNumber = int( secretNumber )

        secretNumbers.append( secretNumber )

    return secretNumbers


def iterate( numbers, n):

    iteratedNumbers = []
    pricesList = []

    for number in numbers:

        prices = [ number % 10 ]

        for __ in range( n ):

            number = ( 64 * number) ^ number 
            number = number % 16777216
            number = ( number // 32 ) ^ number
            number = ( 2048 * number ) ^ number
            number = number % 16777216

            price = number % 10
            prices.append( price )

        pricesList.append( prices.copy() )
        iteratedNumbers.append( number )
        
    return iteratedNumbers, pricesList


def addBananaData( prices, priceChanges):

    data = Counter()
    nChanges = len( priceChanges )

    for ii in range( nChanges - 3):

        start = ii
        stop = ii + 4
        sequence = tuple( priceChanges[start:stop].tolist() )

        if sequence not in data:
            data[ sequence ] += prices[ stop ]

    return data

def getBananas( pricesList ):

    priceChangesList = []
    bananaData = {}

    for prices in pricesList:

        priceChanges = np.diff( prices )
        priceChangesList.append( priceChanges.copy() )

    bananaData = Counter()

    for prices, priceChanges in zip( pricesList, priceChangesList):
        bananaData += addBananaData( prices, priceChanges)

    return bananaData
