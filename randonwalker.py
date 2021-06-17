from array import ArrayType
from tkinter import *
from tkinter import Canvas
import random

root = Tk()
root.geometry("600x600")
root.title("Random Walker")
root.resizable(1,1)


c = Canvas(root, height=1000, width=1000, bg='WHITE')
c.pack(fill=BOTH, expand=True)


def drawGrid(array,no_of_grids):
    size = 600/no_of_grids
    width = 1
    for i in range(0,int(600/size)):
        for j in range(0,int(600/size)):
            if array[i][j] == 0:
                fill = 'tan3'
                dfill = 'tan4'
                c.create_rectangle(i*size,j*size,i*size+size,j*size+size,width=width,outline="black",fill=fill)
            else:
                fill = 'bisque'
                dfill= 'bisque3'
                c.create_rectangle(i*size,j*size,(i*size+size),(j*size+size),width=width,outline="black",fill=fill,disabledfill=dfill)

no_of_grids = 20
array = [[random.randint(0,1) for x in range(no_of_grids)] for x in range(no_of_grids)]
drawGrid(array,no_of_grids)

root.mainloop()