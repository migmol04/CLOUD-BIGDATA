#!/usr/bin/env python3
import sys
import re

# Expresión regular para extraer la URL de la línea de registro
#\" busca el carácter de comillas ("), que aparece antes y después de la solicitud HTTP en cada línea de registro
#(?P<method>\S+) captura el metodo http
#\s nos ayuda a buscar un espacio en blanco para separar bien nuestra "estructura"
#?P<url>\S+) captura la url
#(?P<protocol>\S+) captura el http y el protocolo
patron = re.compile(r'\"(?P<method>\S+)\s(?P<url>\S+)\s(?P<protocol>\S+)\"')

for line in sys.stdin:
    line = line.strip()
    match = patron.search(line)  #intentamos buscar coincidencias en la linea actual
    if match:
        url = match.group('url') #extraemos la url
        print(f"{url}\t1") # la printeamos
