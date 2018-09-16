import os
from PyPDF2 import PdfFileReader

path = "/home/zoelra/Downloads/realpython"

input_file_name = os.path.join(path, "The Whistling Gypsy.pdf")
input_file = PdfFileReader(open(input_file_name, 'rb'))

title = input_file.getDocumentInfo().title
author = input_file.getDocumentInfo().author
total_pages = input_file.getNumPages()

print(title)
print(author)
print(total_pages)
