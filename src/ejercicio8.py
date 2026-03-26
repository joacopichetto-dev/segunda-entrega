def cifrar_cesar(mensaje,desplazamiento):
    resultado = ""

    for char in mensaje:
        if char.isalpha(): #preguntamos si es una letra
            if char.islower():
                base = ord("a")
            else:
                base = ("A")

            #convertimos a numero 
            pos = ord(char)-base

            #aplico el desplazamiento con rotacion
            nueva_pos = (pos + desplazamiento) % 26
            #volver a la letra
            nuevo_char = chr(base + nueva_pos)

            resultado +=nuevo_char 
        else:
            resultado+=char #no se modifica
    return resultado            