import random 
def amigo_invisible(entrada):
    #convertir a lista y limpiar espacios
    participantes= [p.strip() for p in entrada.split(",")]
    #validar cantidad minima
    if len(participantes)<3:
        return("debe haber al menos tres participantes")
    #validar duplicados
    nombres_normalizados = [p.lower() for p in participantes]
    if len(nombres_normalizados) != len(set(nombres_normalizados)):
        return "No puede haber nombres duplicados." 
    # mezclar lista
    asignados = participantes.copy()
    random.shuffle(asignados)

    # asegurar que nadie se tenga a sí mismo
    for i in range(len(participantes)):
        if participantes[i] == asignados[i]:
            return amigo_invisible(entrada)  # vuelve a intentar

    # armar resultado
    resultado = []
    for i in range(len(participantes)):
        resultado.append((participantes[i], asignados[i]))

    return resultado