import cv2
# Cargar imagen
rutaoriginal = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCVV\\oso.jpg"
image = cv2.imread(rutaoriginal)
# guardar copia como png
rutaimagencopiada = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCVV\\copia-lunes_oso.jpg"
cv2.imwrite(rutaimagencopiada, image)
# cargar copia
copiaimagen = cv2.imread(rutaimagencopiada)
# mostrar
cv2.imshow('Original', image)
cv2.imshow('Copia', copiaimagen)
cv2.waitKey(0)
cv2.destroyAllWindows()