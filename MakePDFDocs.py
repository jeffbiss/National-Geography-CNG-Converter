import os
from pathlib import Path
import img2pdf
from PIL import Image
import re
from pypdf import PdfWriter

regex = re.compile('[0-9]+x')
PDFpath = Path('C:\\Users\\jeffe\\Programming\\Python\\NatGeoProject\\PDFs')


def openimage(name,filepath):
    print('entered openimage()')
    imagefilename = os.path.join(str(filepath) + '\\' + name)
    pathstring = str(imagefilename)
    print('pathstring = ' + pathstring + ' and it\'s type ' + str(type(pathstring)))
    im = Image.open(pathstring)
    print('image format: ' + str(im.format) + '\n')
    print('image size: ' + str(im.size) + '\n')
    print('image mode: ' + str(im.mode) + '\n')
    return()

def convertJPEGtoPDF(JPEGsourcepath, PDFfile):
    print('entered convertJPEGtoPDF()')
    print('PDFfile = ' + str(PDFfile))
    JPEGtoconvert = os.path.join(str(JPEGsourcepath) + '\\' + page)
    print('JPEGtoconvert = ' + str(JPEGtoconvert))
    f.write(img2pdf.convert(JPEGtoconvert, rotation=img2pdf.Rotation.ifvalid))
    return()

def appendPDF():
    print('entered appendPDF()')
    pdf_writer = PdfWriter()    #create the PDFWriter object to store the set of issue pages
    pdf_writer.append(tempPDF)
    with open(issuePDF, "wb") as output_file:
        pdf_writer.write(output_file)
    return()

