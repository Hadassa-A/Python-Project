try:
    import numpy as np
except:
    import math as np

def sinx_x(x):
    """
    :param x: numerical value
    :return: sin(x)/x
    in case of x==0 return 1
    """
    try:
        if x==0:
            return 1
        return np.sin(x)/x
    except Exception as e:
        return f"Error: {e}"

def cosx_x(x):
    """
    :param x: numerical value
    :return: cos(x)/x
    in case of x==0 return 1
    """
    try:
        if x==0:
            return 1
        return np.cos(x)/x
    except Exception as e:
        return f"Error: {e}"

# Create a list with values from -100 to 100 (inclusive) with a step of 0.01
t = np.arange(-100,100.01,0.01)
# list comprehension
sinx = [sinx_x(x) for x in t]
cosx = [cosx_x(x) for x in t]



