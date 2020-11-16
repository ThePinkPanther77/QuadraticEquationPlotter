from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

y=list()
a,b,c=map(int,input().split())
minn,maxx=map(int,input().split())
x=np.linspace(minn,maxx)
for i in x:
    y.append((a*i*i)+(b*i)+c)

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
ax.axis['xzero'].set_visible(True)
ax.axis['yzero'].set_visible(True)
for i in ["left", "right", "bottom", "top"]:
    ax.axis[i].set_visible(False) 
   
plt.plot(x,y)
plt.show()


