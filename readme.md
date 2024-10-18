# PROYECTO 1 - ENTREGA FINAL
### Luis Felipe Campo Gallego

***Requisitos:*** 
- aplicativo docker desktop https://www.docker.com/products/docker-desktop/
- espacio almacenamiento minimo 20 gb solo para ejecucion proyecto
- librerias necesarias:
   - pandas y sentence-trasnformes (desarrollo y ejecucion de proyecto principal)
   - unittest y coverage (desarrollo y ejecucion de pruebas de cobertura) 
  
## Paso a paso para la ejecución de aplicativo busqueda semantica en contenedor docker
### Ejecución aplicativo busqueda semantica
- Primero debemos clonar el proyecto a un ubicacion o carpeta local en tu equipo , lo clonaremos con la instruccion "git clone https://github.com/felipkmpo/semanticsearch" la cual podras ejecutar desde algun terminal independiente o algun terminal dentro de ambiente de desarrollo que desees. (validemos que se hayan clonado todos los archivos, carpetas)

![image](https://github.com/user-attachments/assets/77b79883-822f-4f94-a35c-73c6929ad287)

- Luego de tener nuestro repositorio en local, ejecutamos el aplicativo Docker en nuestro equipo, con el fin de que los servicios esten corriendo y podamos gestionarlo desde consola con sus propios comandos.
  
    - Crearemos una imagen en docker, asi que desde la terminal ejecutamos el comando "docker build -t busquedasemantica .", (la palabra busquedasemantica será el nombre de nuestra imagen asi que se puede 
      modificar) para la creación de esta imagen es relevante tener configurado correctamente el archivo "dockerfile" ya que este es el que contiene todas las instrucciones para el correcto montaje de nuestra 
      imagen y posterio ejecución de los contenedores, aqui se incluirán instrucciones que instalarán librerias y contenido adicional que necesitamos para la correcta ejecución de nuestro proyecto; también 
      esta el archivo "requerimientos.txt" en el cual se encuentran los nombres de las librerias que necesitaremos, este archivo se utiliza para administrar ordenadamente las librearias necesarias.
  
      ![image](https://github.com/user-attachments/assets/f290ba7f-6f74-4b4a-9f55-b14cc9cbf004)
      ![image](https://github.com/user-attachments/assets/857fbddf-9ebf-4409-943d-8296bf5e9cb8)

        ***observacion:*** Dentro del archivo dockerfile, se encuentra el comando "CMD [ "python","src/semantic_search_students.py" ]", el "archivo semantic_search_students.py" es donde esta almacenado
        el código nuestro aplicativo principal, el cual queremos que se ejecute desde el inicio, con la palabra "python" le estamos diciendo a docker que lo ejecute con el compilador de python, de esta manera 
        cuando se corra el contenedor ejecutará este archivo.
    - Cuando termine de ejecutar el comando anterior, abrimos el aplicativo docker y validamos que la imagen  se haya creado correctamente, si no se encuentra, valida el directorio de archivos,el archivo 
    dockerfile este debe esta en la raiz de nuestro directorio.
      ![image](https://github.com/user-attachments/assets/ae2aaf60-44b3-4ac1-8b3f-494bd6080315)
        ***observación:*** este proyecto utilizará las librerias de sentence-transformers la cual son pesadas, nuestra imagen quedara de 10gb aproximadamente.
    - Con la imagen creada podremos continuar con la ejecución de nuestro proyecto, para esto ejecutaremos el comando "docker run -it busquedasemantica" en nuestra terminal, con esto se creará el contenedor, 
    el cual automáticamente ejecutará nuestro aplicativo, para validar la puesta en marcha del contenedor dentro del aplciativo dokcer desktop, vamos a la pestaña "containers" y ahi visualizaremos el nuevo 
     contenedor, los nombre de estos son aleatorios, a comparacion del nombre de la imagen que si la parametrizamos.
     ![image](https://github.com/user-attachments/assets/a998316a-bb5d-4448-8471-9818cd08138c)

     ![image](https://github.com/user-attachments/assets/1b04d739-d643-4066-99d4-54288761c489)

      El aplicativo nos pedirá una descripcion corta sobre que tematica de pelicula nos gustaria ver, y posteriormente nos arrojará recomendaciones de peliculas relacionadas con dicha descripción.
      ![image](https://github.com/user-attachments/assets/df284cbe-102f-44c4-8dc2-d95a410e8b0a)

      ***observación:*** podremos seguir realizando busquedas hasta que digitemos la palabra salir.
 
      ***Nota importante: Dejaremos ejecutando el proyecto para poder continuar con la ejecución de pruebas, si finalizamos nuestra busqueda con la palabra "salir" el contenedor se detendra y no
      podremos seguuir utilizando la linea de comandos dentro del contenedor***

  ### Pruebas y cobertura aplicativo

   - Con el fin de garantizar un desarrollo idóneo del proyecto, se desarrollaron pruebas unitarias para validar la calidad del proyecto, las pruebas las podremos ejecutar y validar de la siguiente manera:
     
        - Abrimos una nueva terminal desde nuestro entorno de desarrollo o prompt elegido, y ejecutamos la siguiente instrucción "docker exec -it mi_contenedor coverage run -m unittest 
          tests/test_search_engine.py", (aqui estamos utilizando coverage que es una librería que nos permite medir la cobertura de las pruebas diseñas) la palabra "mi_contenedor" debe ser reemplazada por el 
          id del contenedor, este id lo obtenemos digitando el comando "docker ps"; tambien es importante el archivo que contiene las pruebas, el cual esta dentro de la carpeta "tests".
  
          ![image](https://github.com/user-attachments/assets/2b1ad691-c2c6-4761-ba53-7a5c9b2e33a2)

        - Cuando ejecutemos el comando anterior veremos que son ejecutadas varias barras de carga, eso depende de la cantidad de pruebas, esperamos que termine la ejecución y podremos obtener la cantidad
          de pruebas realizadas, para este ejercicio fueron 8.
          ![image](https://github.com/user-attachments/assets/8cfcc494-6d91-473e-be10-12bd21757937)

        - Ahora utilizaremos el comando "docker exec -it mi_contenedor coverage report" (tener presente cambiar id contenedor), con el objetivo de visualizar el procentaje de cobertura que tiene las pruebas
          diseñadas, para este ejercicio se obtiene un 74% de cobertura sobre el archivo "semantic_search_students.py".

          ![image](https://github.com/user-attachments/assets/4f204491-e8f1-44d1-9904-a11cb824d5cd)

        - Por último gracias a las librerias de coverage podremos visualizar en detalle los resultados de las pruebas de cobertura, asi que ejecutamos el comando "docker exec -it mi_contenedor  coverage html"
          (tener presente cambiar id contenedor)
          
          ![image](https://github.com/user-attachments/assets/ba054312-fa92-46f3-9a78-3e74d9d9d0af)

        - Para poder visualizar el detalle del test de cobertura necesitamos copiar o descargar la carpeta "htmlcov", abriremos el aplicativo docker desktop, vamos a la pestaña "containers", damos clic sobre           el nombre del contenedor en ejecución, damos clic a la pestañas files, dentro de app se encontrará la carpeta "htmlcov", damos clic derecho save o guardar, y la almacenados en alguna ubicacion local           de nuestro equipo.
          
        ![image](https://github.com/user-attachments/assets/97fcd073-e3a8-49a7-8dee-70a7b99a200a)



     ***observación:*** Para ver en detalle el test de cobertura debemos ejecutar el archivo index.html de la carpeta htmlcov

        ![image](https://github.com/user-attachments/assets/acf91519-b920-4c96-9aeb-06a85e719cc8)

        Aqui podremos identificar todos los archivos sobre los que se ejecutaron las pruebas coverage, el archivo relevante para nosotros es "test_search_engine.py"

       ![image](https://github.com/user-attachments/assets/3d8f2271-3c65-4b0e-a200-176d809936ee)



