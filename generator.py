from random import randint
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



#create walls in order to create the labyrinthe 
walls_created = []
lab = labyrinth(tab)
clab = lab
x, y = clab.depart()
w, z = clab.arrivee()

while clab.solve():
    u, v = randint(0, rows), randint(0, colums)
    while (u,v)==(x,y) or (u,v)==(w,z) :
        u, v = randint(0, rows), randint(0, colums)
    tab[u][v] = 1
    walls_created.append((u,v))
    tab[x][y] = 2
    tab[w][z] = 3
    clab.refresh()
    print(walls_created)


clab.tab[x][y] = 2
clab.refresh()


if __name__ == '__main__':
    clab.affiche()