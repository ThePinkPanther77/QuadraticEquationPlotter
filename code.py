from tkinter import *
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    '''A class for ploting a quadratic equation.''' 
    def __init__(self,root):
        self.root=root
        root.title("Quadratic Equation Plotter")
        icon = PhotoImage(file = 'Quadratic Equation Plotter.gif')
        root.iconphoto(False, icon) 

        self.label1=Label(root,text="Enter the first parameter:")
        self.box1=Entry(root,width=50)

        self.label2=Label(root,text="Enter the second parameter:")
        self.box2=Entry(root,width=50)

        self.label3=Label(root,text="Enter the third parameter:")
        self.box3=Entry(root,width=50)

        self.label4=Label(root,text="Enter the minimum value of x:")
        self.box4=Entry(root,width=50)

        self.label5=Label(root,text="Enter the maximum value of x:")
        self.box5=Entry(root,width=50)

        self.button=Button(root,text="Enter",command=self.Input)

        root.bind('<Return>',self.Input)

        self.label1.grid(row=1,column=1)
        self.label2.grid(row=3,column=1)
        self.label3.grid(row=5,column=1)
        self.label4.grid(row=7,column=1)
        self.label5.grid(row=9,column=1)

        self.box1.grid(row=2,column=1)
        self.box2.grid(row=4,column=1)
        self.box3.grid(row=6,column=1)
        self.box4.grid(row=8,column=1)
        self.box5.grid(row=10,column=1)

        self.button.grid(row=11,column=1)

    def creator(self,a,b,c,minn,maxx):
        '''A method that creates the graph and adjust the axis.'''
        y=list()
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

    def Input(self,event=None):
        a=int(self.box1.get())
        b=int(self.box2.get())
        c=int(self.box3.get())
        minn=int(self.box4.get())
        maxx=int(self.box5.get())
        self.creator(a,b,c,minn,maxx)

def Main():
    '''A function that creates the GUI and initializes the calss (Graph).'''
    R =Tk()
    p=Graph(R)
    R.mainloop()

if __name__ == "__main__":
    Main()
