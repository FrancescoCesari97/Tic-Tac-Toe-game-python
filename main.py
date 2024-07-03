
from tkinter import *
import random 



def next_turn():
    pass

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass


window = Tk()

window.title("FILA FILA 3")

players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " Turn", font=('Arial', 30))
label.pack(side="top")

window.mainloop()