from importlib.resources import as_file
import math
import site
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import pathlib
import os
from tkinter import messagebox


dlgBox = Tk()
dlgBox.title('TRIANGLE CALCULATOR')
dlgBox.geometry('700x500')
dlgBox.wm_iconbitmap(bitmap='D:\\DOWNLOADS\\eeer.ico')
dlgBox.eval('tk::PlaceWindow . center')

sInfo = StringVar()
sInfo.set('FILE INFO : ')


def allListFiles():
    sFolderPath = fd.askdirectory()
    bPath = pathlib.Path(sFolderPath)
    sElement = bPath.iterdir()

    for sElement in sElement:
        if sElement.is_file():
            lstFolders.insert(END, sElement)

        if sElement.is_dir():
            lstFiles.insert(END, sElement)


lableInfo = Label(dlgBox, text='INFO', textvariable=sInfo).place(x=30, y=30)


def selct_Item(self):
    selct_Item = lstFiles.curselection()
    i = selct_Item[0]
    slctFile = lstFiles.get(i)
    sInfo.set(slctFile)


lstFiles = Listbox(dlgBox, width=80, height=10,selectmode=EXTENDED)
lstFiles.place(x=30, y=90)

lstFiles.bind('<<ListboxSelect>>', selct_Item)

lstFolders = Listbox(dlgBox, width=80, height=10)
lstFolders.place(x=30, y=280)

btnFolder = Button(dlgBox, text="PICK FOLDER", command=allListFiles).place(x=30, y=60)


def slctFile():
    file = fd.askopenfilename(filetypes=(('ACROBAT FILES', '*.pdf'), ('TEXT FILES', '*.txt'), ('EXCEL FILES', '*.xls')))
    sInfo.set(str(file))
    os.startfile(file)
    # FOR GIVING OPTIONS FOR EXCLUSIVE FILE EXTENSIONS
    filetypes = (('ACROBAT FILES', '*.pdf'), ('TEXT FILES', '*.txt'), ('EXCEL FILES', '*.xls'))


def slctFiles():
    files = fd.askopenfilenames(filetypes=(('ACROBAT FILES', '*.pdf'), ('TEXT FILES', '*.txt'), ('EXCEL FILES', '*.xls')))
    for file in files:
        lstFiles.insert(END, file)


btnFile = Button(dlgBox, text="PICK FILE", command=slctFile).place(x=115, y=60)

btnFiles = Button(dlgBox, text="PICK FILES ", command=slctFiles).place(x=180, y=60)


def openFile():
    sFileName = sInfo.get()
    iMsg = messagebox.askyesno('Confirm',"ARE YOU SURE YOU WANT TO OPEN ")

    if iMsg == 1:
        os.startfile(sFileName)

btnOPenFile = Button(dlgBox, text="OPEN ", command=openFile).place(x=255, y=60)

dlgBox.mainloop()