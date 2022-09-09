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

lblSideA = Label(dlg, text='Side A:').place(x=30, y=30)
lblSideB = Label(dlg, text='Side B:').place(x=30, y=60)

#txtSideA = Entry(dlg, width=5, textvariable=sideA, bg='yellow', fg='blue').place(x=80, y=30)
spinSideA = Spinbox(dlg, from_ = 0, to = 50, width=5, font="Arial 10", textvariable=sideA).place(x=80, y=30)

#txtSideB = Entry(dlg, width=5, textvariable=sideB, bg='pink', fg='brown', font="Arial 10").place(x=80, y=60)
sclSideB = Scale(dlg, variable=sideB, orient =HORIZONTAL, from_ = 0, to = 50, bg='pink', fg='brown', font="Arial 8").place(x=80, y=60)

imgFile = Image.open("d:\\Classes\\Suraj\\Triangle.png")
dispImage = ImageTk.PhotoImage(imgFile)
lblImage = Label(dlg, image=dispImage).place(x=250, y=30)

lstParameters = Listbox(dlg, width=20, height= 5)
lstParameters.place(x=30, y=110)

#lstParameters.insert(1, 'Area')
#lstParameters.insert(2, 'Hypotenuse')
#lstParameters.insert(3, 'Perimeter')

params = ['Area', 'Hypotenuse', 'Perimeter']

for param in params:
    lstParameters.insert(END, param)

def calcArea():
    A = float(sideA.get())
    B = float(sideB.get())

    Ar = A * B * 0.5
    Ar = round(Ar, 2)

    Hy = math.sqrt(A * A + B * B)
    Hy = round(Hy, 2)

    Pe = A + B + Hy
    Pe = round(Pe, 2)

    selItems = lstParameters.curselection()
    #print(selItems)

    i = selItems[0]
    print(i)
    if i==0:
        sAnswer.set('Area is ' + str(Ar))

    if i==1:
        sAnswer.set('Hypotenuse is ' + str(Hy))

    if i==2:
        sAnswer.set('Perimeter is ' + str(Pe))

btnCalculate = Button(dlg, text='Calculate', command=calcArea).place(x=30, y=200)

lblAnswer = Label(dlg, text='Area', textvariable=sAnswer).place(x=30, y=250)

dlg.mainloop()
