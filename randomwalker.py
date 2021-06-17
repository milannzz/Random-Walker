from array import ArrayType
from tkinter import *
from tkinter import Canvas
import random

# Clearer Ui using ctypes
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.geometry("601x660")
root.title("Random Walker")
root.resizable(1,1)

c = Canvas(root, height=601, width=601, bg='WHITE',borderwidth=0, highlightthickness=0)
c.grid(row=0,column=0)

def drawGrid(array,no_of_grids,ci,cj):
    size = 600/no_of_grids
    width = 1
    gap = 0
    for i in range(0,int(600/size)):
        for j in range(0,int(600/size)):
            if i == ci and j == cj:
                fill = 'tan3'
                dfill = 'tan4'
                c.create_rectangle(i*size+gap,j*size+gap,i*size+size,j*size+size,width=width+1,outline="lightblue",fill=fill)
            elif array[i][j] == 1:
                fill = 'tan3'
                dfill = 'tan4'
                c.create_rectangle(i*size+gap,j*size+gap,i*size+size,j*size+size,width=width,outline="black",fill=fill)
            else:
                fill = 'bisque'
                dfill= 'bisque3'
                c.create_rectangle(i*size+gap,j*size+gap,(i*size+size),(j*size+size),width=width,outline="black",fill=fill) 

def startWalk(array,i,j,no_of_grids):
    choice = random.choice(["left","right","up","down"])
    drawGrid(array,no_of_grids,i,j)
    root.update()
    if choice == "left":
        if j-1>0:
            array[i][j-1] = 1
            j=j-1
        else:
            array[i][j+1] =1
            j=j+1
    elif choice == "right":
        if j+1 < no_of_grids:
            array[i][j+1] = 1
            j=j+1
        else:
            array[i][j-1] = 1
            j=j-1
    elif choice == "up":
        if(i+1<no_of_grids):
            array[i+1][j] = 1
            i=i+1
        else :
            array[i-1][j] = 1
            i=i-1
        
    else:
        if(i-1>0):
            array[i-1][j] = 1
            i=i-1
        else:
            array[i+1][j] = 1
            i=i+1

    startWalk(array,i,j,no_of_grids)

def createGrid():
    global no_of_grids
    no_of_grids = no_of_grids.get()
    array = [[0 for x in range(no_of_grids)] for x in range(no_of_grids)]
    i = int(no_of_grids/2)
    j = int(no_of_grids/2)
    array[i][j]=1
    startWalk(array,i,j,no_of_grids)

def stop():
    root.destroy()

frame = Frame(root)
frame.grid(row=1,column=0,padx=8,pady=2)
root.grid_columnconfigure(1,weight=1)

buttonStart = Button(frame,text="Start The Walk",command=createGrid,width=15)
buttonStart.grid(row=0,column=0,padx=8,pady=2)

global no_of_grids
no_of_grids = IntVar()
scale = Scale(frame,variable=no_of_grids,from_=2, to=100,orient=HORIZONTAL,width=15)
scale.set(20)
scale.grid(row=0,column=2)

buttonStop = Button(frame,text="Exit",command=stop,fg="white",bg="red",width=15)
buttonStop.grid(row=0,column=3,padx=8,pady=2)

root.mainloop()