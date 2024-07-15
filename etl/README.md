# Ejercicio 1
Se realiza un proceso de ETL utilizando Python para leer datos de un archivo CSV y cargarlos en una base de datos PostgreSQL utilizando Docker comopose.


Ejecuta el siguiente comando para construir la imagen basada en Docker.
> $ sudo docker build . --tag ejercicio1

Revisamos los contenedores de docker que están ejecutandose.
> $ sudo docker images

Se ejecuta el contenedor utilizando la imagen creada, el -d es para que corra en segundo plan.
> $ sudo docker run -d ejercicio1

Verifica el estado del contenedor.
> $ sudo docker ps

Nos conectamos al contenedor en ejecución para revisar que el servicio de PostgreSQL esté funcionando correctamente.
> $ sudo docker exec -it ejercicio1 /bin/bash

Una vez conectado al contenedor, ingresa al servicio de PostgreSQL.
> $ psql -U postgres

Inicia los servicios definidos en el archivo de Docker compose
> $ sudo docker compose up -d 