#!/usr/bin/env python
import shutil
import sys
from pyPdf import PdfFileWriter, PdfFileReader
from pyPdf.generic import FloatObject
import tempfile


for original in sys.argv[1:]:
    output_pdf = PdfFileWriter()

    input1 = PdfFileReader(open(original, 'rb'))

    _, original_copy = tempfile.mkstemp(suffix='.pdf')
    shutil.copy(original, original_copy)

    input2 = PdfFileReader(open(original_copy, 'rb'))

    page_count = input1.getNumPages()

    for page_index in range(page_count):
        page_left = input1.getPage(page_index)
        page_right = input2.getPage(page_index)  # fastering than copying via python

        width, height = page_left.mediaBox.upperRight

        # Rect = (lowerleft_x, lowerleft_y, upperright_x, upperright_y)
        # move the left box's right edge to the middle
        page_left.mediaBox[2] = FloatObject(width / 2)
        output_pdf.addPage(page_left)

        # and the right box's left edge to the same place
        page_right.mediaBox[0] = FloatObject(width / 2)
        output_pdf.addPage(page_right)

    outputStream = open(original.replace('.pdf', '-split.pdf'), 'wb')
    output_pdf.write(outputStream)
    outputStream.close()
