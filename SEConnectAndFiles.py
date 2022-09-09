import win32com.client as wc
from tkinter import *
from tkinter import filedialog as fd

dlg = Tk()
dlg.title('Solid Edge')
dlg.geometry('600x600')
dlg.eval('tk::PlaceWindow . Center')

sName = StringVar()

sStatusBarText = StringVar()
sStatusBarText.set("Hello from Python")

sCaptionText = StringVar()
sCaptionText.set("Hello from Python")
sDocType = StringVar()

se = wc.GetActiveObject("SolidEdge.Application")
seDoc = se.ActiveDocument

# Change Status Bar Text
lblFilename = Label(dlg, textvariable=sName).place(x=30, y=90)

lblStatusBar = Label(dlg, text='Status Bar Text:').place(x=30, y=30)
txtStatus = Entry(dlg, textvariable=sStatusBarText).place(x=120, y=30)

def setSetStatusBarText():
    se.StatusBar = sStatusBarText.get()

btnSetStatusBarText = Button(dlg, text='Set StatusBar Text', command=setSetStatusBarText).place(x=260, y=30)

# Change Caption
lblCaption = Label(dlg, text='Caption:').place(x=30, y=120)
txtCaption = Entry(dlg, textvariable=sCaptionText).place(x=120, y=120)

def setCaption():
    se.Caption = sCaptionText.get()

btnsetCaption = Button(dlg, text='Set Caption', command=setCaption).place(x=260, y=120)

# Active Document Name
def getActiveDocumentName():
    sFilename = seDoc.FullName
    sName.set(sFilename)

btnFilename = Button(dlg, text='Active Document Name', command=getActiveDocumentName).place(x=30, y=60)

def getDocType():
    sDocType.set(se.ActiveDocumentType)

btnDocType = Button(dlg, text='Active Document Type', command=getDocType).place(x=180, y=60)

lblDocType = Label(dlg, textvariable=sDocType).place(x=350, y=60)

# Count Documents
sDocumentCount = StringVar()
lblDocuments = Label(dlg, text='Doc Count', textvariable=sDocumentCount).place(x=30, y=180)

lstDocuments = Listbox(dlg, width=80, height=5)
lstDocuments.place(x=30, y=210)

def countDocuments():
    n = se.Documents.Count
    sDocumentCount.set('Number of open documents = ' + str(n))
    seDocs = se.Documents
    lstDocuments.delete(0, END)
    for seDoc in seDocs:
        lstDocuments.insert(END, seDoc.FullName)

btnDocCount = Button(dlg, text='Count and List Open Documents', command=countDocuments).place(x=30, y=150)

# Active environment
sEnviron = StringVar()

def getActiveEnviron():
    sEnv = se.ActiveEnvironment
    sEnviron.set(sEnv)

btnEnv = Button(dlg, text='Active Environ', command=getActiveEnviron).place(x=30, y=300)
lblEnv = Label(dlg, text='', textvariable=sEnviron).place(x=120, y=300)

# Create new documents

def createDoc():
    seDoc = se.Documents.Add("SolidEdge.DraftDocument")
    sFilename = fd.asksaveasfilename(initialdir='D:\\Classes\\Suraj\\', filetypes = (('Solid Edge Part Files', '*.par'), ('Text Files', '*.txt'), ('Excel Files', '*.xls') ))
    sFilename = str(sFilename)
    sFilename = sFilename.replace('/', '\\')
    print(sFilename)
    seDoc.SaveAs(sFilename + '.dft')

btnCreateNew = Button(dlg, text='Create New Document', command=createDoc).place(x=30, y=330)

# Open a document

def openDoc():
    sFilename = fd.askopenfilename(initialdir='D:\\Classes\\Suraj\\', filetypes=(
    ('Solid Edge Part Files', '*.par'), ('Draft Documents', '*.dft'), ('Assembly Files', '*.asm')))
    sFilename = str(sFilename)
    sFilename = sFilename.replace('/', '\\')
    print(sFilename)
    seDoc = se.Documents.Open(sFilename)


btnOpenDoc = Button(dlg, text='Open a Document', command=openDoc).place(x=180, y=330)

# Close a document

def closeActiveDoc():
    seDoc = se.ActiveDocument
    seDoc.Close(False) # False means don't save changes, close forecefully without saving and changes.

btnCloseActiveDoc = Button(dlg, text='Close Active Document', command=closeActiveDoc).place(x=120, y=300)

# Close all documents

def closeAllDocs():
    seDocs = se.Documents
    seDocs.Close()

btnCloseAallDocs = Button(dlg, text='Close All Documents', command=closeAllDocs).place(x=270, y=300)

# Activate document

def activateDoc():
    curSels = lstDocuments.curselection()
    iCurSel = curSels[0]
    sFilename = str(lstDocuments.get(iCurSel))
    seDocs=se.Documents
    seDoc = seDocs.Item(sFilename)
    seDoc.Activate()

btnActivateDoc = Button(dlg, text='Activate Document', command=activateDoc).place(x=400, y=300)

# Close Selected document

def closeSelectedDoc():
    curSels = lstDocuments.curselection()
    iCurSel = curSels[0]
    sFilename = str(lstDocuments.get(iCurSel))
    seDocs = se.Documents
    seDoc = seDocs.Item(sFilename)
    seDoc.Close()
    lstDocuments.delete(ANCHOR)
    countDocuments()

btnCloseSelDoc = Button(dlg, text='Close Sel Document', command=closeSelectedDoc).place(x=300, y=330)

# Export Selected document

def exportSelectedDoc():
    curSels = lstDocuments.curselection()
    iCurSel = curSels[0]
    sFilename = str(lstDocuments.get(iCurSel))
    seDocs = se.Documents
    seDoc = seDocs.Item(sFilename)
    seDoc.SaveAs(sFilename + '.sat')


btnexportSelectedDoc = Button(dlg, text='Export Sel Document', command=exportSelectedDoc).place(x=430, y=330)


dlg.mainloop()
