from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, when, expr
import sys

# Crear la sesión de Spark
spark = SparkSession.builder.appName("AverageMovieRating").getOrCreate()

ratings_path = sys.argv[1]  # Ruta al archivo de ratings 
output_path = sys.argv[2]   # Directorio de salida para los resultados

# Leer el archivo CSV como DataFrame
#Header es True para que tome la primera fila como encabezado
#inferSchema es True para que tome el tipo de dato de cada columna
df = spark.read.csv(ratings_path, header=True, inferSchema=True)

# Calcular el promedio de calificaciones por movieId
average_ratings = (
    df.groupBy("movieId")                    # Agrupar por movieId
      .agg(avg("rating").alias("avg_rating"))  # Calcular el promedio de calificaciones
)

# Asignar rangos de calificación
movie_ranges = (
    average_ratings.withColumn(
        "rating_range",
        when((col("avg_rating") >= 0) & (col("avg_rating") <= 1), "Range 1: [0, 1]")
        .when((col("avg_rating") > 1) & (col("avg_rating") <= 2), "Range 2: (1, 2]")
        .when((col("avg_rating") > 2) & (col("avg_rating") <= 3), "Range 3: (2, 3]")
        .when((col("avg_rating") > 3) & (col("avg_rating") <= 4), "Range 4: (3, 4]")
        .when((col("avg_rating") > 4) & (col("avg_rating") <= 5), "Range 5: (4, 5]")
        .otherwise("Out of Range")
    )
)

# Guardar los resultados en el directorio de salida
#overwrite para que si existe el archivo lo sobreescriba
#header=True para que tome la primera fila como encabezado
movie_ranges.write.mode("overwrite").csv(output_path, header=True)

# Detener la sesión de Spark
spark.stop()
