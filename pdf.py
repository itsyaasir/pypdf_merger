import PyPDF2 as pdf2
import os
import sys

inputs = sys.argv[1:]
merger = pdf2.PdfFileMerger()


def pdf_combiner(pdf_list):
    for pdfs in pdf_list:
        print(pdfs)
        merger.append(pdfs)
    merger.write("output.pdf")


pdf_combiner(inputs)
