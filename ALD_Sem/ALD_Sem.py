import tkinter
from PIL import ImageTk, Image
from pathlib import Path
import random
import numpy as np

#initialization, w is the width of the canvas, h is the height
#number of rows (x) and columns (y)
#imglist exists as a means to stop the garbage collector from deleting images
x=10; y=10
w=45*x; h=45*y
root = tkinter.Tk()
canvas = tkinter.Canvas(width=w, height=h)
arr = [[0 for i in range(x)] for _ in range(y)]
imglist = []

#printing method for array testing
class Print:
    def ArrPrint(arr, x, y):
        for i in range(y):
            for j in range(x):
                print(arr[i][j], end = " ")
            print()

#class for all random number methods
class Rng:
    #Chooses one of 4 values. Each value can be assigned a chance, this allows us to make some tiles rarer.
    def Choose4(n1, c1, n2, c2, n3, c3, n4, c4):
        k=random.randint(1,100)
        if k<=c1:
            return n1
        elif k<=(c1+c2):
            return n2
        elif k<=(c1+c2+c3):
            return n3
        else:
            return n4

    #method that fills array with values
    #the numbers correspond to the names of the images
    def Fill(arr,x,y):
        #The top left corner can have any value. There are 16 images, therefore a random integer between 1 and 16 is chosen
        arr[0][0]=random.randint(1,16)
        #This fills the rest of the top row.
        for i in range(x-1):
            if ((arr[0][i] >= 5) and (arr[0][i] <= 12)):
                arr[0][i+1]=random.choice([2, 3, 5, 7, 9, 11, 14, 15])
            else:
                arr[0][i+1]=random.choice([1, 4, 6, 8, 10, 12, 13, 16])
        #Similar thing as the above for the rest of the first column.
        for i in range(y-1):
            if ((arr[i][0] >= 1) and (arr[i][0]) <= 8):
                arr[i+1][0]=random.choice([3, 4, 5, 8, 11, 12, 13, 14])
            else:
                arr[i+1][0]=random.choice([1, 2, 6, 7, 9, 10, 15, 16])
        #This fills the rest of the array. We have to check the array values both to the left and above.
        for i in range(y-1):
            for j in range(x-1):
                if ((arr[i][j+1] >= 1) and (arr[i][j+1] <= 8)):
                    if ((arr[i+1][j] >= 5) and (arr[i+1][j]) <= 12):
                        arr[i+1][j+1]=Rng.Choose4(3, 30, 5, 15, 11, 30, 14, 25)
                    else:
                        arr[i+1][j+1]=Rng.Choose4(4, 30, 8, 25, 12, 30, 13, 15)
                else:
                    if ((arr[i+1][j] >= 5) and (arr[i+1][j]) <= 12):
                        arr[i+1][j+1]=Rng.Choose4(2, 30, 7, 25, 9, 30, 15, 15)
                    else:
                        arr[i+1][j+1]=Rng.Choose4(1, 30, 6, 25, 10, 30, 16, 15)
#class for drawing
class Draw():
    #Method for drawing an image using the array values
    def DrawImage(self, arr, x, y):
        for i in range(y):
            for j in range(x):
                k=arr[i][j]
                xcoord=(j)*w/x
                ycoord=(i)*h/y
                strin = "images\\" + str(k) + ".png"
                self.im=Image.open(Path(strin))
                ph=ImageTk.PhotoImage(self.im)
                root.ph = ph
                imglist.append(ph)
                canvas.create_image(xcoord, ycoord, image=ph, anchor='nw')
        
#calling the various methods
dr=Draw()
Rng.Fill(arr, x, y)
Print.ArrPrint(arr,x,y)
dr.DrawImage(arr, x, y)



canvas.pack()
root.mainloop()
