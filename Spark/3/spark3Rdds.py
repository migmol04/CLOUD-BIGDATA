from pyspark import SparkContext
import sys

# Crear el contexto de Spark
sc = SparkContext(appName="AverageClosePrice")

input_path = sys.argv[1]  # Ruta al archivo CSV de entrada
output_path = sys.argv[2]  # Directorio de salida para los resultados

# Leer el archivo CSV como RDD
data = sc.textFile(input_path)

# Función para procesar cada línea del archivo
def process_line(line):
    # Separar los campos por coma
    fields = line.split(",")
    # Ignorar el encabezado
    if fields[0] == "Date":
        return None
    date = fields[0]
    close_price = float(fields[4])  # Campo precio de cierre en la posición 4
    year = date.split("-")[0]  # Extraer el año de la fecha
    return (year, (close_price, 1))

# Procesar el archivo, filtrando el encabezado y calculando el promedio anual
average_close_per_year = (
    data.map(process_line)                        # Mapear cada línea a (año, (precio de cierre, 1))
        .filter(lambda x: x is not None)          # Filtrar encabezado/ lineas no validas
        .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))  # Sumar precios y contar días por año
        .mapValues(lambda x: x[0] / x[1])         # Calcular el promedio de cierre anual
        .sortByKey()                              # Ordenar por año
)

# Guardar los resultados en el directorio de salida
average_close_per_year.saveAsTextFile(output_path)

# Detener 
sc.stop()
