#!/usr/bin/env python3
import sys

current_url = None #la usaremos para almacenar la url actual
current_count = 0 #un contador para contar urls

for line in sys.stdin:            #recorremos cada linea de la entrada
    line = line.strip()   
    url, count = line.split('\t', 1)        #capturamos la url y le asignamos un contador con valor 1
    try:
        count = int(count)                #convertimos a int y comprobamos que sea un valor valido
    except ValueError:
        continue

    if current_url == url:                #si la url coincide le sumamos count a current count
        current_count += count
    else:
        if current_url:                 #si cambiamos de url
            print(f"{current_url}\t{current_count}") #la printeamos
        current_url = url            #reseteamos la url
        current_count = count        #reseteamos current_count

#al salir del bucle nos aseguramos que imprime la ultima url
if current_url == url:
    print(f"{current_url}\t{current_count}")
