# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:34:33 2021

"""


import matplotlib.pyplot as plt

# data preperation
x1 = [1,2,3,4,5,6] 
y1 = [5,15,25,30,20,15] 

# plot creation
fig = plt.figure() 

# pos is a three digit integer, where the first digit is the number of rows, 
# the second the number of columns, and the third the index of the subplot. 
# i.e. fig.add_subplot(222) is the same as fig.add_subplot(2, 2, 2). 
# Note that all integers must be less than 10 for this form to work.

ax = fig.add_subplot(221) 

# customize plot 
ax.plot(x1, y1, color='red', linewidth=1)  
ax.scatter([2,4,6], [5,15,25], color='green', marker='*') 
ax.set_xlim(1, 6.5) # the x-axis view limits.

# save plot
plt.savefig('Example_plot.png')

# # The Axes Class contains most of the figure elements: Axis, Tick, 
# # Line2D, Text, Polygon, etc., and sets the coordinate system. 

ax2 = fig.add_subplot(222) 
#fig, ax2 = plt.subplots(212)
#ax2.plot(x1,y1)   # Draw points with lines or markers connecting them
ax2.scatter(x1,y1)        # Draw unconnected points, scaled or colored

ax3 = fig.add_subplot(223)
# fig3, ax3 = plt.subplots()
ax3.fill(x1,y1,color='blue') # Draw filled polygons

ax4 = fig.add_subplot(224)
ax4.fill_between(x1,y1,color='yellow') # Fill between y-values and 0

fig2, ax5 = plt.subplots()
ax5.hist(y1) # Plot a histogram

fig3, ax6 = plt.subplots()
ax6.boxplot(y1) # Make a box and whisker plot

#show plot
plt.show()