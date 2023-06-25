import PyPDF2
#abrir el archivo PDF

with open('clcoding.pdf', 'rb') as pdf_file:
    pdf_reader=PyPDF.PdfFileReader(pdf_file)
    