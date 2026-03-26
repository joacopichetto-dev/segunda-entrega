def normalizar_alumnos(students):
    alumnos = {}

    for alumno in students:
        nombre = alumno["name"]
        nota = alumno["grade"]
        estado = alumno["status"]

        #validar nombre
        if nombre is None or nombre.strip() =="":
            continue 
        #validar nota
        if nota is None or not nota.isdigit():
            continue 
        #limpiar normalizar 
        nombre = nombre.strip().title()
        nota = int(nota)
        estado = estado.strip().title()

        #eliminar duplicados
        if nombre in alumnos :
            if nota>alumnos[nombre]["grade"]:
                alumnos[nombre]={"grade": nota, "status": estado}
        else:
           alumnos[nombre]= {"grade": nota, "status": estado}        
    #ordenamos alfabeticamente
    alumnos_ordenados= sorted(alumnos.items())   
    return alumnos_ordenados    