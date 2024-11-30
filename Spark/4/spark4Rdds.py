from pyspark import SparkContext
import sys

# Crear el contexto de Spark
sc = SparkContext(appName="AverageMovieRating")

ratings_path = sys.argv[1]  # Ruta al archivo de ratings
output_path = sys.argv[2]   # Directorio de salida para los resultados

# Leer el archivo de ratings como RDD
ratings_rdd = sc.textFile(ratings_path)

# Filtrar el encabezado y extraer (movieId, rating)
header = ratings_rdd.first()
ratings = (ratings_rdd
           .filter(lambda line: line != header)                    # Ignorar encabezado
           .map(lambda line: line.split(","))                      # Dividir por coma
           .map(lambda fields: (int(fields[1]), float(fields[2]))) # (movieId, rating)
)

# Calcular el promedio de calificaciones por movieId
average_ratings = (ratings
                   .mapValues(lambda rating: (rating, 1))                 # Mapear a (movieId, (rating, 1))
                   .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))  # Sumar ratings y contar
                   .mapValues(lambda x: x[0] / x[1])                      # Calcular promedio
)

# Asignar cada movieId a su rango de calificación
def assign_range(avg_rating):
    if 0 <= avg_rating <= 1:
        return "Range 1: [0, 1]"
    elif 1 < avg_rating <= 2:
        return "Range 2: (1, 2]"
    elif 2 < avg_rating <= 3:
        return "Range 3: (2, 3]"
    elif 3 < avg_rating <= 4:
        return "Range 4: (3, 4]"
    elif 4 < avg_rating <= 5:
        return "Range 5: (4, 5]"
    else:
        return "Out of Range"

# Asignar cada movieId a su rango de calificación
movie_ranges = average_ratings.mapValues(assign_range)

# Guardar los resultados en el directorio de salida
movie_ranges.saveAsTextFile(output_path)

# Detener el contexto
sc.stop()
