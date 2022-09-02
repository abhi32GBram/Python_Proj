import math
from tkinter import *

dlg = Tk()
dlg.title('Triangle')
dlg.geometry('300x300')
dlg.eval('tk::PlaceWindow . Center')

sideA = StringVar()
sideA.set('12.5')

sideB = StringVar()
sideB.set('5.46')

sArea = StringVar()
sHypo = StringVar()
sPeri = StringVar()

iArea = IntVar()
iArea.set(1)

iHypo = IntVar()

iPeri = IntVar()
iPeri.set(1)

lblSideA = Label(dlg, text='Side A:').place(x=30, y=30)
lblSideB = Label(dlg, text='Side B:').place(x=30, y=60)

txtSideA = Entry(dlg, width=5, textvariable=sideA, bg='yellow', fg='blue').place(x=80, y=30)
txtSideB = Entry(dlg, width=5, textvariable=sideB, bg='pink', fg='brown').place(x=80, y=60)

chkArea = Checkbutton(dlg, text='Area', variable=iArea).place(x=30, y=90)
chkHypo = Checkbutton(dlg, text='Hypotenuse', variable=iHypo).place(x=100, y=90)
chkPeri = Checkbutton(dlg, text='Perimeter', variable=iPeri).place(x=200, y=90)


def calcArea():
    A = float(sideA.get())  # '12.5'
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar, 2)

    Hy = math.sqrt(A * A + B * B)
    Hy = round(Hy, 2)

    Pe = A + B + Hy
    Pe = round(Pe, 2)

    if iArea.get() == 1:
        sArea.set('Area is ' + str(Ar))
    else:
        sArea.set('')

    if iHypo.get() == 1:
        sHypo.set('Hypotenuse is ' + str(Hy))
    else:
        sHypo.set('')

    if iPeri.get() == 1:
        sPeri.set('Perimeter is ' + str(Pe))
    else:
        sPeri.set('')


btnCalculate = Button(dlg, text='Calculate', command=calcArea).place(x=30, y=120)

lblAnswer = Label(dlg, text='Area', textvariable=sArea).place(x=30, y=180)
lblHypo = Label(dlg, text='Hypo', textvariable=sHypo).place(x=30, y=210)
lblPeri = Label(dlg, text='Peri', textvariable=sPeri).place(x=30, y=240)

btnLambda = Button(dlg, text='Cube', command=lambda N=4: print(N * N * N)).place(x=30, y=270)

dlg.mainloop()
