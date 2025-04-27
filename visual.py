from tkinter import *
from generator import clab, tab
 
class Table:
    """
    Used to illustrate the labyrinth as a grid by assining colors to cases 
    """
    def __init__(self, root, tab : list[list]):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if tab[i][j] == 0:
                    self.e = Entry(root, width=20, disabledbackground="white")
                if tab[i][j] == 1:
                    self.e = Entry(root, width=20, disabledbackground="black")
                if tab[i][j] == 2:
                    self.e = Entry(root, width=20, disabledbackground="blue")
                if tab[i][j] == 3:
                    self.e = Entry(root, width=20, disabledbackground="red")
                 
                self.e.grid(row=i, column=j, ipady=10)
                self.e.config(state="disabled")
                

                
total_rows = clab.nb_ligne()
total_columns = clab.nb_colonne()


#window settings
window = Tk()
window.title("Test")
window.minsize(800,600)


#frame creation
frame = Frame(window, bg='#16377b')
frame_lab = Frame(window, bg='#16377b')
frame_sol = Frame(window, bg='#16377b')
t = Table(frame_lab, tab)

#labels of main frame
label_title = Label(frame, text='Labyrinth soliving game', font=("Calibri", 40),bg='#16377b' , fg='#f5f5f5' )
label_title.pack(padx= 35, pady=25)

label_sub = Label(frame, text=  'To solve the labytinth, you have to path from the blue case to reach the red one. \n'
                                'To do so, you may only go through the white cases.',
                        font=("Calibri", 25), fg='#dcdcdc', bg='#16377b')
label_sub.pack(padx= 30, pady=20)

#label of solution frame
label_title_sub = Label(frame_sol, text='Click on the button to see \n the solution', font=("Calibri", 20),bg='#16377b' , fg='#f5f5f5' )
label_title_sub.pack(padx= 20, pady=10)


#function to change background color of button to reveal answer
def handle_click(event):
    """
    changes the background of text widget to display the answer
    """
    text.config(bg="white")

#solution print
solution = clab.solve()

text = Text(frame_sol, height= len(solution), width=10 )
text.config(bg='#000000')
text.tag_configure("center", justify='center')

for i in solution :
    text.insert(END, f"{i}" + '\n') 
text.tag_add("center", "1.0", "end")
text.pack(padx=20, pady=5)
text['state'] = 'disabled'


#button to show answer
button = Button(frame_sol, text="Show solution", pady=5)
button.bind("<Button-1>", handle_click)
button.pack(pady=5)



frame.pack(expand=YES, fill=BOTH)
frame_lab.pack(expand=YES, side=LEFT, fill=BOTH)
frame_sol.pack(expand=YES, side=RIGHT, fill=BOTH)
window.mainloop()
