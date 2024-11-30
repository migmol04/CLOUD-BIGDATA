from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year
import sys

# Crear una sesión de Spark
spark = SparkSession.builder.appName("AverageClosePrice").getOrCreate()

input_path = sys.argv[1]  # Ruta al archivo CSV de entrada
output_path = sys.argv[2]  # Directorio de salida para los resultados

# Leer el archivo CSV como DataFrame
#Header es True para que tome la primera fila como encabezado
#inferSchema es True para que tome el tipo de dato de cada columna
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Calcular el promedio del precio de cierre por año
average_close_per_year = (
    df.withColumn("Year", year(col("Date")))  # Extraer el año de la fecha
      .groupBy("Year")                       # Agrupar por año
      .agg(avg("Close").alias("AverageClose"))  # Calcular el promedio del precio de cierre
      .orderBy("Year")                       # Ordenar por año
)

# Guardar los resultados en el directorio de salida
#overwrite para que si existe el archivo lo sobreescriba
average_close_per_year.write.mode("overwrite").csv(output_path, header=True)

# Detener la sesión de Spark
spark.stop()
