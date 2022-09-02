
from tkinter import *
import math

#INITIALIZE TK INTER
dlgBox = Tk()
#TITLE CARD
dlgBox.title('Triangle Calculator')
# DIMENSIONS OF DIALOGUE BOX
dlgBox.geometry('400x400')
#POSITION OF THE BOX
dlgBox.eval('tk::PlaceWindow . center ')

#TO DENY MAXINMIZING OR RESIZING
#dlgBox.resizable(False,False)

# CHANGING BG OF BOX
#dlgBox.configure(bg='#ANY COLOUR ')

#STRING VAR OF INPUT RELATION
sideA = StringVar()
sideB = StringVar()

 # TAKE VALUES OF INPUT TO SAVE FOR NEXT TIME
def read_val():
    file= open("D:\\VS_CODE\\SYNTX\\PYTHON\\triangle_val.txt",'r')
    lines =file.read().splitlines()

    sideA_val = lines[0]
    sideB_val = lines[1]

    sideA.set(sideA_val)
    sideB.set(sideB_val)

    file.close()


read_val()

sAnswer = StringVar()
iAnswer = IntVar()

# TEXT LABELS FOR USER INPUT
labelSideA= Label(dlgBox, text='SIDE A : ').place(x=30,y=30)
labelSideB= Label(dlgBox, text='SIDE B : ').place(x=30,y=60)

# ENTRY BOX FOR USER TO TYPE VALUES
txtSideA = Entry(dlgBox,width=5, textvariable= sideA,bg ='#e3496d').place(x=120,y=30)
txtSideB = Entry(dlgBox,width=5, textvariable= sideB,bg ='#e3496d').place(x=120,y=60)

# RADIO BUTTON FOR EACH PARAMETER TO BE CALCULATED
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

    save()


btnCalculate = Button(dlgBox, text='CALCULATE',command=calcArea).place(x=30,y=150)
labelAnswer = Label(dlgBox, text= 'AREA',textvariable=sAnswer).place(x=30,y=180)

def save():
    file = open("D:\\VS_CODE\\SYNTX\\PYTHON\\saved_values.txt",'w')

    file.write(str(sideA.get()))
    file.write('\n')
    file.write(str(sideB.get()))
    file.close()


btnCalculate = Button(dlgBox, text='CALCULATE',command=calcArea).place(x=30,y=150)

labelAnswer = Label(dlgBox, text= 'AREA',textvariable=sAnswer).place(x=30,y=180)

dlgBox.mainloop()
