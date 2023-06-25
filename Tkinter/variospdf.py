import os
from docx2pdf import convert

# Ruta a la carpeta que contiene los archivos .docx
#docx_folder = r'ruta/a/la/carpeta'
#docx_folder = r'C:\Users\santo\Documents\Planificaciones\Cuarto\Cuarto\Electromagnetismo'
# Recorrer todos los archivos en la carpeta
docx_folder = r'C:\Users\santo\Desktop\Conversiones\Nueva carpeta'
for file_name in os.listdir(docx_folder):
    # Comprobar si el archivo es .docx
    if file_name.endswith('.docx'):
        # Ruta al archivo .docx
        docx_file = os.path.join(docx_folder, file_name)
        # Ruta de salida para el archivo PDF
        pdf_file = os.path.join(docx_folder, os.path.splitext(file_name)[0] + '.pdf')
        # Convertir el archivo .docx a PDF
        convert(docx_file, pdf_file)
