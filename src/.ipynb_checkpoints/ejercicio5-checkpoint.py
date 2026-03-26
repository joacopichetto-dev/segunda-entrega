def calcular_costo (peso,zona):
    zona = zona.lower() #por las dudas

    #validamos la zona
    if zona not in ["local","regional","nacional"]:
        return("error, la zona no es valida")
    #validar por peso
    if peso <=1:
        if zona == "local":
            costo= 500
        elif zona == "regional":
            costo= 1000
        else: costo= 2000
    elif peso<=5:
        if zona == "local":
            costo= 1000
        elif zona == "regional":
            costo= 2500
        else: costo= 4500     
    else:
        if zona == "local":
            costo= 2000
        elif zona == "regional":
            costo= 5000
        else: costo= 8000    
    return costo    