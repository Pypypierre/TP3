# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:52:57 2021

"""

import matplotlib.pyplot as plt

# plot creation
fig = plt.figure() 
ax = fig.add_subplot(111) 

# Limits & Autoscaling

ax.axis('equal') # Set the aspect ratio of the plot to 1
ax.set(xlim=[1,1.5],ylim=[-1.5,1.5]) # Set limits for x-and y-axis

# Legends

ax.set(title='An Example Axes', ylabel='Y-Axis', xlabel='X-Axis') #Set a title and x-and y-axis labels

# Ticks

ax.xaxis.set(ticks=range(1,5), ticklabels=[3,30,-5,"hello"]) # Manually set x-ticks
ax.tick_params(axis='y', direction='inout', length=10)    # Make y-ticks longer and go in and out

plt.show()
