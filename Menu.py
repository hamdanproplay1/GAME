from tkinter import *
from Settings import settings
from tkinter import messagebox
import config
from Player import player
def menu():  
    window = Tk()
    window.geometry("600x400")
    window.title("Game menu")
    window.attributes("-fullscreen",config.FULLSCREEN)
    def always_exit():
        variable = messagebox.askyesno("Exit Game", "Are you sure to exit the game?")
        if variable:
            window.destroy()

    play = Button(window,command=lambda:[player(window), window.withdraw()],text="Start",font=("Arial"),width=15,height=4)
    play.place(x=210,y=0)
    
    settings1 = Button(window,text="Settings",command=lambda: [settings(window), window.withdraw()],font=("Arial"),width=15,height=4)
    settings1.place(x=210,y=130)

    exit = Button(window,command=always_exit,text="Exit",font=("Arial"),width=15,height=4)
    exit.place(x=210,y=250)

    window.mainloop()

