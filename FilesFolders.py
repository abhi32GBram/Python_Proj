from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import pathlib
import os

dlg = Tk()
dlg.title('Triangle')
dlg.geometry('800x500')
dlg.eval('tk::PlaceWindow . center')
#dlg.resizable(False, False)
dlg.iconbitmap("triIcon.ico")

sInfo = StringVar()
sInfo.set('Info')

def listAllFiles():
    sFolderPath = fd.askdirectory()
    bPath = pathlib.Path(sFolderPath)
    sItems = bPath.iterdir()
    #lstFiles.delete(0, END)
    for sItem in sItems:
        if sItem.is_file():
            sFilename = str(sItem)
            if sFilename.endswith(".txt"):
                lstFiles.insert(END, sItem)

        if sItem.is_dir():
            lstFolders.insert(END, sItem)

lblInfo = Label(dlg, text='info', textvariable=sInfo ).place(x=30, y=30)

def selItem(self):
    selItems = lstFiles.curselection()
    i = selItems[0]
    selectedFile = lstFiles.get(i)
    sInfo.set(selectedFile)

lstFiles = Listbox(dlg, width=80, height =10, selectmode=EXTENDED)
lstFiles.place(x=30, y=90)
lstFiles.bind('<<ListboxSelect>>', selItem)

lstFolders = Listbox(dlg, width=80, height =10)
lstFolders.place(x=30, y=280)

btnFolder = Button(dlg, text='Pick Folder', command=listAllFiles).place(x=30, y=60)

def selectFile():
    file = fd.askopenfilename(initialdir='E:/PDF_PPT', filetypes = ( ('Acrobat Files', '*.pdf'), ('Text Files', '*.txt'), ('Excel Files', '*.xls') ))
    sInfo.set(str(file))
    os.startfile(file)

btnFile = Button(dlg, text='Pick File', command=selectFile).place(x=120, y=60)

def selectFiles():
    files = fd.askopenfilenames(initialdir='E:/PDF_PPT', filetypes = ( ('Acrobat Files', '*.pdf'), ('Text Files', '*.txt'), ('Excel Files', '*.xls') ))

    for file in files:
        lstFiles.insert(END, file)

btnFiles = Button(dlg, text='Pick Files', command=selectFiles).place(x=180, y=60)


def openSelectedFile():
    sFilename = sInfo.get()

    iMsg = mb.askyesnocancel('Confirm', "Are you sure to open?")
    if iMsg == 1:
        os.startfile(sFilename)

btnOpenFile = Button(dlg, text='Open Selected File', command=openSelectedFile).place(x=250, y=60)

def openSelectedFiles():
    sSelectedIndices = lstFiles.curselection()
    print(sSelectedIndices)

    for i in sSelectedIndices:
        sFilename = str(lstFiles.get(i))
        os.startfile(sFilename)


btnOpenFiles = Button(dlg, text='Open Selected Files', command=openSelectedFiles).place(x=370, y=60)


def selectFilesFromSubFolders():
    i = 0
    sPath = fd.askdirectory()
    os.chdir(sPath)
    for sPath, allDirs, allFiles in os.walk('.'):
        for filename in allFiles:
            if filename.endswith('.txt'):
                lstFiles.insert(END, filename)
                i = i + 1

    sInfo.set(str(i) + ' files found.')

btnSelectFilesFromSubFolders = Button(dlg, text='Files SubFolders', command=selectFilesFromSubFolders).place(x=500, y=60)

btnRemoveSel = Button(dlg, text='Remove Selected', command=lambda lbox=lstFiles:lbox.delete(ANCHOR)).place(x=610, y=60)

# def clearListBox():
#     lstFiles.delete(0, END)

btnClearList = Button(dlg, text='Clear List', command=lambda lbox=lstFiles:lbox.delete(0, END)).place(x=720, y=60)

# command = lambda N=4: print(N*N*N)

def showMB():
    mb.showinfo('Info', 'Hello from Python')
    mb.showerror('Error', "Some Error occurred" + "\n Do you want to continue" )

btnShowMB = Button(dlg, text='Show Message Box', command=showMB).place(x=30, y=460)

dlg.mainloop()
