from tkinter import *
import inv

def shop(gameplay):
    shopwindow = Toplevel(gameplay)
    #shopwindow = Tk()
    shopwindow.geometry("800x1200")
    shopwindow.title("Shop!")
    
    def buy(item_name,item_price):
        if item_price <= inv.coins:
            inv.add(item_name)
            inv.coins -= item_price
            label.config(text=f"You have bought {item_name} for {item_price}")
            coin_label.config(text=f"Coins = {inv.coins}")
        else:
            label.config(text="Insufficient coins")

    totem_img = PhotoImage(file="images/totem.png")
    totem_img = totem_img.subsample(4,4)
    totem_btn = Button(shopwindow,command=lambda:[buy("Totem",300)],image=totem_img,text="Totem = 300 coins", compound="left",bg="lightblue",font=("Arial",20))
    totem_btn.pack()

    mace_img = PhotoImage(file="images/mace.png")
    mace_img = mace_img.subsample(4,4)
    mace_btn = Button(shopwindow,command=lambda:[buy("Mace",500)],image=mace_img,text="mace = 500 coins", compound="left",bg="lightblue",font=("Arial",20))
    mace_btn.pack()

    goldenapple_img = PhotoImage(file="images/goldenapple.png")
    goldenapple_img = goldenapple_img.subsample(7,7)
    goldenapple_btn = Button(shopwindow,command=lambda:[buy("Golden Apple",100)],image=goldenapple_img,text="Golden Apple = 100 coins", compound="left",bg="lightblue",font=("Arial",20))
    goldenapple_btn.pack()

    ak_47_img = PhotoImage(file="images/ak47.png")
    ak_47_img = ak_47_img.subsample(9,9)
    ak_47_btn = Button(shopwindow,command=lambda:[buy("AK 47",800)],image=ak_47_img,text="AK_47 = 800 coins", compound="left",bg="lightblue",font=("Arial",20))
    ak_47_btn.pack()

    shield_img = PhotoImage(file="images/shield.png")
    shield_img = shield_img.subsample(7,7)
    shield_btn = Button(shopwindow,command=lambda:[buy("Shield",400)],image=shield_img,text="Shield = 400 coins", compound="left",bg="lightblue",font=("Arial",20))
    shield_btn.pack()

    wind_charge_img = PhotoImage(file="images/Wind_Charge.png")
    wind_charge_img = wind_charge_img.subsample(7,7)
    wind_charge_btn = Button(shopwindow,command=lambda:[buy("Wind charge",150)],image=wind_charge_img,text="Wind_Charge = 150 coins", compound="left",bg="lightblue",font=("Arial",20))
    wind_charge_btn.pack()

    back_btn = Button(shopwindow,command=lambda:[shopwindow.withdraw(),gameplay.deiconify()],text="Back")
    back_btn.pack()

    label = Label(shopwindow)
    label.pack()

    coin_label = Label(shopwindow,text=f"Coins = {inv.coins}")
    coin_label.pack()
# images references
    shopwindow.totem_img = totem_img
    shopwindow.ak_47_img = ak_47_img
    shopwindow.goldenapple_img = goldenapple_img
    shopwindow.wind_charge_img = wind_charge_img
    shopwindow.mace_img = mace_img
    shopwindow.shield_img = shield_img

    shopwindow.mainloop()

# shop()