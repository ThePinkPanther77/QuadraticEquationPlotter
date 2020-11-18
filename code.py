from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

y=list()

class Graph:
    '''A class for ploting a quadratic equation.'''
    def __init__(self,a,b,c,minn,maxx):
        self.a=a
        self.b=b
        self.c=c
        self.minn=minn
        self.maxx=maxx

    def creator(self):
        '''A method that creates the graph and adjust the axis. '''
        x=np.linspace(self.minn,self.maxx)
        for i in x:
            y.append((self.a*i*i)+(self.b*i)+self.c)
        fig = plt.figure()
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)
        ax.axis['xzero'].set_visible(True)
        ax.axis['yzero'].set_visible(True)
        for i in ["left", "right", "bottom", "top"]:
                ax.axis[i].set_visible(False) 
        plt.plot(x,y)
        plt.show()

def main():
    '''A function the initializes the calss (Graph).'''
    print('Enter the parameters:')
    a,b,c=map(int,input().split())
    print('Enter the minimum and maximum values of x (respectively):')
    minn,maxx=map(int,input().split())
    p=Graph(a,b,c,minn,maxx)
    p.creator()

if __name__ == "__main__":
    main()
