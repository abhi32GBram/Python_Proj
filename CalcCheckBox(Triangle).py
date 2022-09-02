import math
from tkinter import *

dlgBox = Tk()
dlgBox.title('Triangle Calculator')
dlgBox.geometry('400x400')

sideA = StringVar()
sideA.set("4000")

sideB = StringVar()
sideB.set("400")

sArea = StringVar()
sHypo = StringVar()
sPeri = StringVar()

iArea = IntVar()
iHypo = IntVar()
iPeri = IntVar()


labelSideA= Label(dlgBox, text='SIDE A : ').place(x=30,y=30)
labelSideB= Label(dlgBox, text='SIDE B : ').place(x=30,y=60)

txtSideA = Entry(dlgBox,width=5, textvariable= sideA,bg ='#e3496d').place(x=120,y=30)
txtSideB = Entry(dlgBox,width=5, textvariable= sideB,bg ='#e3496d').place(x=120,y=60)

chkArea = Checkbutton(dlgBox, text='Area',variable=iArea).place(x=30,y=90)
chkHypo = Checkbutton(dlgBox, text='Hypotenuse',variable=iHypo).place(x=100,y=90)
chkPeri = Checkbutton(dlgBox, text='Perimeter',variable=iPeri).place(x=200,y=90)



def calcArea():
    A = float(sideA.get())
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar,2)

    Hy = math.sqrt(A**2+B**2)
    Hy = round(Hy,2)

    Pe = A + B + Hy
    Pe = round(Pe,2)

    if iArea.get() == 1:
        sArea.set('Area is : ' + str(Ar))
    else:
        sArea.set('')

    if iHypo.get() == 1 :
        sHypo.set('Hypotenuse is : ' + str(Hy))
    else:
        sHypo.set('')

    if iPeri.get() == 1:
        sPeri.set('Perimeter is : ' + str(Pe))
    else:
        sPeri.set('')


btnCalculate = Button(dlgBox, text='CALCULATE',command=calcArea).place(x=30,y=120)

labelAnswer = Label(dlgBox, text= 'AREA',textvariable=sArea).place(x=30,y=150)
labelHypo = Label(dlgBox ,text='HYPOTENUSE',textvariable=sHypo).place(x=30,y=180)
labelPeri = Label(dlgBox ,text='PERIMETER',textvariable=sPeri).place(x=30,y=210)

dlgBox.mainloop()











