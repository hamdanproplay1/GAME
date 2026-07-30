from tkinter import *
from tkinter import messagebox
import config

def inventory(gameplay):
    inv_window = Toplevel(gameplay)
    inv_window.title("Inventory")
    inv_window.geometry("500x400")
    inv_window.attributes("-fullscreen",config.FULLSCREEN)

    def remove():
        selection = listbox.curselection()
        listbox.delete(selection)

    def add():
        ...

    def equip():
        selection = listbox.curselection()
        messagebox.showinfo("Inventory","You've equiped the selected item")

    back_btn = Button(inv_window,text="Back",command=lambda:[inv_window.destroy(),gameplay.deiconify()])
    back_btn.place(x=0,y=0)

    items = ["potion","sword","axe","steak"]
    Label(inv_window,text="Your Inventory").pack()
    listbox = Listbox(inv_window)
    listbox.pack()

    for i in items:
        listbox.insert(END,i)

    discard_btn = Button(inv_window,text="Discard",command=remove)
    discard_btn.pack()
    
    add_btn = Button(inv_window,text="Add")
    add_btn.pack()

    equip_btn = Button(inv_window,text="Equip",command=equip)
    equip_btn.pack()

