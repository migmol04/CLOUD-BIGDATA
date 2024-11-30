from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import sys
# Crear la sesión de Spark
spark = SparkSession.builder.appName("AverageMeteoriteMass").getOrCreate()

input_path = sys.argv[1]  # Ruta al archivo CSV de entrada
output_path = sys.argv[2] # Directorio de salida para los resultados

# Leer el archivo CSV como DataFrame
# Header es True para que tome la primera fila como encabezado
# inferSchema es True para que tome el tipo de dato de cada columna
# sep es el separador de columnas
df = spark.read.csv(input_path, header=True, sep=";", inferSchema=True)

# Filtrar filas sin masa y calcular el promedio por tipo (recclass)
average_mass_per_type = (
    df.filter(col("mass (g)").isNotNull())  # Filtrar filas con masa nula
      .groupBy("recclass")                 # Agrupar por tipo de meteorito
      .agg(avg("mass (g)").alias("avg_mass"))  # Calcular promedio de masa
      .orderBy("recclass")                 # Ordenar por tipo de meteorito
)

# Guardar los resultados en el directorio de salida
# overwrite para que si existe el archivo lo sobreescriba
# header=True para que tome la primera fila como encabezado
average_mass_per_type.write.mode("overwrite").csv(output_path, header=True)

# Detener la sesión de Spark
spark.stop()
