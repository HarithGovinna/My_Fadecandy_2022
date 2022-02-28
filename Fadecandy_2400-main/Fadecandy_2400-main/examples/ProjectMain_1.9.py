#Libraries
import opc                             #import OPC library           
from time import sleep                 #import sleep library from time


from tkinter import *                  #Import all tk libraries to create user interface
from tkinter import Frame              #Rectangular areas in the screen to organize the layout
from PIL import Image, ImageTk         #Import image library
from tkinter import messagebox         #Import messagebox library

#Variables
leds = [(0,0,0)]*360                   #Black colour LED simulator               
led_frame = [(255,255,255)]*360        #White colour LED simulator 
client = opc.Client('localhost:7890')  #Create a client object for the Open Pixel server

client.put_pixels(leds)                #Printing LEDs in the simulator              

#User Interface
class AnimationBox:                         #Define a class
    def __init__(self, root):               #Allows the class to initialize the attributes of the class
        self.root = root                    #The variable that wants to access the class
        self.root.title("Animation Box")    #Title of the user interface 
        self.root.geometry("500x600+0+0")   #Size of the user interface


        # Create a label for the title
        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Animation Box",   #Title
        fg="red",bg="white",font=("times new romen",20,"bold"))             #Title colour,Font type, Font size
        lbltitle.pack(side=TOP,fill=X)                                      #Position of the title


        #==================IMAGE ONE Snake==============#

        img = Image.open(r"images\snake.png")            #File path of the snake image. 
        img = img.resize((165,165), Image.ANTIALIAS)     #Size of the image. ANTIALIAS : smoothing of jagged edges in digital images by averaging the colors of the pixels at a boundary.
        self.photoimg = ImageTk.PhotoImage(img)          #Importing snake image

        self.btn_1 =Button(self.root, command=self.Snake,  image = self.photoimg, cursor="hand2")   #Create snake button.  def + command
        self.btn_1.place(x=0, y=55, width=165, height=165)                                          #Size and the position of the button

        #==================IMAGE TWO Tree ================#

        img_2 = Image.open(r"images\tree.png")            #File path of the Tree image          
        img_2 = img_2.resize((165,165), Image.ANTIALIAS)  #Size of the image
        self.photoimg_2 = ImageTk.PhotoImage(img_2)       #Importing snake image

        self.btn_2 =Button(self.root, command=self.Tree, image = self.photoimg_2, cursor="hand2")    #Create Tree button. def + command
        self.btn_2.place(x=165, y=55, width=165, height=165)  
                                               #Size and the position of the button

        #==================IMAGE THREE Flag===============#

        img_3 = Image.open(r"images\flag.jpg")              #File path of the Flag image 
        img_3 = img_3.resize((165,165), Image.ANTIALIAS)    #Size of the image
        self.photoimg_3 = ImageTk.PhotoImage(img_3)         #Importing snake image

        self.btn_3 =Button(self.root,command=self.Flag, image = self.photoimg_3, cursor="hand2")    #Create flag button. def + command
        self.btn_3.place(x=330, y=55, width=165, height=165)                                        #Size and the position of the button

        #==================IMAGE FOUR Star=================#

        img_4 = Image.open(r"images\blink.jpg")            #File path of the star image 
        img_4 = img_4.resize((165,165), Image.ANTIALIAS)   #Size of the image
        self.photoimg_4 = ImageTk.PhotoImage(img_4)        #Importing snake image

        self.btn_4 =Button(self.root,command=self.Blink, image = self.photoimg_4, cursor="hand2")    #Create flag button. def + command
        self.btn_4.place(x=0, y=220, width=165, height=165)                                          #Size and the position of the button


        #=============== IMAGE FIVE Random_Dark============#

        img_5 = Image.open(r"images\Random_Dark.jpg")        #File path of the Random dark image 
        img_5 = img_5.resize((165,165), Image.ANTIALIAS)     #Size of the image
        self.photoimg_5 = ImageTk.PhotoImage(img_5)          #Importing snake image

        self.btn_5 =Button(self.root, command=self.Random_Dark, image = self.photoimg_5, cursor="hand2")   #Create flag button. def + command
        self.btn_5.place(x=165, y=220, width=165, height=165)                                              #Size and the position of the button

        #================ IMAGE SIX Iteraions =============#

        img_6 = Image.open(r"images\iterations.jpg")            #File path of the Iterations image
        img_6 = img_6.resize((165,165), Image.ANTIALIAS)        #Size of the image
        self.photoimg_6 = ImageTk.PhotoImage(img_6)             #Importing snake image

        self.btn_6 =Button(self.root, command=self.iterations, image = self.photoimg_6, cursor="hand2")     #Create flag button. def + command
        self.btn_6.place(x=330, y=220, width=165, height=165)                                               #Size and the position of the button 

        #============== IMAGE SEVEN Blinking ==============#

        img_7 = Image.open(r"images\Blinking.jpg")               #File path of the Blinking image
        img_7 = img_7.resize((165,165), Image.ANTIALIAS)         #Size of the image
        self.photoimg_7 = ImageTk.PhotoImage(img_7)              #Importing snake image

        self.btn_7 =Button(self.root, command=self.Blinking, image = self.photoimg_7, cursor="hand2")     #Create flag button. def + command
        self.btn_7.place(x=0, y=385, width=165, height=165)                                               #Size and the position of the button 


        #============ IMAGE EIGHT Mid Reverse ============#

        img_8 = Image.open(r"images\Mid_Reverse.jpg")          #File path of the Mid reverse image
        img_8 = img_8.resize((165,165), Image.ANTIALIAS)       #Size of the image
        self.photoimg_8 = ImageTk.PhotoImage(img_8)            #Importing snake image

        self.btn_8 =Button(self.root, command=self.Mid_Reverse, image = self.photoimg_8, cursor="hand2")      #Create flag button. def + command
        self.btn_8.place(x=165, y=385, width=165, height=165)                                                 #Size and the position of the button

        #================ TEST Covid-19==================#

        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)             #Create button frame,  bd=20 : backgrounf size of the button
        Buttonframe.place(x=330,y=385,width=165,height=145)         #Size and the position of the button frame

        btnCovid=Button(Buttonframe , command= self.Covid, text="Test Me" ,fg="white",bg="green",font=("times new romen",12,"bold"),width=12,height=5)   #Create Covid button
        btnCovid.grid(row=0,column=1)                                                                                                                    #Position and the size of the button. fg: Font colour, bg: Background colour


        # ===============================BUTTON FRAME=============================#

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)             #Create button frame,  bd=20 : backgrounf size of the button
        Buttonframe.place(x=0,y=530,width=500,height=70)            #Size and the position of the button frame

        btnExit=Button(Buttonframe, command=self.iExit ,text="Exit" ,fg="white",bg="red",font=("times new romen",12,"bold"),width=45)          #Create Covid button
        btnExit.grid(row=0,column=1)                                                                                                           #Position and the size of the button. fg: Font colour, bg: Background colour


