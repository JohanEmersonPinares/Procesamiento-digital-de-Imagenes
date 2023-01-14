def convertir_rgb_gris(imagen_rgb):
    (f, c, d) = imagen_rgb.shape
    if d == 3:
        r = imagen_rgb[:,:,0]
        g = imagen_rgb[:,:,1]
        b = imagen_rgb[:,:,2]
        imagen_gris = 0.299*r + 0.587*g + 0.114*b
        (a,l)=imagen_gris.shape
        return (imagen_gris)
        
        