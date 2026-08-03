from tkinter import *
from Settings import settings
from Play import play
import config

def player(window):
    playerwindow = Toplevel(window)
    playerwindow.title("Player selection")
    playerwindow.geometry("700x450")
    playerwindow.attributes("-fullscreen",config.FULLSCREEN)

    mainframe = Frame(playerwindow)
    mainframe.pack(fill="both", expand=True)

    leftframe = Frame(mainframe)
    leftframe.pack(side="left",fill="both",expand=True,padx=20,pady=20)

    rightframe = Frame(mainframe)
    rightframe.pack(side="right",fill="both",expand=True,padx=20,pady=20)

    file_name = "images/player.png"
    
    def get_values():
        
        global photo
        

        #get values
        player_name = entry1.get()
        charactername = character.get()
        ability_chosen = ability.get()
            
        #fighters
            
        if player_name == "" or player_name == " ":
            playername.config(text="You player name shouldn't have spaces")

        else:
            photo = PhotoImage(file=file_name)
            photo_label.config(image=photo)

            playername.config(text=f"Your player name will be {player_name.capitalize()}")
            submit.config(text="confirm",command=lambda:[play(playerwindow) ,playerwindow.withdraw()])

            if charactername =="monk":
                fighter_preview.config(text="You chose to fight with Monk")
                

            if charactername == "samurai":
                fighter_preview.config(text="You chose to fight with Samurai")
                

            if charactername == "warrior":
                fighter_preview.config(text="You chose to fight with Warrior")

            #abilities

            if ability_chosen =="Fireball":
                ability_preview.config(text="You chose the ability to throw a Fireball")
                

            if ability_chosen == "Dtap":
                ability_preview.config(text="You chose to attack 2 times in 0.5s")
                

            if ability_chosen == "Jab":
                ability_preview.config(text="You chose a quick, sharp thrust punch")

        
        
        

# variables

    ability = StringVar()
    ability.set("Dtap")

    character = StringVar()
    character.set("Monk")
    

#widgets

    playername = Label(rightframe)
    playername.pack()

    fighter_preview = Label(rightframe)
    fighter_preview.pack()

    ability_preview = Label(rightframe)
    ability_preview.pack()

    fighter_preview = Label(rightframe)
    fighter_preview.pack()
    
    label = Label(leftframe,text="Enter the name of your character")
    label.pack()

    entry1 = Entry(leftframe)
    entry1.pack()

    player_select = Label(leftframe,text="Select a character class")
    player_select.pack()

    photo_label = Label(rightframe)
    photo_label.pack()

# fighters

    monk = Radiobutton(leftframe,text="Monk",variable=character,value="monk")
    monk.pack()

    Warrior = Radiobutton(leftframe,text="Warrior",variable=character,value="warrior")
    Warrior.pack()

    samurai = Radiobutton(leftframe,text="Samurai",variable=character,value="samurai")
    samurai.pack()

    player_ability = Label(leftframe,text="Select an ability")
    player_ability.pack()

# abilities

    Fireball = Radiobutton(leftframe,text="Fireball",variable=ability,value="Fireball")
    Fireball.pack()

    dtap = Radiobutton(leftframe,text="Dtap",variable=ability,value="Dtap")
    dtap.pack()

    Jab = Radiobutton(leftframe,text="Jab",variable=ability,value="Jab")
    Jab.pack()

# submit button
    submit = Button(leftframe, text="Submit",command=get_values)
    submit.pack()

    back_btn = Button(playerwindow,text="Back",command=lambda:[playerwindow.destroy(), window.deiconify()])
    back_btn.place(x=0,y=0)