# author: Sebastian Avila
# date: March  17, 2023
# file: game.py is a python program that implements a gui for a fifteen puzzle 
# input: user moves (button presses)
# output: game board

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice
          
def addButton(gui, text, name):
    return Button(gui, textvariable=text, name=str(name),
                      bg='white', fg='black', font=font, height=3, width=4,
                      command = lambda : clickButton(game,name,text))

def clickButton(game,name,text):
    global blank_button_index; global texts; global button_order
    move = int(text.get()) if text.get()!=' ' else 0
    index_move = button_order.index(move)
    index_blank = button_order.index(0)
    if game.is_valid_move(move):
        text.set(' ')
        texts[blank_button_index].set(move)
        button_order[index_move], button_order[index_blank] = button_order[index_blank], button_order[index_move]
        blank_button_index = button_order.index(0)
        game.update(move)
    if game.is_solved():
        gui.title("SOLVED")
    else:
        gui.title("Fifteen")

def shuffleBoard():
    global buttons; global texts; global names
    for i in range(1000):
        random_button = choice(buttons)
        index = buttons.index(random_button)
        clickButton(game,names[index],texts[index])
    
if __name__ == '__main__':    

    # make tiles
    game = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    names = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    button_order = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    
    texts = [StringVar() for i in range(16)]
    buttons = []
    for i in range(16):
        if i == 15:
            texts[i].set(' ')
        else:
            texts[i].set(i+1)
        buttons.append(addButton(gui,texts[i],names[i]))
    blank_button_index = 15
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i, column=j, columnspan=1)
    button_shuffle = Button(gui,text='Shuffle',bg='white',fg='black',font=font,height=2,width=6, command=lambda:shuffleBoard())
    button_shuffle.grid(column=1,columnspan=2,row=5)

    # update the window
    gui.mainloop()
