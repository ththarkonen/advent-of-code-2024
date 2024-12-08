import antennas

file = open("./day8/data.txt")
lines = file.readlines()

data = antennas.parse( lines )
antinodes = antennas.computeAntinodes( data )
antinodesHarmonic = antennas.computeHarmonicAntinodes( data )

totalAntinodes = len( antinodes )
totalHarmonics = len( antinodesHarmonic )

print( totalAntinodes )
print( totalHarmonics )