#============================ Snake =========================================#

    def Snake(self):                              #Defining snakes self function
        led = 0                                   #Number of LEDs
        while led < 30:                           #While number of LEDs less than 30                           
            for led in range (150):               #Run the python in the LED range of 150
                leds = [(255,255,255)]*360        #Colour of LED frame (white) 
                leds[led] = (0, 255,0)            #Adding one LED to the front for the forward motion. Colour Green 
                leds[led+1] = (0,255,0)   
                leds[led+2] = (0,255,0)
                leds[led+3] = (0,255,0)
                leds[led+4] = (0,255,0)
                leds[led+5] = (0,255,0)
                leds[led+6] = (255,140,0)          #Colour Yellow

                client.put_pixels(leds)            #Draw a LED pixel in the frame.
                sleep(0.1)                         #Sleep by 0.1 seconds
                led = led + 1                      #Counting the number of turns in the while loop.

        

# =========================== TREE ==========================================#

    def Tree(self):                             #Defining Tree self function
        leds = [(0,0,0)]*360                    #Colour of LED frame (White)
        leds1 =[(0,0,0)]*360                    #
        leds2 =[(0,0,0)]*360
        leds3 =[(0,0,0)]*360
        leds4 =[(0,0,0)]*360
        leds5 =[(0,0,0)]*360

                
        Tree_positions1 = [[6,7,0,1], [17,18,0,1], [29,30,0,1], [41,42,0,1], [53,54,0,1]]   #Make a variable as Tree_positions1 to give the first line led position by an array list 
        for i, item in enumerate(Tree_positions1):                                          #Implementing first tree list to the python's enumerate() to get a counter and the value from the iterable at the same time.
            for one in range(item[0], item[1]):                                             #Postions of the fisrt column in the Tree_positions1 
                for row in range(item[2], item[3]):                                         #Postions of the fisrt row in the Tree_positions1                                      
                    leds[one+row*60] = (255,0,0)         #Red     ||   Implement the colours for the design
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (148,0,211)      #Violet
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink
                    

                
        Tree_positions2 = [[5,6,7,8,1,2], [16,17,18,19,1,2], [28,29,30,31,1,2], [40,41,42,43,1,2], [52,53,54,55,1,2]]
        for i, item in enumerate(Tree_positions2):
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds[one+row*60] = (255,0,0)         #Red
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (255,0,255)      #Violet
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink
                    

        Tree_positions3 = [[4,5,6,7,8,9,2,3], [15,16,17,18,19,20,2,3], [27,28,29,30,31,32,2,3], [39,40,41,42,43,44,2,3], [51,52,53,54,55,56,2,3]]
        for i, item in enumerate(Tree_positions3):
            for one in range(item[0], item[5]):
                for row in range(item[6], item[7]):
                    leds[one+row*60] = (255,0,0)         #Red
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (255,0,255)      #Violet
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        Tree_positions4 = [[3,4,5,6,7,8,9,10,3,4], [14,15,16,17,18,19,20,21,3,4], [26,27,28,29,30,31,32,33,3,4], 
                          [38,39,40,41,42,43,44,45,3,4], [50,51,52,53,54,55,56,57,3,4]]
        for i, item in enumerate(Tree_positions4):
            for one in range(item[0], item[7]):
                for row in range(item[8], item[9]):
                    leds[one+row*60] = (255,0,0)         #Red
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (255,0,255)      #Violet
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        Tree_positions5 = [[2,3,4,5,6,7,8,9,10,11,4,5], [13,14,15,16,17,18,19,20,21,22,4,5],
                          [25,26,27,28,29,30,31,32,33,34,4,5], [37,38,39,40,41,42,43,44,45,46,4,5], [49,50,51,52,53,54,55,56,57,58,4,5]]
        for i, item in enumerate(Tree_positions5):
            for one in range(item[0], item[9]):
                for row in range(item[10], item[11]):
                    leds[one+row*60] = (255,0,0)         #Red
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (255,0,255)      #Violet
                    leds3[one+row*60] = (255, 255, 0)    #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        Tree_positions6 = [[5,6,7,8,5,6], [16,17,18,19,5,6], [28,29,30,31,5,6], [40,41,42,43,5,6], [52,53,54,55,5,6]]
        for i, item in enumerate(Tree_positions6):
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds[one+row*60] = (255,0,0)         #Red
                    leds1[one+row*60] = (0,255,0)        #Green
                    leds2[one+row*60] = (255,0,255)      #Violet
                    leds3[one+row*60] = (255,255,0)      #Yellow
                    leds4[one+row*60] = (0,0,255)        #Blue
                    leds5[one+row*60] = (254,127,156)    #Pink

        for i in range(3):                         #Terminate the christmas tree 4 times with 6 different colours (Mentioned above)
            client.put_pixels(leds)                #Draw a LED pixel in the frame [client.put_pixels] and implement the colour [(leds)].
            sleep(0.5)                             #Sleep by 0.5 seconds
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

           # client.close()
        

