import cv2

# Cargar imagen
image_path = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\salypimienta.png"
output_file = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\salypimienta-filtrado.png"
image = cv2.imread(image_path)

# Aplicar filtro de desenfoque mediano
k = 3 # Tamaño del kernel: kxk

blur = cv2.medianBlur(image, k)

# Guardar imagen filtrada
cv2.imwrite(output_file, blur)

# Mostrar imágenes
cv2.imshow('Original', image)
cv2.imshow('Filtrado', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
