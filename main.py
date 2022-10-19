from tkinter import *
import random

window = Tk()
window.geometry('400x400')
window.resizable(0, 0)
window.title('Rock-Paper-Scissor')

Label(window, text='Rock-Paper-Scissor', font='arial 20 bold').pack()

user_takes = StringVar()
Label(window, text='Choose any of these: rock, paper ,scissors ', font='arial 15 bold').place(x=10, y=40)
Entry(window, font='arial 15', textvariable=user_takes).place(x=90, y=80)

comp = range(0, 2)
for i in comp:
    if comp[i] == 0:
        print('rock')

    elif comp[i] == 1:
        print('Paper')

    else:
        print('Scissor')

Result = StringVar()


def play():
    user_pick = user_takes.get()
    if user_pick == comp:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')


def Reset():
    Result.set('')
    user_takes.set('')


def Exit():
    window.destroy()


Entry(window, font='arial 10 bold', textvariable=Result, width=50, ).place(x=25, y=250)
Button(window, font='arial 13 bold', text='PLAY', padx=5, command=play).place(x=150, y=190)
Button(window, font='arial 13 bold', text='RESET', padx=5, command=Reset).place(x=70, y=310)
Button(window, font='arial 13 bold', text='EXIT', padx=5, command=Exit).place(x=230, y=310)

window.mainloop()
