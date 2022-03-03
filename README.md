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


# OPC Simulator

- The OPC simulator has provided 360 leds arranged in a grid pattern of 6 rows with 60 leds. 
- The output of each code is displaying in the simulator  #
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
- Define a functions for first two animations (Snake, christmas tree animations)
- Snake going forward
- Christmas tree develop the code using an array list
- Once the button ptress the code is running in the simulator
- Updated the github with every changes
- Add comments

# Version 04

- Buddhist flag, star blink normally, random dark going forward and backward printed
- Develop the chritsmas tree to constantly light up with different colour
- Compltede the code by connecting the GUI, once we presss the button the code is simulating in the simulator
- Github uploaed
- Add comments

# Version 05

- Iteration , blinking, mid reverse code developed
- Connected with GUI to run in the simulator
- Snake, combined a new code in the snake code, once the snake code finish like to turn the simulaort into green
- Added an another flag in the right side of the simulator and make both of them to constatntly light up by a looping
- Added comments (every version)

# Version 06

- Added a test me button to check the coronavirus
- Once the user click the button, the temp, fever, and cough askig questions in the console, once the user input the values it gives a result saying that its positie o     negative
- If the cough >  (enter numbers)
- While the result is displaying in the terminal, the opc simulator also gives the outpu as positive or ngative with a beautiful animation.
- Github uploaed
- Add comments

# Version 07

- Added an animation for the snake to reverse (direction) the snake.
- added an animation to Reduced the brightness the of the frame in snake
- Added an green heart in the middle of the simulator to animate it and loop the whole animation to animate it three times.
- Number of rows in the range of 6 using a for loop  || Last three rows reversed (right to left) in star
- Changed the animation into rainbow colours. once the image button press comes up the rainbow colours and then the other animation is displaying in the simulator
- Format: [(R_value, G_value, B_value)]. Each tuple element in the list represents a single led.
- Changed the colours of the animation in the blinking animation
- Develop the mid reverse the animation, as at the end it reversing the in the by seperating it only for three rows
- Overall changed the animations colours for high contrast
- Github uploaed
- Add comments
- 


# Version 08

- Added demo and explanation video
- Added a new branch in the github as Harith_Madhushan - the final code and the images commited to identify easily
- Main branch(Default branh) to check the consistency of the final code
- Spelling correction (commentsm readme)
- Better formatting of code
- Removed unnecessary lines from the main code to shortened
- Added comments all most all the lines to give a clear understanding for the code
- Finalised the code





