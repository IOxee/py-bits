"""
py-bits: Circle Mouse Movement

This script makes the mouse cursor move in a circle pattern on the screen.
It leverages the 'clicknium' library to control the mouse and uses basic 
trigonometry to calculate the circular path.

Parameters:
- `w`: Defines the number of steps for a complete circle.
- `m`: A factor derived from `w` to scale the circle steps.
- `r`: Radius of the circle.

When executed, the script will indefinitely move the mouse cursor in a circle 
centered around its initial position with a radius `r`.

Dependencies:
- time: To introduce a delay between each step.
- math: For trigonometric calculations.
- clicknium: To control the mouse position.

Usage:
Simply run the script. To stop the mouse movement, interrupt the script 
(e.g., Ctrl+C in the terminal).

Author:
IOxee
"""

from time import sleep
import math
from clicknium import clicknium as cc
def circle():
    a,b = cc.mouse.position()
    w = 20  
    m = (2*math.pi)/w 
    r = 200      

    while 1:    
        for i in range(0, w+1):
            x = int(a+r*math.sin(m*i))  
            y = int(b+r*math.cos(m*i))
            cc.mouse.move(x,y)
            sleep(0.2)

if __name__ == "__main__":
    circle()