from typing import Any
from base import Stack

class labyrinth:
    """
    Labyrinthe

    Methodes :
        - .affiche : afficher le labyrinthe
        - .nb_ligne : donne le nombre de lignes
        - .nb_colonne : donne le nombre de colonne
        - .depart : donne les coordonnées du départ
        - .arrivee : donne les coordonnées de l'arrivée
        - .est_valide : vérifie la véracité des coordonées dans un laryrinthe
        - .nb_cases_vides : compte le nombre de cases vides dans un labyrinthe
        - .est_visitee : marque une case comme visitée
        - .liste_voisines_libres : donne les cases libres à proximité$$
        - .solve : solves the labyrinth
    
    """
    def __init__(self , li : list):
        self.tab = li

    def affiche(self ) -> list:
        """
        Affiche le labyrinthe
        """
        for inner_list in self.tab:
            print(inner_list)

    def nb_ligne(self ) -> int:
        """
        Donne le nombre de lignes
        """
        count = 0
        for _ in self.tab: 
            count += 1
        return count
    
    def nb_colonne(self) -> int :
        """
        Donne le nombre de colonne
        """
        count = 0
        for _ in self.tab[1]:
            count+= 1
        return count
    
    def depart(self ) -> int :
        """
        Donne le tuple du point de départ
        """
        i = 0
        for _ in self.tab:
            for j in range(len(self.tab[i])):
                if self.tab[i][j] == 2:
                    return i, j
            i += 1 
        

    def arrivee(self) -> int:
        """
        Donne le tuple du point d'arrivée
        """
        i = 0
        for _ in self.tab:
            for j in range(len(self.tab[i])):
                if self.tab[i][j] == 3:
                    return i, j
            i += 1

    def est_valide(self , i : int, j: int) -> bool :
        """
        Vérifie la véracité des coordonées dans un laryrinthe
        """
        if 0 <= i <= self.nb_ligne and 0 <= j <= self.nb_colonne() :
            return True
        return False
    
    def nb_cases_vides(self ) -> int:
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

    def est_visitee(self , i : int, j : int) -> None:
        """
        Marque une case comme visité en changeant le chiffre en 4
        """
        self.tab[i][j] = 4

    def liste_voisines_libres(self , i: int, j : int) -> list :
        """
        Donne une liste des coordonnées des cases voisines disponibles 
        """
        available = []
        if j+1 <= self.nb_colonne()-1 :
            if self.tab[i][j+1] == 0 or self.tab[i][j+1] == 3:
                available.append((i, j+1))
        if j-1 >= 0: 
            if self.tab[i][j-1] == 0 or self.tab[i][j-1] == 3:
                available.append((i, j-1))
        if i-1 >= 0: 
            if self.tab[i-1][j] == 0 or self.tab[i-1][j] == 3:
                available.append((i-1, j))
        if i+1 <= self.nb_ligne()-1:
            if self.tab[i+1][j] == 0 or self.tab[i+1][j] == 3:
                available.append((i+1, j))       
        if available != []:
            return available
        return None
    
    def case_fausse(self , i : int, j : int) -> None :
        """
        Remplace le numéro par 5 d'une case menant sur une impasse
        """
        if self.liste_voisines_libres(i,j) == None:
            self.tab[i][j] = 5

    def solve(self) -> Stack :
        sol = Stack()
        x, y = self.depart()
        w, z = self.arrivee()
        self.est_visitee(x, y)
        while x != w or y != z: 
            l = self.liste_voisines_libres(x, y)
            x, y = l[0]
            self.est_visitee(x, y)
            sol.put((x, y))
            l = self.liste_voisines_libres(x, y)
            if self.liste_voisines_libres(x, y) == None and (x, y) != (w, z):
                while self.liste_voisines_libres(x, y) == None:
                    x, y = sol.get()

        l_sol = []
        while not sol.is_empty:
                l_sol.append(sol.get())
        return l_sol



tab2 = [[1, 1, 1, 1, 1, 1, 1],
        [2, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 3, 1]]


lab1 = labyrinth(tab2)
clab1 = lab1


if __name__ == '__main__':

    print(clab1.depart())