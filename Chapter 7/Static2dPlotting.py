from pprint import pprint

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

mpl.rcParams['font.family'] = 'serif'

# %matplotlib inline
# When using py notebook this ^ can show plot inline instead of pop-up

np.random.seed(1000) # set a fix seed for randomization
y= np.random.standard_normal(20) # draw 2 random numbers
x= np.arange(len(y)) # return evenly spaced values within a given interval
plt.plot(x, y)
plt.show()

# customise plot
plt.figure(figsize=(10, 6))
plt.plot(y.cumsum(), 'b', lw=1.5) # Plots the data as a line in blue with line width of 1.5 points.
plt.plot(y.cumsum(), 'ro') # Plots the data as red (thick) dots.
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()

y = np.random.standard_normal((20, 2)).cumsum(axis=0) # Generate 2 datasets
pprint(y)
# Visualise 2 data sets in single graph
plt.figure(figsize=(10, 6))
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 1], lw=1.5, label='2nd')
plt.legend(loc=0) # place legend in the "best" location
plt.plot(y, 'ro')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show()

# SCALING DATA PROBLEMS
y[:, 0] = y[:, 0] * 100 # Rescale dataset to 100x
plt.figure(figsize=(10, 6))
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 1], lw=1.5, label='2nd')
plt.plot(y, 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.show() # 1st data looks like a straight line

# SCALING DATA SOLUTION 1: ADD 2 SCALE AXES
fig, ax1 = plt.subplots() # Defines the figure and axis objects.
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=8)
plt.xlabel('index')
plt.ylabel('value 1st')
plt.title('A Simple Plot')
ax2 = ax1.twinx() # Creates a second axis object that shares the x-axis.
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.ylabel('value 2nd')
plt.show()

# SCALING DATA SOLUTION 1: ADD 2 SEPARATE SUBPLOTS
plt.figure(figsize=(10, 6))
# subplot arguments are three integers for numrows, numcols, and fignum (either separated by commas or not)
plt.subplot(211) # Defines the upper subplot 1.
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=0)
plt.ylabel('value')
plt.title('A Simple Plot')
plt.subplot(212) # Defines the lower subplot 2.
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.show()


# OTHER PLOTTING STYLES

# Scatter Plot
y = np.random.standard_normal((1000, 2))
c = np.random.randint(0, 10, len(y))
plt.figure(figsize=(10, 6))
plt.scatter(
    y[:, 0], # scatter plot first dataset
    y[:, 1], # scatter plot second dataset
    c=c, # add the third (colour) dataset
    cmap='coolwarm',
    marker='o'
)
plt.colorbar()
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(y, label=['1st', '2nd'], bins=25) # Histogram plot produced via the plt.hist() function.
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()

# Mathematically Inspired Plot
def func(x):
    return 0.5 * np.exp(x) + 1
a, b = 0.5, 1.5 # The integral limits.
x = np.linspace(0, 2) # The x values to plot the function.
y = func(x) # The y values to plot the function.
Ix = np.linspace(a, b) # The x values within the integral limits.
Iy = func(Ix) # The y values within the integral limits.
# The list object with multiple tuple objects representing coordinates for the polygon to be plotted.
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]

ig, ax = plt.subplots(figsize=(10, 6))
plt.plot(x, y, 'b', linewidth=2) # Plots the function values as a blue line
plt.ylim(bottom=0) # Defines the minimum y value for the ordinate axis.

# Plots the polygon (integral area) in gray.
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
ax.add_patch(poly)

# Places the integral formula in the plot (LaTeX label)
plt.text(0.5 * (a + b), 1, r'$\int_a^b f(x)\mathrm{d}x$', horizontalalignment='center', fontsize=20)

# Places the axis labels.
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')

# Places the x labels.
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))

# Places the y labels.
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$f(b)$'))
plt.show()