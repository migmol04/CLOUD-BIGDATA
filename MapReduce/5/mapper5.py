#!/usr/bin/env python3
import sys
import csv


reader = csv.reader(sys.stdin, delimiter=';')   # Configura el lector de CSV con punto y coma como delimitador
header = next(reader, None)  # Salta el encabezado si existe

for row in reader:
    try:

        if len(row) < 5:
            continue

        recclass = row[3].strip()  # Índice 3 para la clase
        mass = row[4].strip()      # Índice 4 para la masa
        if mass:
            mass = float(mass)  # Verifica que la masa no esté vacía, y conviértela a float
            print(f"{recclass}\t{mass}\t1")
    except IndexError: # Ignoramos líneas con menos columnas de las esperadas
        continue
    except ValueError:  # Ignoramos conversiones fallidas de mass a float
        continue
