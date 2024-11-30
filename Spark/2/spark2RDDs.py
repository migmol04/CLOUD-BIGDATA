from pyspark import SparkConf, SparkContext
import sys
import re

# Configurar Spark
conf = SparkConf().setAppName('CountURLAccessFrequency')
sc = SparkContext.getOrCreate(conf)

"""Patron que queremos buscar en el archivo de logs: 
   "(?P<method>\S+)\s(?P<url>\S+)\s(?P<protocol>\S+)"
   - method: captura Método HTTP 
   -url: captura la URL solicitada
   -protocol: captura el protocolo HTTP 
"""
# Ruta de entrada y salida
input_path = sys.argv[1]  # Archivo de log de entrada
output_path = sys.argv[2]  # Directorio de salida

# Procesamiento directo usando lambdas
url_counts = (sc.textFile(input_path)  #para cada linea del archivo
              .map(lambda line: re.search(r'"(?P<method>\S+)\s(?P<url>\S+)\s(?P<protocol>\S+)"', line))  # Buscar patrón
              .filter(lambda match: match is not None)  # Filtrar líneas inválidas
              .map(lambda match: match.group('url').split('?')[0])  # Obtener URL base
              .map(lambda url: (url, 1))  # Crear pares (URL, 1)
              .reduceByKey(lambda a, b: a + b))  # Reducir por clave para contar frecuencias

# Guardar el resultado
url_counts.saveAsTextFile(output_path)

# Detener 
sc.stop()
