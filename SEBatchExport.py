import win32com.client as wc
from tkinter import *
from tkinter import filedialog as fd
import pathlib
import os

dlg = Tk()
dlg.title('Solid Edge Batch Processor')
dlg.geometry('600x280')
dlg.eval('tk::PlaceWindow . Center')

se = wc.GetActiveObject("SolidEdge.Application")

def listAllPartFiles():
    sFolderPath = fd.askdirectory()
    bPath = pathlib.Path(sFolderPath)
    sItems = bPath.iterdir()
    # lstFiles.delete(0, END)
    for sItem in sItems:
        if sItem.is_file():
            sFilename = str(sItem)
            if sFilename.endswith(".par"):
                lstFiles.insert(END, sItem)


btnFolder = Button(dlg, text = 'Select Folder', command=listAllPartFiles).place(x=30,y=30)

lstFiles = Listbox(dlg, width=60, height =7)
lstFiles.place(x=30, y=60)

def startBatchProcess():
    seDocs = se.Documents

    for i in range(lstFiles.size()):
        sFilename = str(lstFiles.get(i))
        sStatus.set('Exporting...' + sFilename)
        seDoc = seDocs.Open(sFilename)
        sNewFilename = sFilename + ".sat"
        seDoc.SaveAs(sNewFilename)
        seDoc.Close()

    sStatus.set('Finished exporting...' + str(lstFiles.size()) + " files")

btnStart = Button(dlg, text = 'Start', command = startBatchProcess).place(x=30,y=200)

sStatus = StringVar()
lblStatus = Label(dlg, textvariable=sStatus).place(x=30, y=240)

dlg.mainloop()