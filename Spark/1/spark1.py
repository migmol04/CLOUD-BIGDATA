# Distributed grep implementation
from pyspark import SparkConf, SparkContext
import re
import sys

#Configurar Spark
conf = SparkConf().setAppName('DistributedGrep')
sc = SparkContext.getOrCreate(conf)

#Entrada de argumentos
word_to_search = sys.argv[1]  # Palabra a buscar
input_path = sys.argv[2]  # Ruta del archivo de entrada

#Grep distribuido
lines_with_word = (sc.textFile(input_path)
                   .coalesce(4) # reduce el numero de particiones a 4
                   .filter(lambda line: re.search(r'\b' + re.escape(word_to_search) + r'\b', line, re.IGNORECASE))) #filtramos las lineas con las palabras

# Guarda las líneas que contienen la palabra en un archivo de texto
lines_with_word.saveAsTextFile(sys.argv[3])  # salida de la ruta

# Para
sc.stop()