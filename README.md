# README File for Python LED FADECANDY Assessment

# My Fadecandy 2022

My project consists of a tiny interesting playing item that people of all ages can enjoy when they have free time or when they are bored. 

There are nine main types of animations in the graphical user interface (Animation Box).

There are eight animations with image buttons; once the user click the button, the simulator gives an appealing animation for the user.

At the end, there is a 'Test Me' button to see whether the coronavirus, which is exceedingly harmful these days, is positive or negative. The result is shown in the console after we press the button, so once the user enter the body temperature, cough days, and fever days, the simulator displays the output with a beautiful animation.

The user would be able to select the animation as their desire to view the animation in the simulator.

The simulator has been connected using the graphical UI (User Interface) and the Console (Terminal) to produce various animations. 

The user interface has an exit button at the bottom of the GUI. When the user presses the exit button, a message box appears asking "Do you want to exit?". The user can press yes to exit the UI or no to continue in the GUI.

The sizes of the image buttons and text buttons have been set, so that the user can see them clearly and learn a little about the animation style.

Python version 3.8 or 3.10 can be used to run the code in the opc simulator

# OPC Simulator

- The OPC simulator has provided 360 leds arranged in a grid pattern of 6 rows with 60 leds. 
- The output of each code is displaying in the simulator  
- The colours of the simulator frame can be modified as desired by the user.

opc.Client() - Sets up a client object that will establish communication between Python and a fadecandy server.

Required argument: an IP or localhost with correct port for the server.

To connect to the simulator, use localhost with port 7890 when setting up your fadecandy instance in Python: 
```
client = opc.Client('localhost:7890')
```

# Version 01

- To begin, import all of the necessary libraries with a geometry of ("500*600+0+0") to develop the Graphical User Interface (GUI).
~~~
LIBRARIES
from tkinter import *                -  Import all tk libraries to create user interface
from tkinter import Frame            -  Rectangular areas in the screen to organize the layout
from PIL import Image, ImageTk       -  Import image library
from tkinter import messagebox       -  Import messagebox library
~~~

- Create the program title for the GUI as "Animation Box". 
- Create a "Animation Box" label for the GUI's header.

# Version 02

- For each animation, created Eight image buttons and one text button based on the animations that display in the simulator.
- Created an exit button at the bottom of the GUI to destroy the process.
~~~
def iExit(self):                                                      - Defining the exit button
  iExit=messagebox.askyesno("Animation Box","Do you want to Exit?")   - Message box 
  if iExit>0:                                                         - If the exit greater than zero, the result value is true else it's false 
    root.destroy()                                                    - Destroy the root connection for user interface
    return                                                            - Returning the result
 ~~~
- Completed the process of front end developmentation. (Graphical User Interface)

# Version 03

- Created the front-end developing, back-end developing and server connection using opc libraries to create different animations.
~~~
LIBRARIES
import opc                             - import OPC library           
from time import sleep                 - import sleep library from time
import colorsys                        - Import colorsys library
import random                          - Import random library
~~~

- Define the functions and developed the code for the first two animations. (Snake animation and christmas tree animation)
```
def Snake(self): 
def Tree(self): 
```
- The code is connected with the User Interface, and when the user presses the button, the animation appears in the simulator.
```
command=self.Snake   - The command for establishing a link between the GUI and the code.
command=self.Tree
```
- Create the code that will allow the snake to go forward.
- Create the code for the christmas tree to display five times in the simulator using an array list. 
- The code begins to run in the opc simulator once the image button is pressed.
- Add comments to the code to get a better understanding of the code.

# Version 04

- The next threee animations were developed in the code. (Flag, Star, Random dark)
- The Buddhist flag was designed to be displayed only once in the simulator.
- The star code was programmed to blink four times in the simulator at specific locations.
- To transverse ahead and backward, a random dark code was developed. In the beginning, the simulator is darkening, and it is ideally increase the contrast in the display.
- Developed the christmas tree to lit up with five different colours. (Red, Green, Violet, Yellow, Blue, Pink)
```
for i in range(2):                     - Terminate the christmas tree 3 times with 6 different colours (Mentioned above)
  client.put_pixels(leds)              - Draw a LED pixel in the frame 
  sleep(0.5)  
```
- Connect the GUI to the code, and then press the button to simulate the code in the simulator.
- Add comments to the code.
- Uploaded the code to the github.

# Version 05

- Developed the code for iterations, blinking, and mid reverse.
- The simulator outputs a display that changes colours in the simulator, and then there's an animation that reverses the display from the simulator's centre and finally a white LED is moving from starting point to the ending point.
- The blinking code is used to change the simulator's colour to purple, and a white LED appears one after the purple LED, and it dims as the length of the second row grows longer, and the white colour LED dims from the first line.
- The mid reverse code cfreated to scrolls from the simulator's midpoint to the simulator's finishing and starting location with different colours.
- Connected all the animations with GUI to run in the simulator.
- The snake code was developed, and further animations were added to the code, as the simulator turned green once the snake code was completed.
- Another flag was added to the simulator's right side, and both of them were made to consistently light up by a looping animation.
- Added comments to the codes.
- Uploaded all the codes into the github.

# Version 06

- As the final animation, added a test me button to the user interface to check the possibity of coronavirus.
- When the user click the button, there some questions appears in the console about to know the temperature, fever days and the cough days.
- When the user inputs the data in the console, the console returns a result indicating whether the coronavirus is positive or negative.
```
 if (temp>37 and fever>3 and cough>3):            -If temp is greater than 37, fever greater than 3 and dry cough greater than 3, the final printing statment is satisfying 
   print("Your Body tempreature is " + str(temp))
   print("Days of Fever is :" + str(fever))
   print("Days of Dry cough is:" + str(cough))
   print("You are positive with Coroana Virus")
            
 else:                                                      #If if condition is not satisfying.
  print("Your Body tempreature is " +str(temp))
  print("Days of Fever is :" +str(fever))
  print("Days of Dry cough is:" + str(cough))
  print(" You are Negetive with Corona Virus")
 ```

- The opc simulator also gives the output as positive or ngative with a beautiful animation as the result is displayed in the terminal.
- Added comments to the codes.
- Uploaded all the codes into the github.

# Version 07

To finalise all the codes:
- Created a code to reverse the snake animation once it reach to the end poisition of the simulator.
- An animation was added to snake animation, and reduced the brightness and made the frame flash a few times.

- Developed the code to create a green heart in the middle of the simulator, and looped the entire animation three times. 

- Developed the star animation code, which scrolls the first three rows and the final three rows seperately from left to right with two different colours using a loop as the user presses the star image button.

- The random dark animation has been changed to rainbow colours. After pressing the image button, the rainbow colours appear, followed by the other animation in the simulator.
- Format: [(R_value, G_value, B_value)]. Each tuple element in the list represents a single led.

- By following the same thing from bottom to top, reversed the blinking animation.

- Develop the mid-reverse animation, since it reverse by seperating first and last three rows with an attractive colour. 

- Overall, the animation's colours were altered to make it more contrasty.
- Added comments to the codes.
- Uploaded all the codes into the github.

# Version 08

To finalise the assessment:
- A demo and explanation video have been added.
- Added a new branch to github called Harith_Madhushan, which contains the final code and graphics for easy identification.
- The main branch(Default branh) is to check the consistency of the final code in the Github.
- Spelling correctionin the readme file and in the comments in the python code.
- Developed the code and finalised for better formatting of code.
- Removed unnecessary lines from the main code to be shortened.
- Added comments all most all the lines to give a clear understanding for the code.
- Finalised the code.
- Uploaded all the codes into the github.
