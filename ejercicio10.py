def competencia_cocina(rounds):
    stats={}

    for ronda_num,ronda in enumerate(rounds,start=1):

        theme = ronda["theme"]
        scores = ronda["scores"]

        print(f"ronda: {ronda_num}-{theme}")

        ganador=None
        mejor_puntaje=-1
        #calcular puntaje de la ronda
        for nombre,jueces in scores.items():
            puntaje = sum(jueces.values())    

            if nombre not in stats:
                stats[nombre]= {

                    "total": 0,
                    "wins": 0,
                    "best": 0,
                    "rounds": 0
                }
            
            #actualizamos estadisticas
            stats[nombre]["total"]+=puntaje
            stats[nombre]["rounds"]+=1

            if puntaje>stats[nombre]["best"]:
                stats[nombre]["best"]=puntaje
            #quien fue el ganador de la ronda
            if puntaje>mejor_puntaje:
                mejor_puntaje=puntaje
                ganador=nombre
        
        #sumamos victoria
        stats[ganador]["wins"]+=1
        print(f"Ganador: {ganador} ({mejor_puntaje} pts)")
         # tabla parcial
        print("Posiciones parciales:")
        ordenados = sorted(stats.items(), key=lambda x: x[1]["total"], reverse=True)
        
        for nombre, datos in ordenados:
            promedio = datos["total"] / datos["rounds"]
            print(f"{nombre} | {datos['total']} | {datos['wins']} | {datos['best']} | {round(promedio,1)}")
    #tabla final

    print("\nTabla de posiciones final:")
    print("Cocinero | Puntaje | Rondas ganadas | Mejor ronda | Promedio")
    #ordenamos por puntaje total, de mayor a menor
    ordenados = sorted(stats.items(), key=lambda x: x[1]["total"], reverse=True)

    for nombre, datos in ordenados:
        promedio = datos["total"] / datos["rounds"]
        print(f"{nombre} | {datos['total']} | {datos['wins']} | {datos['best']} | {round(promedio,1)}")