import math
from tkinter import *

dlgBox = Tk()
dlgBox.title('Triangle Calculator')
dlgBox.geometry('400x400')

sideA = StringVar()
sideA.set("200")

sideB = StringVar()
sideB.set("400")

sAnswer = StringVar()
iAnswer = IntVar()


labelSideA= Label(dlgBox, text='SIDE A : ').place(x=30,y=30)
labelSideB= Label(dlgBox, text='SIDE B : ').place(x=30,y=60)

txtSideA = Entry(dlgBox,width=5, textvariable= sideA,bg ='#e3496d').place(x=120,y=30)
txtSideB = Entry(dlgBox,width=5, textvariable= sideA,bg ='#e3496d').place(x=120,y=60)

radArea = Radiobutton(dlgBox,text='Area',variable=iAnswer ,value=1).place(x=30,y=90)
radHypo = Radiobutton(dlgBox,text='Hypotenuse',variable=iAnswer,value=2).place(x=100,y=90)
radPeri = Radiobutton(dlgBox,text='Perimeter',variable=iAnswer,value=3).place(x=200,y=90)


def calcArea():
    A = float(sideA.get())
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar,2)

    Hy = math.sqrt(A**2+B**2)
    Hy = round(Hy,2)

    Pe = A + B + Hy
    Pe = round(Pe,2)

    if iAnswer.get() == 1:
        sAnswer.set('Area is : ' + str(Ar))
    if iAnswer.get() == 2:
        sAnswer.set('Hypotenuse is : ' + str(Hy))
    if iAnswer.get() == 3:
        sAnswer.set('Perimeter is : ' + str(Pe))



btnCalculate = Button(dlgBox, text='CALCULATE',command=calcArea).place(x=30,y=150)

labelAnswer = Label(dlgBox, text= 'AREA',textvariable=sAnswer).place(x=30,y=180)

dlgBox.mainloop()











