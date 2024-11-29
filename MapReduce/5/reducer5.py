#!/usr/bin/env python3
import sys

current_recclass = None
total_mass = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) != 3:
        continue

    recclass, mass, cnt = parts

    try:
        mass = float(mass)
        cnt = int(cnt)
    except ValueError:
        continue

    # Si la clase actual coincide, acumula la masa y el contador
    if current_recclass == recclass:
        total_mass += mass
        count += cnt
    else:
        # Si es una nueva clase de meteorito, imprime el promedio anterior
        if current_recclass:
            average_mass = total_mass / count
            print(f"{current_recclass}\t{average_mass:.2f}\t{count}")
        
        # Actualiza a la nueva clase de meteorito
        current_recclass = recclass
        total_mass = mass
        count = cnt

# Imprime el promedio para la última clase de meteorito
if current_recclass:
    average_mass = total_mass / count
    print(f"{current_recclass}\t{average_mass:.2f}\t{count}")
