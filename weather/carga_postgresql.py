import pandas as pd
import psycopg2
from api_weather import get_weather_data


cities = ["Miami", "London", "Paris", "Barcelona", "Madrid"]
key = "482ed3291eb0845ec7abf2c7fde2840e"

data_weather = get_weather_data(key = key, *cities)

# Establecer la conexión a PostgreSQL
conexion = psycopg2.connect(
    dbname="Clima",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)


# Crear un cursor para ejecutar las consultas de SQL
cursor = conexion.cursor()


try:
    # Iterar sobre cada fila del DataFrame
    #index es el índice de la fila y row es un objeto que contiene los datos de la fila
    for index, row in ciudades.iterrows():
        # Ejecutar la consulta SQL de inserción para cada fila
        cursor.execute(
            "INSERT INTO ciudades ('city', 'temperature', 'humidity', 'weather') VALUES (%s, %s, %s, %s);",
            (row['city'], row['temperature'], row['humidity'], row['weather'])
        )
        print(f"Fila {index} insertada correctamente en PostgreSQL.")

    # Confirmar todos los nuevos ingresos de los registros al finalizar el bucle
    conexion.commit()

except (Exception, psycopg2.Error) as error:
    print("Error al insertar datos en PostgreSQL:", error)

finally:
    # Cerrar el cursor y la conexión
    # Calidar que conexion no sea None
    # Se asegura que no se va a cerrar una conexión que no se abrió 
    if conexion:
        cursor.close()
        conexion.close()
        print("Conexión a PostgreSQL cerrada.")

