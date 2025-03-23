from random import randint
from pprint import pprint
from labyrinth import labyrinth


#randomly generate a list[list]
rows = randint(4,10)
colums = randint(4,10)

print(rows, colums)

tab = [[0 for _ in range(colums+1)] for _ in range(rows+1)]


#randomly assign start
x, y = randint(0, rows), randint(0, colums)
tab[x][y] = 2

#randomly assign finish
w = randint(0, rows)
z = randint(0, colums)
while (w,z)==(x,y) :
    w, z = randint(0, rows), randint(0, colums)
tab[w][z] = 3


