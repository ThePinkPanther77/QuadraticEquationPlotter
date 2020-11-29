from tkinter import *
from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np


class Graph:
    '''A class for ploting a quadratic equation.'''
    def __init__(self,a,b,c,minn,maxx):
        self.a=a
        self.b=b
        self.c=c
        self.minn=minn
        self.maxx=maxx

    def creator(self):
        '''A method that creates the graph and adjust the axis.'''
        y=list()
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

def main(event=None):
    '''A function that initializes the calss (Graph).'''
    a=int(box1.get())
    b=int(box2.get())
    c=int(box3.get())
    minn=int(box4.get())
    maxx=int(box5.get())
    p=Graph(a, b, c, minn, maxx)
    p.creator()


root =Tk(className="Quadratic Equation Plotter")
icon = PhotoImage(file = 'Quadratic Equation Plotter.gif')
root.iconphoto(False, icon) 


label1=Label(root,text="Enter the first parameter:")
box1=Entry(root,width=50)

label2=Label(root,text="Enter the second parameter:")
box2=Entry(root,width=50)

label3=Label(root,text="Enter the third parameter:")
box3=Entry(root,width=50)

label4=Label(root,text="Enter the minimum value of x:")
box4=Entry(root,width=50)

label5=Label(root,text="Enter the maximum value of x:")
box5=Entry(root,width=50)

button=Button(root,text="Enter",command=main)

root.bind('<Return>',main)

label1.grid(row=1,column=1)
label2.grid(row=3,column=1)
label3.grid(row=5,column=1)
label4.grid(row=7,column=1)
label5.grid(row=9,column=1)

box1.grid(row=2,column=1)
box2.grid(row=4,column=1)
box3.grid(row=6,column=1)
box4.grid(row=8,column=1)
box5.grid(row=10,column=1)

button.grid(row=11,column=1)

root.mainloop()
