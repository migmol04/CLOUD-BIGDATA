#!/usr/bin/env python3
import sys

current_movie_id = None            #id de la pelicula que etsamos viendo
sum_ratings = 0.0                  #variable para acumular
count = 0                          #contador

for line in sys.stdin:        #para cada linea
    line = line.strip()
    movie_id, rating, cnt = line.split('\t')     #sacamos el id de la pelicula, el rating y llevamos un contador
    try:
        rating = float(rating)                 
        cnt = int(cnt)
    except ValueError:
        continue

    if current_movie_id == movie_id:    # si estamos en la pelicula
        sum_ratings += rating * cnt    #vamos acumulando 
        count += cnt                  #sumamos al contador
    else:
        if current_movie_id:               #si cambiamos de pelicula
            average = sum_ratings / count         #calculamos el promedio
            print(f"{current_movie_id}\t{average:.2f}\t{count}")      #imprimimos el id de la pelicula  el promedio y count
        current_movie_id = movie_id
        sum_ratings = rating * cnt
        count = cnt

if current_movie_id == movie_id:           #imprimimos la ultima pelicula
    average = sum_ratings / count
    print(f"{current_movie_id}\t{average:.2f}\t{count}")
