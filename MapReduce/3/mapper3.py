#!/usr/bin/env python3
import sys
import csv
from datetime import datetime

for line in sys.stdin:  #leemos cada linea de la entrada
    line = line.strip()
    if line.startswith('Date') or not line:   #con esta linea nos saltamos la linea de encabezado
        continue
    try:
        reader = csv.reader([line]) #utilizamos el reader de csv para no tener problemas a la hora de la lectura
        for row in reader:
            date_str = row[0] #capturamos la fecha que esta en la primera columna 
            close_price = row[4] #capturamos el precio de cierre de la quinta columna
            date = datetime.strptime(date_str, '%Y-%m-%d') #formateamos la fecha para que sea de formato datetime
            year = date.year #extraemos el año de nuestra fecha
            print(f"{year}\t{close_price}\t1") #emitimos el año y el close price
    except Exception as e:  #maneja cualquier error de formato
        continue
