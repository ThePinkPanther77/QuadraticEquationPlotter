from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

y=list()

class Graph:
    '''A class for ploting a function.'''
    def __init__(self,a,b,c,minn,maxx):
        '''The class constructor.'''
        self.a=a
        self.b=b
        self.c=c
        self.minn=minn
        self.maxx=maxx

    def creator(self):
        x=np.linspace(self.minn,self.maxx)
        #Making an array that contains the values of x 
        for i in x:
            y.append((self.a*i*i)+(self.b*i)+self.c)
        #Making an array that contains the values of y for each x
        fig = plt.figure()
        #Creating the plot figure
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)
        ax.axis['xzero'].set_visible(True)
        ax.axis['yzero'].set_visible(True)
        for i in ["left", "right", "bottom", "top"]:
                ax.axis[i].set_visible(False) 
        #Adjusting the axis
        plt.plot(x,y)
        plt.show()
        #Showing the plot


def main(a,b,c,minn,maxx):
    '''
    The function that initializes the Graph class.

    a -- the first parameter
    b -- the second parameter
    c -- the third parameter
    minn -- the minimum value of x
    maxx -- the maximum value of x
    '''
    p=Graph(a,b,c,minn,maxx)
    p.creator()

print('Enter the parameters:')
a,b,c=map(int,input().split())
print('Enter the minimum and maximum values of x (respectively):')
minn,maxx=map(int,input().split())
main(a,b,c,minn,maxx)