#================================ Flag ==========================================#

    def Flag(self):                             #Defining Flag self function
        leds1 =[(0,0,0)]*360                    #Variables names for deining the colour frame.               
        leds2 =[(0,0,0)]*360
        leds3 =[(0,0,0)]*360
        Green = (0,255,0)

        flag_positions1 = [[0,1,2,3,0,5,0,0,255,0.2], [3,4,5,6,0,5,255,255,0,0.2], [6,7,8,9,0,5,255,0,0,0.2], [9,10,11,12,0,5,255,255,255,0.2],
                          [12,13,14,15,0,5,255,165,0,0.2], [15,16,17,18,0,1,0,0,255,0.2], [15,16,17,18,1,2,255,255,0,0.2], [15,16,17,18,2,3,255,0,0,0.2], 
                          [15,16,17,18,3,4,255,255,255,0.2], [15,16,17,18,4,5,255,165,0,0.2]]     
                          #Make a variable as Flag_position1 to give the first line led position by an array by implementing both coloutr sleepinmg time. 
        for i, item in enumerate(flag_positions1):                     #Implementing first tree list to the python's enumerate() to get a counter and the value from the iterable at the same time.
            for one in range(item[0], item[3]):                        #Column
                for row in range(item[4], item[5]):                    #Rnage of the row using for loop
                    leds1[one+row*60] = (item[6], item[7], item[8])    #Implementing the colour by specifically identifying the row and column part (Calculation part) 
                client.put_pixels(leds1)
                sleep(item[9])                                         #Implement the sleep from the above array list using the item.

        
        heart = [[24,25,26,27,28,0,1], [32,33,34,35,36,0,1]]
        for i, item in enumerate(heart):
            for one in range(item[0], item[4]):
                for row in range(item[5], item[6]):
                    leds3[one+row*60] = Green                 #                   
                client.put_pixels(leds3)
                sleep(0.2)

        heart = [[23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,1,2]]
        for i, item in enumerate(heart):
            for one in range(item[0], item[14]):
                for row in range(item[15], item[16]):
                    leds3[one+row*60] = Green
                client.put_pixels(leds3)
                sleep(0.2)

        heart = [[23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,2,3]]
        for i, item in enumerate(heart):
            for one in range(item[0], item[14]):
                for row in range(item[15], item[16]):
                    leds3[one+row*60] = Green
                client.put_pixels(leds3)
                sleep(0.2)

        heart = [[25,26,27,28,29,30,31,32,33,34,35,3,4]]
        for i, item in enumerate(heart):
            for one in range(item[0], item[10]):
                for row in range(item[11], item[12]):
                    leds3[one+row*60] = Green
                client.put_pixels(leds3)
                sleep(0.2)

        heart = [[27,28,29,30,31,32,33,4,5]]
        for i, item in enumerate(heart):
            for one in range(item[0], item[6]):
                for row in range(item[7], item[8]):
                    leds3[one+row*60] = Green
                client.put_pixels(leds3)
                sleep(0.2)
                    
        heart = [[29,30,31,5,6]]
        for i, item in enumerate(heart):
            for one in range(item[0], item[2]):
                for row in range(item[3], item[4]):
                    leds3[one+row*60] = Green
                client.put_pixels(leds3)
                sleep(0.2)

                
        flag_positions2 = [[57,58,59,60,0,5,0,0,255,0.2], [54,55,56,57,0,5,255,255,0,0.2], [51,52,53,54,0,5,255,0,0,0.2],
                          [48,49,50,51,0,5,255,255,255,0.2], [45,46,47,48,0,5,255,165,0,0.2], [42,43,44,45,0,1,0,0,255,0.2], [42,43,44,45,1,2,255,255,0,0.2],
                          [42,43,44,45,2,3,255,0,0,0.2], [42,43,44,45,3,4,255,255,255,0.2], [42,43,44,45,4,5,255,165,0,0.2]]
        for j, item in enumerate(flag_positions2): 
            for one in range(item[0], item[3]):
                for row in range(item[4], item[5]):
                    leds2[one+row*60] = (item[6], item[7], item[8])
                client.put_pixels(leds2)
                sleep(item[9])


        for i in range(3):
            client.put_pixels(leds1)
            sleep(0.5)
            client.put_pixels(leds2)
            sleep(0.5)
            client.put_pixels(leds3)
            sleep(0.5)
            

