
#folder_path = "C:/Users/santo/Documents/Planificaciones/Cuarto/Cuarto/Electromagnetismo"
#input_folder=r'C:\Users\santo\Documents\Planificaciones\Cuarto\Cuarto\Electromagnetismo'
# Ruta de la carpeta de salida
#output_folder = r'C:\Users\santo\Documents\Planificaciones\Cuarto\Cuarto\Electromagnetismo\pdfs'
# Inicializar Word
from docx2pdf import convert

# Ruta al archivo .docx
docx_file = r'C:\Users\santo\Documents\Planificaciones\Cuarto\Cuarto\Electromagnetismo\Plan de clase 3.docx'

# Ruta de salida para el archivo PDF
pdf_file = r'C:\Users\santo\Documents\Planificaciones\Cuarto\Cuarto\Electromagnetismo\doc.pdf'

# Convertir el archivo .docx a PDF
convert(docx_file, pdf_file)
