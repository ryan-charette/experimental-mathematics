import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

f = lambda r, x: r*x*(1-x)

x_0_init = random.random()
r_init = 0.5
x = [0]
fx = [x_0_init]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(x, fx)

ax_r = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_r = Slider(ax_r, 'r', 0.0, 4.0, valinit=r_init)
ax_x0 = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_x0 = Slider(ax_x0, 'x0', 0.0, 1.0, valinit=x_0_init)

def update(val):
    r = slider_r.val
    x_0 = slider_x0.val
    x = [0]
    fx = [x_0]
    for n in range(1, 1_500):
        x.append(n)
        fx.append(f(r, fx[n-1]))
    line.set_data(x, fx)
    ax.relim()
    ax.set_ylim([0, 1])
    ax.autoscale_view()
    fig.canvas.draw_idle()

slider_r.on_changed(update)
slider_x0.on_changed(update)

plt.show()