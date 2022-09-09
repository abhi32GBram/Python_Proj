import os

def getFilenameComponents(fullfilename):
    # print(fullfilename)
    folder, filenameWithExtn = os.path.split(fullfilename)
    # print(folder)
    # print(filename)

    filename, extn = os.path.splitext(fullfilename)
    # print(extn)

    filenameWOpath = os.path.basename(fullfilename)
    # print(filenameWOpath)
    filenameWoExtWoPathList = os.path.splitext(filenameWOpath)
    # print(filenameWoExtWoPathList)
    filenameWoExtWoPath = filenameWoExtWoPathList[0]
    # print(filenameWoExtWoPath)

    return folder, filenameWithExtn, extn, filenameWoExtWoPath


ff = "D:\\Classes\\Suraj\\wheel.par"
print(ff)
comps = ff.split('\\')
print(comps)
print('Drive is ', comps[0])
print('Filename is ', comps[-1])

ffn = ff.replace('\\', '/')
print(ffn)
comps = ffn.split('/')
print(comps)
print('Drive is ', comps[0])
print('Filename is ', comps[-1])

#comps = getFilenameComponents(ff)

