#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin: #leemos cada linea
    line = line.strip()
    if line.startswith('userId') or not line: #omitimos el encabezado o cualquier linea vacia al principio de cada fichero
        continue
    try:
        reader = csv.reader([line]) #usamos csv reader para leer el archivo csv
        for row in reader:     #para cada fila obtenemos el id de la pelicula y su rating
            movie_id = row[1]
            rating = float(row[2])                       
            print(f"{movie_id}\t{rating}\t1")  #emitimos el id de la pelicula y su rating
    except Exception as e:   #hacemos que salte la excepcion en cualququier caso de mal formato
        continue
