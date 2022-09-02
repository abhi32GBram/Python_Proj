import math
from tkinter import *
from PIL import ImageTk, Image

dlg = Tk()
dlg.title('Triangle')
dlg.geometry('450x300')
dlg.eval('tk::PlaceWindow . center')

sideA = StringVar()
sideA.set('12.5')

sideB = StringVar()
sideB.set('5.46')

sAnswer = StringVar()
sParam = StringVar()

lblSideA = Label(dlg, text='Side A:').place(x=30, y=30)
lblSideB = Label(dlg, text='Side B:').place(x=30, y=60)

spinSideA = Spinbox(dlg, from_ = 0, to = 50, width=5, font="Arial 10", textvariable=sideA).place(x=80, y=30)
sclSideB = Scale(dlg, variable=sideB, orient =HORIZONTAL, from_ = 0, to = 50, bg='pink', fg='brown', font="Arial 8").place(x=80, y=60)

params = ['Area', 'Hypotenuse', 'Perimeter']

oMenu = OptionMenu(dlg, sParam, *params).place(x=30, y=110)

def calcArea():
    A = float(sideA.get())
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar, 2)

    Hy = math.sqrt(A * A + B * B)
    Hy = round(Hy, 2)

    Pe = A + B + Hy
    Pe = round(Pe, 2)

    if sParam.get() == 'Area':
        sAnswer.set('Area is ' + str(Ar))

    if sParam.get() == 'Hypotenuse':
        sAnswer.set('Hypotenuse is ' + str(Hy))

    if sParam.get() == 'Perimeter':
        sAnswer.set('Perimeter is ' + str(Pe))

btnCalculate = Button(dlg, text='Calculate', fg='blue', command=calcArea).place(x=30, y=200)

lblAnswer = Label(dlg, text='Area', textvariable=sAnswer).place(x=30, y=250)

def calArea():
    sAnswer.set('Area = 100')

def calHypo():
    sAnswer.set('Hypo = 50')

def calPeri():
    sAnswer.set('Peri = 150')

def showInfo():
    strInfo = StringVar()
    strInfo.set('CADVertex.com')

    dlgInfo = Toplevel(dlg)
    btnOK = Button(dlgInfo, text='OK').place(x=30,y=60)
    lblInfo = Label(dlgInfo, textvariable=strInfo).place(x=30, y=30)

menubar = Menu()

paramMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Calculate', menu=paramMenu)
paramMenu.add_cascade(label='Area', command = calArea)
paramMenu.add_cascade(label='Hypotenuse', command = calHypo)
paramMenu.add_cascade(label='Perimeter', command = calPeri)

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_cascade(label='Help')
helpMenu.add_cascade(label='About', command=showInfo)
helpMenu.add_cascade(label='Go to CADVertex.com')

dlg.config(menu=menubar)

dlg.mainloop()
