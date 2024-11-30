from pyspark import SparkContext
import sys

# Crear el contexto de Spark
sc = SparkContext(appName="AverageMeteoriteMass")

input_path = sys.argv[1]  # Ruta al archivo CSV de entrada
output_path = sys.argv[2] # Directorio de salida para los resultados

# Leer el archivo CSV como RDD
data = sc.textFile(input_path)

# Función para procesar cada línea
def process_line(line):
    fields = line.split(";")
    # Ignorar el encabezado y entradas sin masa
    if fields[0] == "name" or fields[4] == '':
        return None
    # Extraer clase de meteorito y masa, devolver (recclass, (mass, 1))
    recclass = fields[3]
    mass = float(fields[4])
    return (recclass, (mass, 1))

# Procesar el archivo, filtrando el encabezado y calculando el promedio de masa
average_mass_per_type = (
    data.map(process_line)                        # Mapear cada línea a (recclass, (mass, 1))
        .filter(lambda x: x is not None)          # Filtrar entradas sin masa y el encabezado
        .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))  # Sumar masas y contar meteoritos por tipo
        .mapValues(lambda x: x[0] / x[1])         # Calcular el promedio de masa por tipo de meteorito
        .sortByKey()                              # Ordenar por tipo de meteorito
)


# Guardar los resultados en el directorio de salida
average_mass_per_type.saveAsTextFile(output_path)

# Detener 
sc.stop()
