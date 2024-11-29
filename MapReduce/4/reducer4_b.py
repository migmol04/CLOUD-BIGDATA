#!/usr/bin/env python3
import sys

current_range = None
movies_in_range = []

for line in sys.stdin:  # Para cada línea de la entrada
    line = line.strip()
    try:
        range_id, movie_id, average_rating = line.split('\t') #sacamos el rango, el id de la pelicula , promedio 
    except ValueError:
        print(f"Línea mal formateada: {line}", file=sys.stderr)
        continue

    # Verificar si estamos en el mismo rango
    if current_range == range_id:
        movies_in_range.append(f"{movie_id} ({average_rating})") #si esta en el rango insertamos
    else:
        if current_range:                                  
            print(f"{current_range}\t{'; '.join(movies_in_range)}")   #printeamos
        current_range = range_id    #actualizamos rango
        movies_in_range = [f"{movie_id} ({average_rating})"]

# Imprimir el último rango
if current_range:
    print(f"{current_range}\t{'; '.join(movies_in_range)}")
