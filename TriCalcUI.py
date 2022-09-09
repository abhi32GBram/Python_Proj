import math
from tkinter import *

dlg = Tk()
dlg.title('Triangle')
dlg.geometry('300x300')
dlg.eval('tk::PlaceWindow . center')

sideA = StringVar()
sideA.set('12.5')

sideB = StringVar()
sideB.set('5.46')

sArea = StringVar()
sHypo = StringVar()
sPeri = StringVar()

lblSideA = Label(dlg, text='Side A:').place(x=30, y=30)
lblSideB = Label(dlg, text='Side B:').place(x=30, y=60)

txtSideA = Entry(dlg, width=5, textvariable=sideA, bg='yellow', fg='blue').place(x=80, y=30)
txtSideB = Entry(dlg, width=5, textvariable=sideB, bg='pink', fg='brown').place(x=80, y=60)


def calcArea():
    A = float(sideA.get()) # '12.5'
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar, 2)

    sArea.set('Area is ' + str(Ar))

    Hy = math.sqrt(A * A + B * B)
    Hy = round(Hy, 2)
    sHypo.set('Hypotenuse is ' + str(Hy))

    Pe = A + B + Hy
    Pe = round(Pe, 2)
    sPeri.set('Perimeter is ' + str(Pe))

    file = open("C:\\temp\\TriData.csv", 'a')
    sData = sideA.get() + ", " + sideB.get() + ", " + str(Hy) + "\n"
    file.write(sData)
    file.close()

btnCalculate = Button(dlg, text='Calculate', command=calcArea).place(x=30, y=90)

lblAnswer = Label(dlg, text='Area', textvariable=sArea).place(x=30, y=150)
lblHypo = Label(dlg, text='Hypo', textvariable=sHypo).place(x=30, y=180)
lblPeri = Label(dlg, text='Peri', textvariable=sPeri).place(x=30, y=210)

dlg.mainloop()
