# El contenedor de postgres por defecto curre sobre el puerto 5432
FROM postgres

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 1234
ENV POSTGRES_DB Ventas

# La carpeta de initdb.d maneja los scripts que se van a ejecutar una vez se encienda el contenedor
ADD ./data/ejercicio1.sql /docker-entrypoint-initdb.d/