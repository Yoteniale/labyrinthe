from typing import Self, Any
from base import Stack

class labyrinth:
    """
    Labyrinthe

    Methodes :
        - .affiche : afficher le labyrinthe
        - .nbligne : donne le nombre de lignes
        - .nbcolonne : donne le nombre de colonne
        - .depart : donne les coordonnées du départ
        - .arrivee : donne les coordonnées de l'arrivée
        - .est_valide : vérifie la véracité des coordonées dans un laryrinthe
        - .nb_cases_vides : compte le nombre de cases vides dans un labyrinthe
        - .est_visitee : marque une case comme visitée
        - .liste_voisines_libres : donne les cases libres à proximité
    
    """
    def __init__(self : Self, li : list):
        self.tab = li

    def affiche(self: Self) -> list:
        """
        Affiche le labyrinthe
        """
        for inner_list in self.tab:
            print(inner_list)

    def nblignes(self : Self) -> int:
        """
        Donne le nombre de lignes
        """
        count = 0
        for _ in self.tab: 
            count += 1
        return count
    
    def nbcolonne(self : Self) -> int :
        """
        Donne le nombre de colonne
        """
        count = 0
        for _ in self.tab[1]:
            count+= 1
        return count
    
    def depart(self : Self) -> int :
        """
        Donne le tuple du point de départ
        """
        i = 0
        for _ in self.tab:
            for j in range(len(self.tab[i])):
                if j == 2:
                    return i, j
            i += 1 

    def arrivee(self : Self) -> int:
        """
        Donne le tuple du point d'arrivée
        """
        i = 0
        for _ in self.tab:
            for j in range(len(self.tab[i])):
                if self.tab[i][j] == 3:
                    return i, j
            i += 1

    def est_valide(self : Self, i : int, j: int) -> bool :
        """
        Vérifie la véracité des coordonées dans un laryrinthe
        """
        if 0 <= i <= self.nblignes and 0 <= j <= self.nbcolonne() :
            return True
        return False
    
    def nb_cases_vides(self : Self) -> int:
        """
        Compte le nombre de cases vides dans un labyrinthe
        """
        i = 0
        nbempty = 0
        for _ in self.tab:
            for j in self.tab[i]:
                if j == 0:
                    nbempty += 1
            i += 1
        return nbempty

    def est_visitee(self : Self, i : int, j : int) -> None:
        """
        Marque une case comme visité en changeant le chiffre en 4
        """
        self.tab[i][j] = 4

    def liste_voisines_libres(self : Self, i: int, j : int) -> list :
        """
        Donne une liste des coordonnées des cases voisines disponibles 
        """
        available = []
        if j+1 <= self.nbcolonne()-1 :
            if self.tab[i][j+1] == 0 or self.tab[i][j+1] == 3:
                available.append((i, j+1))
        if j-1 >= 0: 
            if self.tab[i][j-1] == 0 or self.tab[i][j-1] == 3:
                available.append((i, j-1))
        if i-1 >= 0: 
            if self.tab[i-1][j] == 0 or self.tab[i-1][j] == 3:
                available.append((i-1, j))
        if i+1 <= self.nblignes()-1:
            if self.tab[i+1][j] == 0 or self.tab[i+1][j] == 3:
                available.append((i+1, j))       
        if available != []:
            return available
        return None
    
    def case_fausse(self : Self, i : int, j : int) -> None :
        """
        Remplace le numéro par 5 d'une case menant sur une impasse
        """
        if self.liste_voisines_libres(i,j) == None:
            self.tab[i][j] = 5




tab2 = [[1, 1, 1, 1, 1, 1, 1],
        [2, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 3, 1]]


lab1 = labyrinth(tab2)
# lab1.affiche()
# print(lab1.nblignes())
# print(lab1.nbcolonne())
# print(lab1.depart())
# print(lab1.arrivee())
# print(lab1.est_valide(4, 5))
# print(lab1.est_valide(12, -3))
# print(lab1.nb_cases_vides())
# print(lab1.liste_voisines_libres(2, 0))

clab1 = lab1
sol = Stack()
x, y = clab1.depart()
w, z = clab1.arrivee()
clab1.est_visitee(x, y)
l = clab1.liste_voisines_libres(x, y)


while x != w or y != z: 
    l = clab1.liste_voisines_libres(x, y)
    x, y = l[0]
    clab1.est_visitee(x, y)
    sol.put((x, y))
    l = clab1.liste_voisines_libres(x, y)
    if clab1.liste_voisines_libres(x, y) == None and (x, y) != (w, z):
        while clab1.liste_voisines_libres(x, y) == None:
            x, y = sol.get()


while not sol.is_empty():
        print(sol.get())





#etape 4 : 2. il n'y a pas de solutions
# while clab1.liste_voisines_libres(x, y) != None :
#     l = clab1.liste_voisines_libres(x, y)
#     x, y = l[0], l[1]
#     clab1.est_visitee(x, y)
#     sol.put(f"({x}, {y})")
#     l = clab1.liste_voisines_libres(x, y)
# if x == w and y == z : 
#     while not sol.is_empty():
#         print(sol.get())
# else :
#     pass
# pas finito


#tuple = n-uplet
tu = (3,4,5)
#ou tu = 3,4,5
x, y, z = tu
print(tu)
print(tu[0])
