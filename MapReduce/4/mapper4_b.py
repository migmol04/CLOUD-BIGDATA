#!/usr/bin/env python3
import sys

for line in sys.stdin:  #para cada linea...
    line = line.strip()
    try:
        movie_id, average_rating, _ = line.split('\t', 2)  #Sacamos el id de la pelicula y el promedio de ratings ignorando el tercer valor (count)
        average_rating = float(average_rating)
    except ValueError:
        print(f"Línea mal formateada: {line}", file=sys.stderr)
        continue
                                                  
    if 0 <= average_rating <= 1:                         #asignamos segun el promedio un rango
        range_id = 'Range 1: [0, 1]'
    elif 1 < average_rating <= 2:
        range_id = 'Range 2: (1, 2]'
    elif 2 < average_rating <= 3:
        range_id = 'Range 3: (2, 3]'
    elif 3 < average_rating <= 4:
        range_id = 'Range 4: (3, 4]'
    elif 4 < average_rating <= 5:
        range_id = 'Range 5: (4, 5]'
    else:
        continue
#lo emitimos
    print(f"{range_id}\t{movie_id}\t{average_rating:.2f}")