#============================== Star ========================================#
    
    def Blink(Self):                                #Defining Star self function

        numStrings = 8                              #Make a varible as numStrings and then it equal to 8.
        
        string = [ (0,0,0) ] * 64                   #The gap of the each row (64)

        for j in range(8):                          #The LED bulbs light up within range of 8.
            string[8 * j] = (0, 255, 0)             #Implementing green colour to light up within a range of 8. 
        led_color = string * numStrings             #Lighting up all the colours in the LED frame

        for j in range(8):
            string[8 * j] = (255, 0, 0)            #Red
        led_color1 = string * numStrings

        for j in range(8):
            string[8 * j] = (255, 140, 0)          #Orange
        led_color3 = string * numStrings

        for j in range(3):                         #Terminating 3 times
            client.put_pixels(led_color)           #
            sleep(0.5)
            client.put_pixels(led_color1)
            sleep(0.5)
            client.put_pixels(led_color3)
            sleep(0.5)         


#=============================== Random - Dark ===================================#

    def Random_Dark (self):                    #Defining Dark self function
        Turns=0                                #Make a variable as Turns and then equals to Zero
        while Turns<=2:                        #While the turns less than or equal to 2, the loop is terminating
            led = 0                            #Variable led equals to zero. 
            while led<60:                      #While number of LEDs less than 60, the loop is terminating else it stops.
                for rows in range(6):          #
                    led_color = (106 * ((led / 30) - 0.00001), 90 * ((led / 30) - 1), 205 * ((led / 30)- 2))   #Implementing the colour and reducing the brightness using a calculation part   
                    led_frame[59-led + rows*60] = led_color                      #Terminating the LED code from ending point to the starting point. (Reversing from 59 to 0) 
                sleep(0.1)
                client.put_pixels(led_frame)
                led = led + 1                   #or reverse if you want

            led = 0
            while led<60:
                for rows in range(6):
                    led_color = (106 * ((led / 30) - 0.00001), 90 * ((led / 30) - 1), 205 * ((led / 30)- 0.00003))
                    led_frame[led + rows*60] = led_color                         # Start to end
                sleep(0.1)
                client.put_pixels(led_frame)
                led = led + 1                    #or reverse if you want

            Turns = Turns+1


