
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

rest_button = Button(text="restart", font=('Arial', 20), command=new_game)
rest_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range (3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Arial', 20), width=3, height=3,
                                       command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()