#!/usr/bin/env python3
import sys

current_year = None  #inicializmos el año actual a None
sum_close_price = 0.0 #la suma acumulada de los precios
count = 0 #mantiene el numero de registros totales

for line in sys.stdin: #para cada linea...
    line = line.strip()
    year, close_price, cnt = line.split('\t')  #extraemos el año, el precio de cierre y el contador de los registros
    try:
        close_price = float(close_price)         #comprobamos que son numeros validos
        cnt = int(cnt)
    except ValueError:
        continue

    if current_year == year:                          #si estamos en el mismo año
        sum_close_price += close_price * cnt          #sumamos a la suma acumulada el precio de cierre * el registro
        count += cnt                                  # vamos acumulando en el contador
    else:
        if current_year:                             # entramos en otro año..
            average = sum_close_price / count        #calculamos el promedio  con la suma acumulada y el contador
            print(f"{current_year}\t{average:.2f}\t{count}")       #emitimos el año actual, el promedio y el contador
        current_year = year
        sum_close_price = close_price * cnt
        count = cnt

if current_year == year:            #emitimos el ultimo año
    average = sum_close_price / count
    print(f"{current_year}\t{average:.2f}\t{count}")