# ========================== Iterations=====================#

    def iterations(self):                                 #Defining Iterations self function
        numLEDs = 360                                     #Variable 
        yelloshade = (255 * ((numLEDs / 10) - 0.2), 128 * ((numLEDs/ 10) - 0.2), 0)   #

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
                sleep(0.01)
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

#============================= Blinking ========================#

    def Blinking(self):                           #Defining Blinking self function

        for i in range(3):
            for strip2 in range(8):
                pixels2 = [ (90,0,90) ] * 512
                for j in range(32):
                    pixels2[strip2 * 64 + j * 2] = (200,200,200)

                client.put_pixels(pixels2)
                sleep(0.5)

            for strip in range(8):
                pixels1 = [ (90,0,90) ] * 512
                for i in range(32):
                    pixels1[strip * (-64) - i * 2] = (200,200,200)

                client.put_pixels(pixels1)
                sleep(0.5)

#=========================== Mid Reverse =========================#

    def Mid_Reverse(self):                                       #Defining Mid Reverse self function
        for i in range(3):
            led = 0
            while led<30: #scroll all rows at the same time
                led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.1), 205 * ((led / 30)- 0.2))
                for rows in range(6): #first three rows left to right
                    leds[29-led + rows*60] = led_color
                for rows in range(6):
                    leds[30+led + rows* 60] = led_color
                client.put_pixels(leds)
                sleep(.1)
                led = led + 1

            led = 0
            while led<=30:
                for rows in range(6):
                    led_color = (106 * ((led / 30) - 0.01), 90 * ((led / 30) - 0.1), 205 * ((led / 30)- 0.2))
                    leds[led + rows*60] = led_color
                    leds[59-led + rows*60] = led_color
                sleep(.1)
                client.put_pixels(leds)
                led = led + 1 #or reverse if you want

            led = 0
            while led<30: #scroll all rows at the same time
                led_color2 = (255 * ((led / 30) - 0.01), 140 * ((led / 30) - 0.1), 0)
                for rows in range(6): #first three rows left to right
                    leds[29-led + rows*60] = led_color2
                for rows in range(6):
                    leds[30+led + rows* 60] = led_color2
                client.put_pixels(leds)
                sleep(.1)
                led = led + 1

            led = 0
            while led<=30:
                for rows in range(6):
                    led_color2 = (255 * ((led / 30) - 0.01), 140 * ((led / 30) - 0.1), 0)
                    leds[led + rows*60] = led_color2
                    leds[59-led + rows*60] = led_color2
                sleep(.1)
                client.put_pixels(leds)
                led = led + 1 #or reverse if you want


