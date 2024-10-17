# PROYECTO 1 - ENTREGA FINAL

## Paso a paso para la ejecucion de aplicativo busqueda semantica en contenedor docker

requisitos: aplicativo docker desktop https://www.docker.com/products/docker-desktop/

- Primero debemos clonar el proyecto a un ubicacion o carpeta local en tu equipo , lo clonaremos con la instruccion "git clone https://github.com/felipkmpo/semanticsearch" la cual podras ejecutar desde algun terminal independiente o algun terminal dentro de ambiente de desarrollo que desees. (validemos que se hayan clonado todos los archivos, carpetas)

- continuamos c



instrucciones para correr Docker:

docker build -t busquedasemantica .
docker run -it busquedasemantica  (modo interactivo)
coverage

docker exec -it mi_contenedor coverage run -m unittest src/tests/test_search_engine.py
docker exec -it mi_contenedor coverage report
docker exec -it mi_contenedor  coverage html
docker cp <container_id>:<source_path> <destination_path_on_local_machine>


## Objetivos - Entrega preliminar

- Crear un repositorio haciendo uso de git.
- Crear un archivo readme explicando como ejecutar el proyecto.
- Subir los cambios necesarios al repositorio para ejecutar el proyecto.
- Crear un contenedor con docker para ejecutar por consola el proyecto.
    - ¿Cómo guardamos los datos luego de aplicar la similitud por coseno?
- Crear una función que cree una nueva columna que va a tener información relevante para los embeddings, ¿tal vez es importante tener el valor ganado de la película, o el nombre del director?.

### Rubrica
| Funcionalidad (2.5)   | Documentación    (2.5)   |
| ------------ | ------------ | 
| El código funciona según las instrucciones, desde un contenedor | Existe documentación clara en formato MarkDown de cómo ejecutar el proyecto. | 
| El proyecto está en un repositorio de git con acceso al profesor. | El código está correctamente documentado. | 
|Existe una función para aumentar el contexto de los embeddings | |
|El proyceto una vez iniciado permite realizar varias búsquedas y para su ejecución con un comando específico||

## Objetivos - Entrega final
- Crear pruebas unitarias.

- Usar las mejores prácticas teniendo en cuenta el nivel de acople y desacople de los módulos, manejo de errores, etc.
- Usar y documentar al menos un patrón de diseño.
- Documentar las funciones y el proyecto (estructura).

### Rúbrica
| Funcionalidad (2.0)   | Documentación    (0.5)   | Pruebas y calidad (1.5) | Estructura (1.0) |
| ------------ | ------------ | ------------ | ------------ | 