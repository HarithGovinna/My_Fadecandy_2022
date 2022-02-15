
import opc
from time import sleep
import random
import colorsys
import numpy
import math

leds = [(0,0,0)]*360
led_frame = [(255,255,255)]*360
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
        self.root.geometry("500x600+0+0")


        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Animation Box",
        fg="red",bg="white",font=("times new romen",20,"bold") )
        lbltitle.pack(side=TOP,fill=X)

        #========IMAGE ONE Snake=========#

        img = Image.open(r"images\snake.png")
        img = img.resize((165,165), Image.ANTIALIAS)     
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 =Button(self.root, command=self.Snake,  image = self.photoimg, cursor="hand2")
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

        self.btn_4 =Button(self.root,command=self.Blink, image = self.photoimg_4, cursor="hand2")
        self.btn_4.place(x=0, y=220, width=165, height=165)


        #========== IMAGE FIVE Random_Dark=====#

        img_5 = Image.open(r"images\Random_Dark.jpg")
        img_5 = img_5.resize((165,165), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        self.btn_5 =Button(self.root, command=self.Random_Dark, image = self.photoimg_5, cursor="hand2")
        self.btn_5.place(x=165, y=220, width=165, height=165)

        #=========== IMAGE SIX Iteraions =======#

        img_6 = Image.open(r"images\iterations.jpg")
        img_6 = img_6.resize((165,165), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        self.btn_6 =Button(self.root, command=self.iterations, image = self.photoimg_6, cursor="hand2")
        self.btn_6.place(x=330, y=220, width=165, height=165)

        #========== IMAGE SEVEN 



         # ===============================BUTTON FRAME=============================#

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=500,height=70)

        btnExit=Button(Buttonframe, command=self.iExit ,text="Exit" ,fg="white",bg="red",font=("times new romen",12,"bold"),width=45)
        btnExit.grid(row=0,column=1)


#============================ Snake =========================================#

    def Snake(self):
        led = 0
        while led < 30:
            for led in range (200):
                leds = [(255,255,255)]*360
                leds[led] = (0, 255,0)
                leds[led+1] = (0,255,0)
                leds[led+2] = (0,255,0)
                leds[led+3] = (0,255,0)
                leds[led+4] = (0,255,0)
                leds[led+5] = (0,255,0)
                leds[led+6] = (255,140,0)

                client.put_pixels(leds)
                sleep(0.1)
                led = led + 1

# =========================== TREE ==========================================#

    def Tree(self):
        leds =[(0,0,0)]*360
        leds1 =[(0,0,0)]*360
        leds2 =[(0,0,0)]*360
        leds3 =[(0,0,0)]*360
        leds4 =[(0,0,0)]*360
        leds5 =[(0,0,0)]*360

                
        Tree_positions1 = [[6,7,0,1], [17,18,0,1], [29,30,0,1], [41,42,0,1], [53,54,0,1]]
        for i, item in enumerate(Tree_positions1):
            for one in range(item[0], item[1]):
                for row in range(item[2], item[3]):
                    leds[one+row*60] = (255,0,0)         #Red
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (148,0,211)      #Violet
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink
                    

                
        Tree_positions2 = [[5,6,7,8,1,2], [16,17,18,19,1,2], [28,29,30,31,1,2], [40,41,42,43,1,2], [52,53,54,55,1,2]]
        for i, item in enumerate(Tree_positions2):
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds[one+row*60] = (255,0,0)
                    leds1[one+row*60] = (0,255,0)
                    leds2[one+row*60] = (255,0,255)
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink
                    

        Tree_positions3 = [[4,5,6,7,8,9,2,3], [15,16,17,18,19,20,2,3], [27,28,29,30,31,32,2,3], [39,40,41,42,43,44,2,3], [51,52,53,54,55,56,2,3]]
        for i, item in enumerate(Tree_positions3):
            for one in range(item[0], item[5]):
                for row in range(item[6], item[7]):
                    leds[one+row*60] = (255,0,0)
                    leds1[one+row*60] = (0,255,0)
                    leds2[one+row*60] = (255,0,255)
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        Tree_positions4 = [[3,4,5,6,7,8,9,10,3,4], [14,15,16,17,18,19,20,21,3,4], [26,27,28,29,30,31,32,33,3,4], [38,39,40,41,42,43,44,45,3,4], [50,51,52,53,54,55,56,57,3,4]]
        for i, item in enumerate(Tree_positions4):
            for one in range(item[0], item[7]):
                for row in range(item[8], item[9]):
                    leds[one+row*60] = (255,0,0)
                    leds1[one+row*60] = (0,255,0)
                    leds2[one+row*60] = (255,0,255)
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        Tree_positions5 = [[2,3,4,5,6,7,8,9,10,11,4,5], [13,14,15,16,17,18,19,20,21,22,4,5], [25,26,27,28,29,30,31,32,33,34,4,5], [37,38,39,40,41,42,43,44,45,46,4,5], [49,50,51,52,53,54,55,56,57,58,4,5]]
        for i, item in enumerate(Tree_positions5):
            for one in range(item[0], item[9]):
                for row in range(item[10], item[11]):
                    leds[one+row*60] = (255,0,0)
                    leds1[one+row*60] = (0,255,0)
                    leds2[one+row*60] = (255,0,255)
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        Tree_positions6 = [[5,6,7,8,5,6], [16,17,18,19,5,6], [28,29,30,31,5,6], [40,41,42,43,5,6], [52,53,54,55,5,6]]
        for i, item in enumerate(Tree_positions6):
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds[one+row*60] = (255,0,0)
                    leds1[one+row*60] = (0,255,0)
                    leds2[one+row*60] = (255,0,255)
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        while True:
            client.put_pixels(leds)
            sleep(0.5)
            client.put_pixels(leds1)
            sleep(0.5)
            client.put_pixels(leds2)
            sleep(0.5)
            client.put_pixels(leds3)
            sleep(0.5)
            client.put_pixels(leds4)
            sleep(0.5)
            client.put_pixels(leds5)
            sleep(0.5)

    


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



#============================== Star ========================================#
    def Blink(Self):

        numStrings = 8
        
        string = [ (0,0,0) ] * 64
        for j in range(8):
            string[8 * j] = (0, 255, 0)
        led_color = string * numStrings

        for i in range(8):
            string[8 * i] = (255, 0, 17)
        led_color1 = string * numStrings

        for i in range(8):
            string[8 * i] = (255, 140, 0)
        led_color3 = string * numStrings

        while True:
            client.put_pixels(led_color)
            sleep(0.5)
            client.put_pixels(led_color1)
            sleep(0.5)
            client.put_pixels(led_color3)
            sleep(0.5)
          


#=============================== Random - Dark ===================================#

    def Random_Dark (self):
        Turns=0
        while Turns<=2:
            led = 0
            while led<60:
                for rows in range(6):
                    led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.02), 205 * ((led / 30)- 0.03))
                    led_frame[59-led + rows*60] = led_color
                sleep(.1)
                client.put_pixels(led_frame)
                led = led + 1 #or reverse if you want


            led = 0
            while led<60:
                for rows in range(6):
                    led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.1), 205 * ((led / 30)- 0.2))
                    led_frame[led + rows*60] = led_color
                sleep(.1)
                client.put_pixels(led_frame)
                led = led + 1 #or reverse if you want

            Turns = Turns+1

