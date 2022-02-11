# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:46:09 2020

"""

# Ex 1: 
## 1 - import the numpy and matplotlib.pyplot libraries as following :

import numpy as np
import matplotlib.pyplot as plt
#from scipy.misc import imread

## 2 - define the bounds in x of the figure (i.e. -π and + π) in the
## variables xstt and xend then in y in the variables ystt and yend.

xstt = -np.pi
xend = np.pi
ystt = -1
yend = 1

## 3 - set the precision of the figure in the form of a variable named step which will indicate the size of the interval
## separating two successive values from the values in x for which we will calculate the values y = sin (x) and y = cos (x)
## (for example step = 0.1).

step = 0.1

## 4
lx=np.arange(xstt,xend,step)

## 5
ly= list(map(np.sin,lx))

## 6
plt.plot(lx,ly)

## 7
#plt.show()

## 8
ly2= list(map(np.cos,lx))

## 9 & 10 & 11 & 12
plt.plot(lx,ly2, label="cos(x)")
plt.legend()
plt.grid()
plt.axis([xstt,xend,ystt,yend])
plt.savefig("ex1.png")
plt.show()


