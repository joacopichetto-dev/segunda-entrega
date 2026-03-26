def analizar_hashtags(posts):
    hashtags =[]

    for post in posts:

        palabras = post.split()

        for palabra in palabras:

            if palabra[0]==("#"):
                #limpiamos posibles saltos de linea
                hashtag = palabra.strip()

                #contamos frecuencia 
                if hashtag in hashtags:
                    hashtags[hashtag]+=1
                else: hashtags[hashtag]=1    
    trending ={}
    for tag,cantidad in hashtags.items():
        if cantidad > 1:
            trending[tag]=cantidad

    return hashtags,trending