#==================  Covid 19 ===========================#

    def Covid(self):                                                 #Defining Covid-19 self function
        
        temp = float(input("Enter your Body tempreture: "))
        fever = int(input("How many days did you have fever : "))
        cough = int(input("How many days did you have dry cough: "))


        if (temp>35 and fever>3 and cough>3):
            print("Your Body tempreature is " + str(temp))
            print("Days of Fever is :" + str(fever))
            print("Days of Dry cough is:" + str(cough))
            print("You are positive with Coroana Virus")

            
            led = 0
            while led<60:
                for rows in range(6):
                    led_frame[led + rows*60] = (255,0,0)
                sleep(.1)
                client.put_pixels(led_frame)
                led = led + 1                               #or reverse if you want
             
            led = 0
            while led<60:
                for rows in range(6):
                    led_frame[59-led + rows*60] = (0,0,0)
                sleep(.1)
                client.put_pixels(led_frame)
                led = led + 1                              #or reverse if you want


            for sign in range (0,1):
                for rows in range(0,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (1,4):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (1,4):
                for rows in range(3,4):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (4,5):
                for rows in range(1,2):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (4,5):
                for rows in range(2,3):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (7,8):
                for rows in range(1,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (9,11):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (9,11):
                for rows in range(5,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (12,13):
                for rows in range(1,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (15,19):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (15,19):
                for rows in range(3,4):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (15,19):
                for rows in range(5,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (15,16):
                for rows in range(1,3):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (18,19):
                for rows in range(4,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (21,26):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (21,26):
                for rows in range(5,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (23,24):
                for rows in range(1,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (28,33):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (30,31):
                for rows in range(1,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (35,40):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (35,40):
                for rows in range(5,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (37,38):
                for rows in range(1,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (42,43):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (43,44):                           
                for rows in range(1,2):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (44,45):                           
                for rows in range(2,3):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (45,46):                           
                for rows in range(3,4):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (46,47):                           
                for rows in range(4,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (47,48):                           
                for rows in range(5,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (48,49):                           
                for rows in range(4,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (49,50):                           
                for rows in range(3,4):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (50,51):                           
                for rows in range(2,3):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (51,52):                           
                for rows in range(1,2):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (52,53):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (54,60):
                for rows in range(0,1):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (54,60):
                for rows in range(3,4):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (54,60):
                for rows in range(5,6):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (54,55):
                for rows in range(1,3):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (54,55):
                for rows in range(4,5):
                    leds[sign +rows*60] = (255,0,0)
                client.put_pixels(leds)
                sleep(.1)

            
        else:
            print("Your Body tempreature is " +str(temp))
            print("Days of Fever is :" +str(fever))
            print("Days of Dry cough is:" + str(cough))
            print(" You are Negetive with Corona Virus")

               
            led = 0
            while led<60:
                for rows in range(6):
                    led_frame[led + rows*60] = (0,255,0)
                sleep(.1)
                client.put_pixels(led_frame)
                led = led + 1                                  #or reverse if you want
             
            led = 0
            while led<60:
                for rows in range(6):
                    led_frame[59-led + rows*60] = (0,0,0)
                sleep(.1)
                client.put_pixels(led_frame)
                led = led + 1                                  #or reverse if you want

            for sign in range (0,1):
                for rows in range(0,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (5,6):
                for rows in range(0,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (1,2):
                for rows in range(1,2):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (2,3):
                for rows in range(2,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (3,4):
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (4,5):
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (8,13):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (8,13):
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (8,13):
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (8,9):
                for rows in range(1,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (8,9):
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (15,20):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (15,16):
                for rows in range(1,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (16,20):
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (16,20):
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (19,20):
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (21,22):
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (22,23):
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (23,24):
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (24,25):
                for rows in range(2,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (25,26):
                for rows in range(1,2):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (26,27):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (27,28):
                for rows in range(1,2):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (28,29):
                for rows in range(2,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (24,30):
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (30,31):
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (31,32):
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (33,34):
                for rows in range(1,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (32,35):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (36,41):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (36,41):
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (38,39):
                for rows in range(1,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (42,43):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (43,44):                           
                for rows in range(1,2):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (44,45):                           
                for rows in range(2,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (45,46):                           
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (46,47):                           
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (47,48):                           
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (48,49):                           
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (49,50):                           
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (50,51):                           
                for rows in range(2,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (51,52):                           
                for rows in range(1,2):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (52,53):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (54,60):
                for rows in range(0,1):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (54,60):
                for rows in range(3,4):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (54,60):
                for rows in range(5,6):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


            for sign in range (54,55):
                for rows in range(1,3):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)

            for sign in range (54,55):
                for rows in range(4,5):
                    leds[sign +rows*60] = (0,255,0)
                client.put_pixels(leds)
                sleep(.1)


#===========================Exit=======================#

    def iExit(self):
        iExit=messagebox.askyesno("Animation Box","Do you want to Exit?")
        if iExit>0:
            root.destroy()
            return

   

root=Tk()
ob=AnimationBox(root)
root.mainloop()
