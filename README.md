# README File for Python LED FADECANDY Assessment

# My_Fadecandy_2022

My project consists of a tiny interesting playing item that people of all ages can enjoy when they have free time or when they are bored. 

There are nine main types of animations in the graphical user interface (Animation Box).

There are eight animations with image buttons; once the user click the button, the simulator gives an appealing animation for the user.

At the end, there is a 'Test Me' button to see whether the coronavirus, which isexceedingly harmful these days, is positive or negative. The result is shown in the console after we press the button, so once the user enter the body temperature, cough days, and fever days, the simulator displays the output with a beautiful animation.

The user would be able to select the animation as their desire to view the animation in the simulator.

The simulator has been connected using the graphical UI (User Interface) and the Console (Terminal) to produce various animations. 

The user interface has an exit button at the bottom of the GUI. When the user presses the exit button, a message box appears asking "Do you want to exit?". The user can press yes to exit the UI or no to continue in the UI.

The sizes of the image buttons and text buttons have been set, so that the user can see them clearly and learn a little about the animation style.



# Version 01
-

# Simulator

The simulator provided has 360 leds arranged in a grid pattern of 6 rows with 60 leds each.

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
