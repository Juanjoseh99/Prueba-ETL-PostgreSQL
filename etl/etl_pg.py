import pandas as pd
import psycopg2

clientes = pd.read_csv("clientes_data.csv")


# Establecer la conexión a PostgreSQL
conexion = psycopg2.connect(
    dbname="Ventas",
    user="postgres",
    password="1234",
    host="postgres",
    port="5432"
)

# Crear un cursor para ejecutar las consultas de SQL
cursor = conexion.cursor()

try:
    cursor.execute("TRUNCATE clientes;")
    # Iterar sobre cada fila del DataFrame
    #index es el índice de la fila y row es un objeto que contiene los datos de la fila
    for index, row in clientes.iterrows():
        # Ejecutar la consulta SQL de inserción para cada fila
        cursor.execute(
            "INSERT INTO clientes (id_cliente, nombre, apellido, email) VALUES (%s, %s, %s, %s);",
            (row['id_cliente'], row['nombre'], row['apellido'], row['email'])
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
