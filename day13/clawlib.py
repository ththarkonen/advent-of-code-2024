import numpy as np

def parse( fileContent ):

    games = []
    gamesStrings = fileContent.split("\n\n")

    for gameStr in gamesStrings:

        gameStr = gameStr.replace("+", " ")
        gameStr = gameStr.replace("=", " ")
        gameStr = gameStr.replace("\n", " ")
        gameStr = gameStr.replace(",", "")
        gameStr = gameStr.split(" ")

        game = {}
        game["x_a"] = int( gameStr[3] )
        game["y_a"] = int( gameStr[5] )

        game["x_b"] = int( gameStr[9] )
        game["y_b"] = int( gameStr[11] )

        game["x_0"] = int( gameStr[14] )
        game["y_0"] = int( gameStr[16] )

        games.append( game )

    return games


def solveGame( game, conversionError = False):

    x_a = game["x_a"]
    x_b = game["x_b"]

    y_a = game["y_a"]
    y_b = game["y_b"]

    x0 = game["x_0"]
    y0 = game["y_0"]

    if conversionError:
        x0 = game["x_0"] + 10000000000000
        y0 = game["y_0"] + 10000000000000

    p0 = [ x0, y0]
    A = [ [ x_a, x_b], [ y_a, y_b]]

    D = x_a * y_b - x_b * y_a
    invA = [ [ y_b, -x_b], [ -y_a, x_a]]

    p0 = np.array( p0 )
    A = np.array( A )
    invA = np.array( invA ) / D

    solution = invA @ p0
    solution = np.round( solution )

    check = A @ solution
    validSolution = np.all( check == p0 )

    if not validSolution: return 0

    cost = 3 * solution[0] + solution[1]
    cost = int( cost )

    return cost


def playOptimal( games, conversionError = False):

    costs = []

    for game in games:
        cost = solveGame( game, conversionError)
        costs.append( cost )

    return costs