# ========================== Iterations=====================#

    def iterations(self):
        numLEDs = 512
        yelloshade = (255 * ((numLEDs / 10) - 0.2), 128 * ((numLEDs/ 10) - 0.2), 0)

        red = [(255, 0, 17)] * numLEDs
        green = [(0, 255, 0)] * numLEDs
        yellow = [(255, 140, 0)]* numLEDs

        Rounds = 0
        while Rounds <=2:
            led = 0
            while led < 60:
                for i in range(numLEDs):
                    pixels = red
                    pixels[i] = yelloshade
                    client.put_pixels(pixels)
                    sleep(0.01)
                    led = led + 1
            led = 0
            while led < 60:
                for j in range(numLEDs):
                    pixels = green
                    led_color = (128 * ((led / 300) - 0.01), 0, 0)
                    pixels[j] = led_color
                    client.put_pixels(pixels)
                    sleep(0.01)
                    led = led + 1
            led = 0
            while led<30: #scroll all rows at the same time
                for rows in range(6): #first three rows left to right
                    led_color = (255 * ((led / 30) - 0.01), 70 * ((led / 30) - 0.02), 14 * ((led / 30)- 0.03))
                    leds[29-led + rows*60] = led_color
                for rows in range(6):
                    leds[30+led + rows* 60] = led_color
                client.put_pixels(leds)
                sleep(.1)
                led = led + 1

            led = 0
            while led<30:
                    for k in range(360):
                        pixels = [ (0,0,0) ] * numLEDs
                        pixels[k] = (255, 255, 255)
                        client.put_pixels(pixels)
                        sleep(0.01)
                        led = led + 1

        Rounds = Rounds+1    


#===========================Exit=======================#

    def iExit(self):
        iExit=messagebox.askyesno("Animation Box","Do you want to Exit?")
        if iExit>0:
            root.destroy()
            return

   

root=Tk()
ob=AnimationBox(root)
root.mainloop()
