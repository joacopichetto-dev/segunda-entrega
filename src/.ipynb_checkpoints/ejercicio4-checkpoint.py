def validar_email(email):
    #hay exactamente un @
    if email.count("@") != 1:
         return False
    
    #no empieza ni termina con @ o .
    if email[0] in "@." or email[-1] in "@.":
         return False
    
    #separar usuario y dominio
    usuario,dominio = email.split("@")

    #al menos un caracter antes del arroba, como separamos usuario y dominio, solo debemos preguntar si usuario esta vacio o no
    if len(usuario) == 0: 
         return False
    #contiene al menos un . despues del @
    if "." not in dominio: 
        return False
    #parte final, despues del ultimo punto
    partes = dominio.split(".") #separo el dominio en una lista
    if (len(partes[-1])< 2):#analizo la ultima palabra de esa lista
         return False
    
    return True 
