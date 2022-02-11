# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:47:03 2020

"""
import csv
import matplotlib.pyplot as plt
import numpy as np
img=plt.imread("SatIvry.png")
fig, ax = plt.subplots()
ax.imshow(img,extent=[2.382,2.394, 48.811,48.815])
GPS={}
m=["+","x","v"]
for a in range(0,3):
    lcor=[]
    lat=[]
    long=[]
    with open('tracesGPS'+str(a+1)+'.csv',"r") as gps:
        path= csv.reader(gps, delimiter=',')
        for row in path:
            if row ==['latitude', 'longitude', 'altitude', 'accuracy', 'time']:
                pass
            else :
                lcor.append(row)
                lat.append(float(row[0]))
                long.append(float(row[1]))
        #GPS["file"+str(a+1)]=lcor
    ax.plot(long,lat, marker=m[a])
    gps.close()

ax.grid()
plt.title("IPSA trajet métro-école")
plt.xlabel('Longitudes')
plt.ylabel('Latitudes')
#plt.imshow(img)
plt.show()
# print(GPS)