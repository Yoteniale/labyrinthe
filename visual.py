from tkinter import *
from labyrinth import lab1, tab2
 
class Table:
     
    def __init__(self,root, tab):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if tab[i][j] == 0:
                    self.e = Entry(root, width=20, bg="white")
                if tab[i][j] == 1:
                    self.e = Entry(root, width=20, bg="black")
                if tab[i][j] == 2:
                    self.e = Entry(root, width=20, bg="blue")
                if tab[i][j] == 3:
                    self.e = Entry(root, width=20, bg="red")
                 
                self.e.grid(row=i, column=j)

                
                
                
total_rows = lab1.nb_ligne()

total_columns = lab1.nb_colonne()
  
# create root window
root = Tk()
t = Table(root, tab2)
root.mainloop()
