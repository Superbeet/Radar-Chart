'''
Created on Jul 22, 2014

@author: 507061
'''
# Working flow
# 1.Program the backgroud
# 2.Program layers
# 3.Program marks

import numpy as np
import matplotlib.pyplot as plt

#Create radius and theta arrays, and a 2d radius/theta array
radius = np.linspace(0.5,1,100)
theta = np.linspace(0,2*np.pi,100)  #100 slices
print theta

R,T  = np.meshgrid(radius,theta)

#Calculate some values to plot
Zfun = lambda R,T: R**2*np.cos(T)
Z = Zfun(R,T)   #color

#Create figure and polar axis
fig = plt.figure()
ax = fig.add_subplot(111, polar = True)

#-----------------------------------------------------------------------------------
#Plot flexible graphs
ax.pcolor(T,R,Z)    #Plot calculated values

#-----------------------------------------------------------------------------------
#Plot thick red section and label it
theta = np.linspace(0,np.pi/4,21) #this is a line
ax.plot(theta,[1.23 for t in theta],color='#AA5555',linewidth=10)   #Colors are set by hex codes

#-----------------------------------------------------------------------------------
#Plot bar chats
rect = plt.bar(left = (0,1,2),height = (0.5,1,1.5),color='#AA5555',width = 0.35,align="center")

#-----------------------------------------------------------------------------------


ax.text(np.pi/8,1.25,"Text")

ax.set_rmax(1.5)   #Set maximum radius

#Turn off polar labels
ax.axes.get_xaxis().set_visible(False)
# ax.axes.get_yaxis().set_visible(False)

plt.show()