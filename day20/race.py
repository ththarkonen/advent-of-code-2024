import racelib

file = open("./day20/data.txt")
lines = file.readlines()

start, stop, racemap = racelib.parse( lines )
path = racelib.tracePath( start, stop, racemap)

speedUpsSilver = racelib.cheat( path, stop, radius = 2, minimumSpeedup = 100)
speedUpsGold = racelib.cheat( path, stop, radius = 20, minimumSpeedup = 100)

totalSilver = speedUpsSilver.values()
totalGold = speedUpsGold.values()

totalSilver = sum( totalSilver )
totalGold = sum( totalGold )

print( totalSilver )
print( totalGold )