from tkinter import *
from inv import inventory
import config

def play():#playerwindow):
        #gameplay = Toplevel(playerwindow)
        gameplay = Tk()
        gameplay.title("Play")
        gameplay.geometry("1000x600")
        gameplay.resizable(False,False)
        gameplay.attributes("-fullscreen",config.FULLSCREEN)
        canvas = Canvas(gameplay,width=2300,height=1300,bg="#15E058")
        canvas.pack()
        SPEED = 10
        
        # house 
        # canvas.create_rectangle(1500,445,1766,265,fill="#493333") #width = 533 height = 300
        # canvas.create_polygon(1500,455,2033,445,1283,545,fill="#493333") #

        screen_width = 2560
        screen_height = 1440

        house_width = 533
        house_height = 300

        house_x = screen_width - house_width - 500
        house_y = screen_height - house_height - 400


        roof_height = 170


        house= {
                "roof":canvas.create_polygon(house_x, house_y, house_x + house_width // 2, house_y -
                                      roof_height, house_x + house_width, house_y, fill="#55371B"),
                "walls":canvas.create_rectangle(house_x, house_y, house_x + house_width, house_y + house_height, fill="#6F0606"),
                "door":canvas.create_rectangle(house_x+215,house_y + 160,house_x+315,house_height + house_y, fill="#858282"),
                "handle":canvas.create_oval(house_x + 290,house_y +225, house_x + 300,house_y + 235,fill="red"),
                "name":canvas.create_text(house_x + house_width // 2,house_y + 50,text="Shop",font=("Arial",30,"bold"))
        }

        
        tree1 = {
                "trunk1":canvas.create_rectangle(100,100,115,260,fill="#493333"),
                "leaves1":canvas.create_polygon(0,100,200,100,107,10,fill="#1A6E00")
        }


        tree2 = {
                "trunk":canvas.create_rectangle(600,100,615,260,fill="#493333"),
                "leaves":canvas.create_polygon(500,100,700,100,607,10,fill="#1A6E00")
        }


        #player
        player = {
                "head": canvas.create_oval(320, 320, 380, 380, fill="black") ,
                "body": canvas.create_rectangle(340, 380, 360, 470, fill="white")
        }

        def move(event):
                y = 0
                x = 0
                if event.keysym.lower() == "w":
                        y = -SPEED

                if event.keysym.lower() == "s":
                        y = SPEED

                if event.keysym.lower() == "a":
                        x = -SPEED

                if event.keysym.lower() == "d":
                        x = SPEED

                for i in player.values():
                        canvas.move(i,x,y)

        gameplay.bind("<KeyPress>",move)


        inv_btn = Button(gameplay,command=lambda:[inventory(gameplay),gameplay.withdraw()], text="Inventory")
        inv_btn.place(x=0,y=0)

        back_btn = Button(gameplay,command=lambda:[gameplay.destroy(),])#text="Back",playerwindow.deiconify()])
        back_btn.pack()


play()