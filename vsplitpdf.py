#!/usr/bin/env python
import shutil
import sys
from pyPdf import PdfFileWriter, PdfFileReader
from pyPdf.generic import FloatObject


for filename in sys.argv[1:]:
    output_pdf = PdfFileWriter()
    input1 = PdfFileReader(open(filename, "rb"))
    filename_copy = '%s.2' % filename
    shutil.copy(filename, filename_copy)
    input2 = PdfFileReader(open(filename_copy, "rb"))
    page_count = input1.getNumPages()

    for page_index in range(page_count):
        page_left = input1.getPage(page_index)
        page_right = input2.getPage(page_index)  # fastering than copying via python
        height, width = page_left.mediaBox.upperRight
        # print height, width

        # print page_left.mediaBox.upperRight
        # print width
        # Rect = (lowerleft_x, lowerleft_y, upperright_x, upperright_y)
        page_left.mediaBox[1] = FloatObject(width / 2)
        # print 'left', page_left.mediaBox
        # print , width / 2
        output_pdf.addPage(page_left)

        page_right.mediaBox[3] = FloatObject(width / 2)
        # print 'right', page_right.mediaBox
        output_pdf.addPage(page_right)

    outputStream = open(filename.replace('.pdf', '-split.pdf'), "wb")
    output_pdf.write(outputStream)
    outputStream.close()
