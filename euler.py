# euler.py
# author: Renata Paramastri
# Solves ODEs using Euler's method and plots the solution

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# figure appearance
GRAPH_BOTTOM = 0.2
SLIDER_LEFT = 0.25
SLIDER_BOTTOM = 0.03
SLIDER_HEIGHT = 0.03
SLIDER_WIDTH = 0.65
STYLE = "seaborn-colorblind"

# math limits
STEP_SIZE_RANGE = (0.01, 1)
Y0_RANGE = (-10, 10)
T_MAX = 5

STEP_SIZE_INIT = 0.1
Y0_INIT = 0

def f(t, y):
    """ Returns y' based on y and the independent variable t. """
    return -2*y + 2 - math.exp(-4*t)

def euler(f, y0, stepSize, tMax):
    """
    Solves an ODE using Euler's method.

    Parameters
    ----------
    f : function
        the function that returns y' based on t and y
    y0 : float
        the initial value at t=0
    stepSize : float
        how much t is incremented for each iteration
    tMax : float
        compute euler's method up to this t

    Returns
    ---------
    y : list
        contains all computed y values (excluding the initial condition)
    """
    tVals = np.arange(0, tMax, stepSize)
    y = []
    for t in tVals:
        slope = f(t, y0)
        y0 += slope * stepSize
        y.append(y0)

    return y

plt.style.use(STYLE)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom = GRAPH_BOTTOM)

tVals = np.arange(0, T_MAX + STEP_SIZE_INIT, STEP_SIZE_INIT)  # include tMax
yVals = [Y0_INIT] + euler(f, Y0_INIT, STEP_SIZE_INIT, T_MAX)

line, = plt.plot(tVals, yVals)
ax.set_xlabel("$t$")
ax.set_ylabel("$y$")

stepAx = plt.axes([SLIDER_LEFT, SLIDER_BOTTOM + SLIDER_HEIGHT + 0.01,
                   SLIDER_WIDTH, SLIDER_HEIGHT])
y0Ax = plt.axes([SLIDER_LEFT, SLIDER_BOTTOM, SLIDER_WIDTH, SLIDER_HEIGHT])

stepSlider = Slider(stepAx, "Step size", *STEP_SIZE_RANGE, valinit=STEP_SIZE_INIT)
y0Slider = Slider(y0Ax, r"$y_0$", *Y0_RANGE, valinit=Y0_INIT)

def update(val):
    stepSize = stepSlider.val
    y0 = y0Slider.val

    newTVals = np.arange(0, T_MAX + stepSize, stepSize)  # include tMax
    newYVals = [y0] + euler(f, y0, stepSize, T_MAX)

    line.set_data(newTVals, newYVals)
    fig.canvas.draw()

stepSlider.on_changed(update)
y0Slider.on_changed(update)

plt.show()

