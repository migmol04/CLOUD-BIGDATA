from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys
import re

# Configurar Spark
spark = SparkSession.builder.appName('DistributedGrepDF').getOrCreate()

# Entrada de argumentos
word_to_search = sys.argv[1]  # Palabra a buscar
input_path = sys.argv[2]  # Ruta del archivo de entrada
output_path = sys.argv[3]  # Ruta de salida

# Leer el archivo como DataFrame
df = spark.read.text(input_path)  # Crea un DataFrame con una sola columna llamada "value" que contiene las líneas

# Filtrar las líneas que contienen la palabra buscada
# rlike es una función de Spark SQL que permite usar expresiones regulares
# (?i) es un modificador para hacer la búsqueda insensible a mayúsculas y minúsculas
# \b es un límite de palabra para que coincida con la palabra completa
# re.escape se utiliza para escapar cualquier carácter especial en la palabra buscada
# col("value") se refiere a la columna "value" del DataFrame
# El resultado es un nuevo DataFrame con las líneas que contienen la palabra buscada
lines_with_word = df.filter(
    col("value").rlike(r'(?i)\b' + re.escape(word_to_search) + r'\b')
)


# Guardar el resultado en un archivo CSV
lines_with_word.write.mode("overwrite").csv(output_path, header=False)

# Detener Spark
spark.stop()
