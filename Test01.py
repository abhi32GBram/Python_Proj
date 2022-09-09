from errno import EXDEV
import math
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import dialog
from turtle import bgcolor, title

dlgBox = Tk()
dlgBox.title("TRIANGLE PARAMETER CALCULATOR")
dlgBox.configure(bg='#e3ae76')
dlgBox.geometry('400x400')

Side1 = StringVar()
Side1.set('100')

Side2 = StringVar()
Side2.set('200')

ePerimeter = StringVar()
eArea = StringVar()
eEccentri = StringVar()

chPeri = IntVar()
chArea = IntVar()
chEccen = IntVar()

label_Side1 = Label(dlgBox, text='MAJOR AXIS  :').place(x=30, y=30)
label_Side2 = Label(dlgBox, text='MINOR AXIS  :').place(x=30, y=60)

text_SideA = Entry(dlgBox, width=5, textvariable=Side1, bg='#e3496d').place(x=120, y=30)
text_SideB = Entry(dlgBox, width=5, textvariable=Side2, bg='#787cf0').place(x=120, y=60)

chkPeri = Checkbutton(dlgBox, text="Perimeter", variable='chPeri').place(x=30, y=90)
chkArea = Checkbutton(dlgBox, text="Area", variable='chArea').place(x=100, y=90)
chkEccen = Checkbutton(dlgBox, text="Eccentricity", variable='chEccen').place(x=150, y=90)


def calculations():
    S1 = float(Side1.get())
    S2 = float(Side2.get())

    Peri = math.pi * (S1 + S2)
    Peri = round(Peri, 2)
    ePerimeter.set("PERIMETER IS :  " + str(Peri))

    Area = float(math.pi * S1 * S2)
    Area = round(Area, 2)
    eArea.set("AREA IS : " + str(Area))

    Eccen = float(math.sqrt(1 - (S1 * 2 / S2 * 2)))
    Eccen = round(Eccen, 2)
    eEccentri.set("ECCENTRICITY IS : " + str(Eccen))

    if chPeri.get() == 1:
        ePerimeter.set("PERIMETER IS :  " + str(Peri))
    else:
        ePerimeter.set('')

    if chArea.get() == 1:
        eArea.set("AREA IS : " + str(Area))
    else:
        eArea.set('')

    if chEccen.get() == 1:
        eEccentri.set("ECCENTRICITY IS : " + str(Eccen))
    else:
        eEccentri.set('')


button_Calc = Button(dlgBox, text='CALCULATE', command=calculations, bg='#22c94c').place(x=30, y=120)

label_Result = Label(dlgBox, text='PERIMETER IS :', textvariable=ePerimeter, bg='#94add6').place(x=30, y=180)
label_Area = Label(dlgBox, text='AREA IS  :', textvariable=eArea, bg='#d694c6').place(x=30, y=210)
label_Eccen = Label(dlgBox, text='AREA IS  :', textvariable=eEccentri, bg='#94d6d0').place(x=30, y=240)

dlgBox.mainloop()