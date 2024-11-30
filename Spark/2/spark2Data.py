from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, split
import sys

# Crear la sesión de Spark
spark = SparkSession.builder.appName("CountURLAccessFrequency").getOrCreate()

# Ruta de entrada y salida
input_path = sys.argv[1]  # Archivo de log de entrada
output_path = sys.argv[2]  # Directorio de salida

# Leer el archivo de logs como DataFrame
df = spark.read.text(input_path)

# Ajustar el patrón sin grupos con nombres
# Captura el método, URL y protocolo
pattern = r'"(\S+)\s(\S+)\s(\S+)"'

# Extraer la URL utilizando regexp_extract (índice 2 corresponde a la URL)
urls = (
    df.withColumn("url", regexp_extract(col("value"), pattern, 2))  # Extraer URL
      .withColumn("base_url", split(col("url"), r'\?').getItem(0))  # Obtener la URL base antes del '?'
      .filter(col("url").isNotNull())  # Filtrar líneas inválidas
)

# Contar las ocurrencias de cada URL
url_counts = urls.groupBy("base_url").count()

# Guardar el resultado
url_counts.write.mode("overwrite").csv(output_path)  # Guardar en formato CSV

# Detener la sesión de Spark
spark.stop()
