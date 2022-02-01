
import opc
from time import sleep
import random
import colorsys
import numpy
import math

leds = [(0,0,0)]*360
client = opc.Client('localhost:7890')

client.put_pixels(leds)
client.put_pixels(leds)

from tkinter import *
from tkinter import Frame
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class AnimationBox:
    def __init__(self, root):
        self.root = root
        self.root.title(" Animation Box" )
        self.root.geometry("500x500+0+0")


        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Animation Box",
        fg="red",bg="white",font=("times new romen",20,"bold") )
        lbltitle.pack(side=TOP,fill=X)

        #========IMAGE ONE Snake=========#

        img = Image.open(r"images\snake.png")
        img = img.resize((165,165), Image.ANTIALIAS)     
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 =Button(self.root,  image = self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=55, width=165, height=165)

        #========IMAGE TWO Tree ========#

        img_2 = Image.open(r"images\tree.png")
        img_2 = img_2.resize((165,165), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 =Button(self.root, command=self.Tree, image = self.photoimg_2, cursor="hand2")

        self.btn_2.place(x=165, y=55, width=165, height=165)

        #=========IMAGE THREE Flag========#

        img_3 = Image.open(r"images\flag.jpg")
        img_3 = img_3.resize((165,165), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 =Button(self.root,command=self.Flag, image = self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=330, y=55, width=165, height=165)

        #=========IMAGE FOUR Star========#

        img_4 = Image.open(r"images\blink.jpg")
        img_4 = img_4.resize((165,165), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        self.btn_4 =Button(self.root, image = self.photoimg_4, cursor="hand2")
        self.btn_4.place(x=0, y=220, width=165, height=165)


         # ===============================BUTTON FRAME=============================#

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=430,width=500,height=70)

        btnExit=Button(Buttonframe, command=self.iExit ,text="Exit" ,fg="white",bg="red",font=("times new romen",12,"bold"),width=45)
        btnExit.grid(row=0,column=1)

# =========================== TREE ==========================================#

    def Tree(self):
        
        Tree_positions1 = [[6,7,0,1,0.1], [17,18,0,1,0.1], [29,30,0,1,0.1], [41,42,0,1,0.1], [53,54,0,1,0.1]]
        for i, item in enumerate(Tree_positions1):
            for one in range(item[0], item[1]):
                for row in range(item[2], item[3]):
                    leds[one+row*60] = (255,0,0)
            client.put_pixels(leds)
            sleep(item[4])
        
        Tree_positions2 = [[5,6,7,8,1,2,0.1], [16,17,18,19,1,2,0.1], [28,29,30,31,1,2,0.1], [40,41,42,43,1,2,0.1], [52,53,54,55,1,2,0.1]]
        for i, item in enumerate(Tree_positions2):
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds[one+row*60] = (255,0,0)
            client.put_pixels(leds)
            sleep(item[6])

        Tree_positions3 = [[4,5,6,7,8,9,2,3,0.1], [15,16,17,18,19,20,2,3,0.1], [27,28,29,30,31,32,2,3,0.1], [39,40,41,42,43,44,2,3,0.1], [51,52,53,54,55,56,2,3,0.1]]
        for i, item in enumerate(Tree_positions3):
            for one in range(item[0], item[5]):
                for row in range(item[6], item[7]):
                    leds[one+row*60] = (255,0,0)
            client.put_pixels(leds)
            sleep(item[8])

        Tree_positions4 = [[3,4,5,6,7,8,9,10,3,4,0.1], [14,15,16,17,18,19,20,21,3,4,0.1], [26,27,28,29,30,31,32,33,3,4,0.1], [38,39,40,41,42,43,44,45,3,4,0.1], [50,51,52,53,54,55,56,57,3,4,0.1]]
        for i, item in enumerate(Tree_positions4):
            for one in range(item[0], item[7]):
                for row in range(item[8], item[9]):
                    leds[one+row*60] = (255,0,0)
            client.put_pixels(leds)
            sleep(item[10])

        Tree_positions5 = [[2,3,4,5,6,7,8,9,10,11,4,5,0.1], [13,14,15,16,17,18,19,20,21,22,4,5,0.1], [25,26,27,28,29,30,31,32,33,34,4,5,0.1], [37,38,39,40,41,42,43,44,45,46,4,5,0.1], [49,50,51,52,53,54,55,56,57,58,4,5,0.1]]
        for i, item in enumerate(Tree_positions5):
            for one in range(item[0], item[9]):
                for row in range(item[10], item[11]):
                    leds[one+row*60] = (255,0,0)
            client.put_pixels(leds)
            sleep(item[12])
        
        Tree_positions6 = [[5,6,7,8,5,6,0.1], [16,17,18,19,5,6,0.1], [28,29,30,31,5,6,0.1], [40,41,42,43,5,6,0.1], [52,53,54,55,5,6,0.1]]
        for i, item in enumerate(Tree_positions6):
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds[one+row*60] = (255,0,0)
            client.put_pixels(leds)
            sleep(item[6])


#================================ Flag ==========================================#

    def Flag(self):
        leds =[(0,0,0)]*360

        flag_positions1 = [[0,1,2,3,0,5,0,0,255,0.1], [3,4,5,6,0,5,255,255,0,0.1], [6,7,8,9,0,5,255,0,0,0.1], [9,10,11,12,0,5,255,255,255,0.1], [12,13,14,15,0,5,255,165,0,0.1], [15,16,17,18,0,1,0,0,255,0.1], [15,16,17,18,1,2,255,255,0,0.1], [15,16,17,18,2,3,255,0,0,0.1], [15,16,17,18,3,4,255,255,255,0.1], [15,16,17,18,4,5,255,165,0,0.1]]
        for i, item in enumerate(flag_positions1):
            for one in range(item[0], item[3]):
                 for row in range(item[4], item[5]):
                    leds[one+row*60] = (item[6], item[7], item[8])
            client.put_pixels(leds)
            sleep(item[9])






    def iExit(self):
        iExit=messagebox.askyesno("Animation Box","Do you want to Exit?")
        if iExit>0:
            root.destroy()
            return

   

root=Tk()
ob=AnimationBox(root)
root.mainloop()
