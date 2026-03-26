def analizar_playlist(playlist):
    total_segundos = 0
    mas_larga = None 
    mas_corta = None
    max=-1
    min= 9999999
    for cancion in playlist:
        duracion = cancion["duration"] #pedimos el valor asociado a la clave duration
        #separar minutos de segundos 
        minutos,segundos = duracion.split(":")
        minutos = int(minutos)
        segundos = int (segundos)

        total = minutos *60 + segundos 
        #acumular duracion total
        total_segundos+=total

        #buscar mas larga
        if total>max :
            max=total
            mas_larga=(cancion["title"],total,duracion)
        #buscar la mas corta
        if total<min: 
            min=total
            mas_corta=(cancion["title"],total,duracion)
    #convertir total a minutos y segundos
    total_min = total_segundos //60
    total_sec = total_segundos % 60

    return total_min,total_sec,mas_larga,mas_corta        