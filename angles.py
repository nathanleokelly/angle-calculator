import math
#import numpy as np
import matplotlib.pyplot as mpl

def sin_calc(start, end, step):
    y_values = []
    x_values = []
    for x in range(start * 10, end * 10, step):
        x_val = x/10
        x_values.append(x_val) 
        sin_val = math.sin(x_val)
        y_values.append(sin_val)
    # Draw  horizontal axis
    mpl.plot([-5.1,5.1],[0,0])
    # Draw  vertical axis
    mpl.plot([0,0],[-1.1,1.1])
    mpl.plot(x_values, y_values)
    mpl.show()
sin_calc(-10, 10, 1)