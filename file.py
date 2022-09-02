from importlib.resources import as_file
import math
from tkinter import *
from tkinter import filedialog as fd
import pathlib

dlgBox = Tk()
dlgBox.title('TRIANGLE CALCULATOR')
dlgBox.geometry('700x400')
dlgBox.wm_iconbitmap(bitmap='D:\\DOWNLOADS\\eeer.ico')


def allListFiles():
    sFolderPath = fd.askdirectory()
    bPath = pathlib.Path(sFolderPath)
    sFile = bPath.iterdir()

    for sElement in sFile:
        if sElement.is_file():
            lstFiles.insert(END, sElement)


lstFiles = Listbox(dlgBox, width=80, height=10)
lstFiles.place(x=30, y=60)
btnFolder = Button(dlgBox, text="PICK A FOLDER", command=allListFiles).place(x=30, y=30)

dlgBox.mainloop()
