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
- Define a functions for all the animations and give the command to the button to run in the opc simulator.
- 


# Basic commands

opc.Client() - Sets up a client object that will establish communication between Python and a fadecandy server.

Required argument: an IP or localhost with correct port for the server.
```
.put_pixels(list) - places a list of tuples with rgb values to the fadecandy server to be displayed.

Format: [(R_value, G_value, B_value)]. Each tuple element in the list represents a single led.
```

There are a few more methods for ensuring connection and disconnect procedures, but they will not be needed with the simulator.

###### Notes

To connect to the simulator, use localhost with port 7890 when setting up your fadecandy instance in Python: 
```
client = opc.Client('localhost:7890')
```

When not using a loop, perform .put_pixels() twice to avoid interpolation issues:
```
client.put_pixels(list)
client.put_pixels(list)
```

It's highly recommended to perform any colour fading in an HSV space as opposed to RGB. Refer to the '4_hsv_rainbow.py' and 'hsv_rainbow_rolling.py' examples. Keep Value (saturation) max to begin with, play with the value for more pastel, washed out colours.  

## Other files

- 60by6.jpg - use this as a template to easily plan templates and check led numbers.
- colour spaces.pdf - basic information on the difference between RGB and HSV. 
- Fadecandy exercises.pdf - some simple tasks to get you started.
