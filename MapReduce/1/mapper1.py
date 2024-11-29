#!/usr/bin/python
import sys

#extraemos la palabra de la linea de comandos
palabra = sys.argv[1].lower()


for line in sys.stdin:
    line = line.strip()
    if palabra in line.lower().split():  #si la palabra esta en la linea la printeamos
        print(line)
