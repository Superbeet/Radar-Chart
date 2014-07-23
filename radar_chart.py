import matplotlib.pyplot as plt
import numpy as np
import time

# x = np.arange(-180.0,190.0,10)
# theta = (np.pi/180.0 )*x    # in radians
# 
# offset = 2.0
# 
# R1 = [-0.358,-0.483,-0.479,-0.346,-0.121,0.137,0.358,0.483,0.479,0.346,0.121,\
# -0.137,-0.358,-0.483,-0.479,-0.346,-0.121,0.137,0.358,0.483,0.479,0.346,0.121,\
# -0.137,-0.358,-0.483,-0.479,-0.346,-0.121,0.137,0.358,0.483,0.479,0.346,0.121,\
# -0.137,-0.358]
# 
# fig1 = plt.figure()
# ax1 = fig1.add_axes([0.1,0.1,0.8,0.8],polar=True)
# ax1.set_rmax(1)
# ax1.plot(theta,R1,lw=2.5)
# plt.show()




# x = np.arange(-90.0,95.0,5)
# # x = [-180. -170. -160. -150. -140. -130. -120. -110. -100.  -90.  -80.  -70.
# #   -60.  -50.  -40.  -30.  -20.  -10.    0.   10.   20.   30.   40.   50.
# #    60.   70.   80.   90.  100.  110.  120.  130.  140.  150.  160.  170.
# #   180.]
# 
# theta = (np.pi/180.0 )*x    # in radians
# 
# offset = 2.0
# 
# R2 = [1.642,1.517,1.521,1.654,1.879,2.137,2.358,2.483,2.479,2.346,2.121,1.863,\
# 1.642,1.517,1.521,1.654,1.879,2.137,2.358,2.483,2.479,2.346,2.121,1.863,1.642,\
# 1.517,1.521,1.654,1.879,2.137,2.358,2.483,2.479,2.346,2.121,1.863,1.642]
# 
# fig2 = plt.figure()
# ax2 = fig2.add_axes([0.1,0.1,0.8,0.8],polar=True)
# ax2.plot(theta,R2,lw=2.5) 
# ax2.set_rmax(1.5*offset)
# plt.show()

radian_unit = np.pi/180

offset = 2.0
xAxis_1 = [0 for i in range(500)]
yAxis_1 = np.arange(0,5,0.01)

fig2 = plt.figure()
#rect = l,b,w,h
ax2 = fig2.add_axes([0.1,0.1,0.8,0.8],polar=True)
ax2.plot(xAxis_1,yAxis_1,lw=2.5) 
ax2.set_rmax(1.5*offset)

xAxis_2 = [radian_unit*45 for i in range(500)]
yAxis_2 = np.arange(0,5,0.01)

ax2 = fig2.add_axes([0.1,0.1,0.8,0.8],polar=True)
ax2.plot(xAxis_2,yAxis_2,lw=2.5) 
ax2.set_rmax(1.5*offset)

# style = 'r-'
# x = np.arange(0, 2*np.pi, 0.1)
# y = np.sin(x)
# line = ax2.plot(x, y, style, animated=True)[0]
# line.set_ydata(np.sin(j*x + i/10.0))

plt.show()