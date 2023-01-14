import numpy as np

def agregar_marcos(imagen_gris, alto, ancho):
    d = len(imagen_gris.shape)
    if d == 2:
        (f, c) = imagen_gris.shape
        nueva_imagen = np.zeros((f+alto*2, c+ancho*2))
        nueva_imagen[alto:-alto, ancho:-ancho] = imagen_gris
        return nueva_imagen
    else:
        print("No es una imagen en escala de grises")