from array import ArrayType
from tkinter import *
from tkinter import Canvas
import random

# Clearer Ui using ctypes
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.geometry("601x635")
root.title("Random Walker")
root.resizable(1,1)

c = Canvas(root, height=601, width=601, bg='WHITE',borderwidth=0, highlightthickness=0)
c.pack()

def drawGrid(array,no_of_grids):
    size = 600/no_of_grids
    width = 1
    gap = 0
    for i in range(0,int(600/size)):
        for j in range(0,int(600/size)):
            if array[i][j] == 1:
                fill = 'tan3'
                dfill = 'tan4'
                c.create_rectangle(i*size+gap,j*size+gap,i*size+size,j*size+size,width=width,outline="black",fill=fill)
            else:
                fill = 'bisque'
                dfill= 'bisque3'
                c.create_rectangle(i*size+gap,j*size+gap,(i*size+size),(j*size+size),width=width,outline="black",fill=fill,disabledfill=dfill)

def createGrid():
    no_of_grids = 20
    array = [[0 for x in range(no_of_grids)] for x in range(no_of_grids)]
    drawGrid(array,no_of_grids)

button = Button(root,text="Start The Walk",command=createGrid).pack(padx=8,pady=2)

root.mainloop()