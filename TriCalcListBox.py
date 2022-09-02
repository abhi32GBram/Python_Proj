import math
from select import select
from tkinter import *

dlgBox = Tk()
dlgBox.title('Triangle Calculator')
dlgBox.geometry('300x300')

sideA = StringVar()
sideA.set("200")

sideB = StringVar()
sideB.set("400")

sAnswer = StringVar()



labelSideA= Label(dlgBox, text='SIDE A : ').place(x=30,y=30)
labelSideB= Label(dlgBox, text='SIDE B : ').place(x=30,y=60)

txtSideA = Entry(dlgBox,width=5, textvariable= sideA,bg ='#e3496d').place(x=120,y=30)
txtSideB = Entry(dlgBox,width=5, textvariable= sideB,bg ='#e3496d').place(x=120,y=60)

lstParameters = Listbox(dlgBox,width=10,height=5)
lstParameters.place(x=30,y=90)


lstParameters.insert(1,'Area')
lstParameters.insert(2,'Hypo')
lstParameters.insert(3,'Peri')


def calcArea():
    A = float(sideA.get())
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar,2)

    Hy = math.sqrt(A**2+B**2)
    Hy = round(Hy,2)

    Pe = A + B + Hy
    Pe = round(Pe,2)

    selectItems =  lstParameters.curselection()
    i = selectItems[0]
    if i == 0 :
        sAnswer.set('Area is : ' + str(Ar))
    if i == 1 :
        sAnswer.set('Hypotenuse is : ' + str(Hy))
    if i == 2 :
        sAnswer.set('Perimeter is : ' + str(Pe))


btnCalculate = Button(dlgBox, text='CALCULATE',command=calcArea).place(x=30,y=200)

labelAnswer = Label(dlgBox, text= 'AREA',textvariable=sAnswer).place(x=30,y=230)

dlgBox.mainloop()