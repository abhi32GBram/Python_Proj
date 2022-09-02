import math
from tkinter import *

dlg = Tk()
dlg.title('Triangle')
dlg.geometry('300x300')
dlg.eval('tk::PlaceWindow . center')

dlg.resizable(False, False)
#dlg.configure(bg='green')

sideA = StringVar()
#sideA.set('12.5')

sideB = StringVar()
#sideB.set('5.46')

def readValues():
    file=open("c:\\temp\\triValues.txt", 'r')
    lines= file.read().splitlines()
    #print(lines)
    aVal = lines[0]
    #print(aVal)
    bVal = lines[1]
    #print(bVal)
    sideA.set(aVal)
    sideB.set(bVal)
    file.close()

readValues()

sAnswer = StringVar()
iAnswer = IntVar()

lblSideA = Label(dlg, text='Side A:').place(x=30, y=30)
lblSideB = Label(dlg, text='Side B:').place(x=30, y=60)

txtSideA = Entry(dlg, width=5, textvariable=sideA, bg='yellow', fg='blue').place(x=80, y=30)
txtSideB = Entry(dlg, width=5, textvariable=sideB, bg='pink', fg='brown').place(x=80, y=60)

radArea = Radiobutton(dlg, text = 'Area', variable=iAnswer, value=1).place(x=30, y=90)
radHypo = Radiobutton(dlg, text = 'Hypotenuse', variable=iAnswer, value=2).place(x=100, y=90)
radPeri = Radiobutton(dlg, text = 'Perimeter', variable=iAnswer, value=3).place(x=200, y=90)

def calcArea():
    A = float(sideA.get()) # '12.5'
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar, 2)

    Hy = math.sqrt(A * A + B * B)
    Hy = round(Hy, 2)

    Pe = A + B + Hy
    Pe = round(Pe, 2)

    if iAnswer.get() == 1:
        sAnswer.set('Area is ' + str(Ar))

    if iAnswer.get() == 2:
        sAnswer.set('Hypotenuse is ' + str(Hy))

    if iAnswer.get() == 3:
        sAnswer.set('Perimeter is ' + str(Pe))

    saveValues()

btnCalculate = Button(dlg, text='Calculate', command=calcArea).place(x=30, y=120)

lblAnswer = Label(dlg, text='Area', textvariable=sAnswer).place(x=30, y=180)

def saveValues():
    file=open("c:\\temp\\triValues.txt", 'w')
    file.write(str(sideA.get()))
    file.write('\n')
    file.write(str(sideB.get()))
    file.close()

#btnSave = Button(dlg, text='Save Values', command=saveValues).place(x=30, y=210)
#btnLoad = Button(dlg, text='Load Values', command=readValues).place(x=150, y=210)

dlg.mainloop()
