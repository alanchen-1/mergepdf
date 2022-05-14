import sys
from PyPDF2 import PdfFileMerger

def mergePDF(filename, files):
    merge = PdfFileMerger()
    for file in files:
        merge.append(file)

    merge.write(filename)

mergePDF(sys.argv[1], sys.argv[2: ])
