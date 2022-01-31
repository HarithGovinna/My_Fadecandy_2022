import opc
import time
import math
import random

leds = [(255,255,255)]*360
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

        #===IMAGE ONE========
        img = Image.open(r"images\snake.png")
        img = img.resize((165,165), Image.ANTIALIAS)     
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 =Button(self.root, command=self.snake, image = self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=55, width=165, height=165)

        #===IMAGE TWO========
        img_2 = Image.open(r"images\tree.png")
        img_2 = img_2.resize((165,165), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 =Button(self.root, command=self.tree ,image = self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=165, y=55, width=165, height=165)

        #===IMAGE THREE========
        img_3 = Image.open(r"images\flag.jpg")
        img_3 = img_3.resize((165,165), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 =Button(self.root, command=self.flag ,image = self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=330, y=55, width=165, height=165)

        #===IMAGE FOUR========
        img_4 = Image.open(r"images\blink.jpg")
        img_4 = img_4.resize((165,165), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        self.btn_4 =Button(self.root, command=self.star ,image = self.photoimg_4, cursor="hand2")
        self.btn_4.place(x=0, y=220, width=165, height=165)


         # ===============================BUTTON FRAME=============================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=430,width=500,height=70)

        btnExit=Button(Buttonframe, command=self.iExit ,text="Exit" ,fg="white",bg="red",font=("times new romen",12,"bold"),width=45)
        btnExit.grid(row=0,column=1)

# ============================= Snake ======================================

    def snake(self):
        while True:
            for led in range (355):
                leds = [(255,255,255)]*360
                leds[led] = (0,0,255)
                leds[led+1] = (0,0,255)
                leds[led+2] = (0,0,255)
                leds[led+3] = (0,0,255)
                leds[led+4] = (0,0,255)
                    
                if leds == 255:
                    leds = 0
                client.put_pixels(leds)
                time.sleep(0.1)
                

    # ==========================Tree ======================================#

    def tree(self):
        leds =[(0,0,0)]*360
        for one in range (6,7):   #1 st part
            for rows in range(0,1):
                leds[one+rows *60] = (254,127,156)  #pink
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (17,18):
            for rows  in range(0,1):
                leds[one+rows *60] = (254,127,156)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (29,30):
            for rows  in range(0,1):
                leds[one+rows *60] = (254,127,156)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (41,42):
            for rone in range(0,1):
                leds[one+rone*60] = (254,127,156)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (53,54):
            for rows in range(0,1):
                leds[one+rows *60] = (254,127,156)
        client.put_pixels(leds)
        time.sleep(.1)



        for one in range (5,8):   # 2 nd part
            for rows in range(1,2):
                leds[one+rows *60] = (0,255,0)  #green
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (16,19):   
            for rone in range(1,2):
                leds[one+rone*60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (28,31):   
            for rows  in range(1,2):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (40,43):   
            for rows  in range(1,2):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (52,55):   
            for rows  in range(1,2):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)


        for one in range (4,9):    #3 rd part
            for rows  in range(2,3):
                leds[one+rows *60] = (128,0,0)  #maroon
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (15,20):
            for rows  in range(2,3):
                leds[one+rows *60] = (128,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (27,32):
            for rows  in range(2,3):
                leds[one+rows *60] = (128,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (39,44):
            for rows  in range(2,3):
                leds[one+rows *60] = (128,0,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (51,56):
            for rows  in range(2,3):
                leds[one+rows *60] = (128,0,0)
        client.put_pixels(leds)
        time.sleep(.1)




        for one in range (3,10):     #4 th part
            for rows  in range(3,4):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (14,21):
            for rows  in range(3,4):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (26,33):
            for rows  in range(3,4):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (38,45):
            for rows  in range(3,4):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (50,57):
            for rows  in range(3,4):
                leds[one+rows *60] = (0,255,0)
        client.put_pixels(leds)
        time.sleep(.1)




        for one in range (2,11):    #Last part 5
            for rows  in range(4,5):
                leds[one+rows *60] = (255,140,0)  #dark orange
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (13,22):
            for rows  in range(4,5):
                leds[one+rows *60] = (255,140,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (25,34):
            for rows in range(4,5):
                leds[one+rows *60] = (255,140,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (37,46):
            for rows  in range(4,5):
                leds[one+rows *60] = (255,140,0)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (49,58):
            for rows  in range(4,5):
                leds[one+rows *60] = (255,140,0)
        client.put_pixels(leds)
        time.sleep(.1)


        for one in range (5,8):   #Leg part
            for rows  in range(5,6):
                leds[one+rows *60] = (178,34,34)   #Firebrick
        client.put_pixels(leds)
        time.sleep(.1)


        for one in range (16,19):  
            for rows  in range(5,6):
                leds[one+rows *60] = (178,34,34)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (28,31):  
            for rows  in range(5,6):
                leds[one+rows *60] = (178,34,34)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (40,43):  
            for rows  in range(5,6):
                leds[one+rows *60] = (178,34,34)
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (52,55):  
            for rows  in range(5,6):
                leds[one+rows *60] = (178,34,34)
        client.put_pixels(leds)
        time.sleep(.1)


# ========================== flag =======================================================

    def flag(self):
        leds =[(0,0,0)]*360
        for one in range (0,3):   #1 st part
            for column in range(0,5):
                leds[one+column *60] = (0,0,255)  #blue
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (3,6):   #2 st part
            for column in range(0,5):
                leds[one+column *60] = (255,255,0)  #yellow
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (6,9):   #3 st part
            for column in range(0,5):
                leds[one+column *60] = (255,0,0)  #red
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (9,12):   #4 st part
            for column in range(0,5):
                leds[one+column *60] = (255,255,255)  #white
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (12,15):   #5 st part
            for column in range(0,5):
                leds[one+column *60] = (255,165,0)  #orange
        client.put_pixels(leds)
        time.sleep(.1)


        for one in range (15,18):  
            for rows in range(0,1):
                leds[one+rows*60] = (0,0,255)  #blue
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (15,18): 
            for rows in range(1,2):
                leds[one+rows*60] = (255,255,0)  #yellow
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (15,18):   
            for rows in range(2,3):
                leds[one+rows*60] = (255,0,0) #red
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (15,18):   
            for rows in range(3,4):
                leds[one+rows*60] = (255,255,255) #white
        client.put_pixels(leds)
        time.sleep(.1)

        for one in range (15,18):   
            for rows in range(4,5):
                leds[one+rows*60] = (255,165,0) #orange
        client.put_pixels(leds)
        time.sleep(.1)

# =============================== blink ==========================================

    def star(self):
        numLEDs = 360
        t = 0

        while True:
            t += 0.4
            brightness = int(min(1, 1.25 + math.sin(t)) * 255)
            frame = [ (brightness, brightness, brightness) ] * numLEDs
            client.put_pixels(frame)
            time.sleep(0.05) 


# ============================= exit ============================================

    def iExit(self):
        iExit=messagebox.askyesno("Animation Box","Do you want to Exit?")
        if iExit>0:
            root.destroy()
            return

   

root=Tk()
ob=AnimationBox(root)
root.mainloop()





