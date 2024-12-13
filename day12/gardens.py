import gardenlib

file = open("./day12/data.txt")
lines = file.readlines()

map = gardenlib.parse( lines )
plots = gardenlib.getPlots( map )
price, priceBulk = gardenlib.computePrice( plots, map)

print( price )
print( priceBulk )