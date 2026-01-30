import binascii
import os
from pathlib import Path

def convertCNGtoJPEG(filepath, page, savepathstring):
    print("entered convert()")
    print("filename is: " + page)
    fullfilename = os.path.join(str(filepath) + '\\' + page)
    print("fullfilename is: " + fullfilename)
    filenamesuffix = Path(fullfilename).suffix
    print('filenamesuffix = ' + filenamesuffix)
    if filenamesuffix == '.cng':
        with open(fullfilename, 'rb') as f:
            content = f.read().hex() #read the file
        #print("content is: \n" + str(content))
        #print( '\ncontent is type ' + str(type(content)))
        numcontents = len(content)
        #print('numcontents = ' + str(numcontents))
        i = 0
        jpegarray = bytearray()
        print('jpegarray = ' + str(jpegarray))
        cnt = len(content)
        while i < cnt:
            j = i + 1
            num = content[i] + content[j]
            num = int(num, 16)
            num = num ^ 239
            jpegarray.append(num)
            i = j + 1
    
        filename = 'temp.jpg'
        savefilename = os.path.join(str(savepathstring) + '\\' + filename)
        print('savefilename = ' + savefilename)
        binaryfile = open(savefilename, 'wb')
        binaryfile.write(bytes(jpegarray))
        binaryfile.close()
    return()

