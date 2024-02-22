import math
#import numpy as np
import matplotlib.pyplot as mpl

def draw():
    wave_calc("sin", -10, 10, 1)
    wave_calc("cos", -10, 10, 1)
    mpl.show()

def wave_calc(type, start, end, step):
    y_values = []
    x_values = []
    for x in range(start * 100, end * 100, step):
        x_val = x/100
        x_values.append(x_val) 
        if type == 'sin':
            val = math.sin(x_val)
        else:
            val = math.cos(x_val)
        y_values.append(val)
    # Draw  horizontal axis
    mpl.plot([-5.1,5.1],[0,0])
    # Draw  vertical axis
    mpl.plot([0,0],[-1.1,1.1])
    mpl.plot(x_values, y_values)

draw()