def reemplazo_sin_mayusculas(texto,palabra,reemplazo):
  resultado =""
  i=0
  largo=len(palabra)
  while i < len(texto):

        # comparar ignorando mayúsculas
        if texto[i:i+largo].lower() == palabra.lower():
            resultado += reemplazo
            i += largo
        else:
            resultado += texto[i]
            i += 1

  return resultado

def filtrar_spoilers (review,palabras_usuario):
  #convertir input a lista
  spoilers= palabras_usuario.split(",")
  texto = review
  for spoiler in spoilers:

    reemplazo = "*" + len(spoiler)

    #reemplazo sin distinguir mayuscukas
    texto = reemplazo_sin_mayusculas(texto,spoiler,reemplazo)
  return texto   