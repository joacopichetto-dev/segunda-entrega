def analizar_texto(texto): 
    #separamos en lineas
    lineas= texto.split("\n")
    total_lineas= len(lineas)
    total_palabras = 0
    palabras_linea=[]

    #recorremos lineas
    for linea in lineas:
        palabras= linea.split() #separamos las palabras de c/linea
        cantidad = len(palabras)
        total_palabras+=cantidad
        palabras_linea.append((linea,cantidad))

    #promedio
    promedio = int(total_palabras/total_lineas)
    #lineas por encima del promedio

    lineas_mayores=[]
    for lineas,cantidad in palabras_linea:
        if cantidad > promedio:    
           lineas_mayores.append((lineas,cantidad)) 

    return total_lineas,total_palabras,promedio,lineas_mayores           