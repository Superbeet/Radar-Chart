'''
Created on Jun 20, 2014

@author: 507061
'''
import matplotlib.pyplot as plt
import numpy as np
import time

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

fig, axes = plt.subplots(nrows=6)

styles = ['r-', 'g-', 'y-', 'm-', 'k-', 'c-']
def plot(ax, style):
    print ax.plot(x, y, style, animated=True)[0]
    return ax.plot(x, y, style, animated=True)[0]

# Let's capture the background of the figure
backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]

fig.show()

# We need to draw the canvas before we start animating...
fig.canvas.draw()

tstart = time.time()

lines = [plot(ax, style) for ax, style in zip(axes, styles)]

for i in xrange(1, 2000):
    items = enumerate(zip(lines, axes, backgrounds), start=1)
    for j, (line, ax, background) in items:
        fig.canvas.restore_region(background)
        line.set_ydata(np.sin(j*x + i/10.0))
        ax.draw_artist(line)
        fig.canvas.blit(ax.bbox)

print 'FPS:' , 2000/(time.time()-tstart)