
#importamos libreria pandas, modulo "util" y "sentence trasnformers" incluidas dentro de las librerias sentence_transformers

import pandas as pd
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

"""## Entendiendo el dataset"""

# cargamos el dataset
pelis = pd.read_csv("IMDBtop1000.csv")

"""## Usando Sentence Transformer para crear embeddings"""

#cargamos en la variable "model" un modelo de sentence transformes pre-entrenado llamado "all minilm-l6-v2",
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Esta línea de código genera incrustaciones para las descripciones de las películas de su conjunto de datos utilizando el modelo Sentence Transformers preentrenado que cargamos anteriormente.
embeddings = model.encode(pelis['Description'],batch_size=64,show_progress_bar=True)

"""Esta línea de código añade una nueva columna llamada 'embeddings' a su DataFrame pelis y almacena los embeddings
generados en esa columna, por otro lado convierte las incrustaciones de una matriz NumPy a una lista."""
pelis['embeddings'] = embeddings.tolist()

"""## Calculando la similitud usando la métrica de similitud por coseno, el código define una función llamada compute_similarity que calcula la similitud entre dos embeddings, utilizando la similitud del coseno."""
def compute_similarity(example, query_embedding):
    embedding = example['embeddings']
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity

"""
    Crea una nueva columna en el DataFrame que combina el nombre del director y el valor ganado
    de la película para proporcionar más contexto.
    """
def info_rele(df_results):
    
    df_results['informacion_relevante'] = df_results.apply(lambda row: f"Director: {row['Cast']}, Valor ganado: {row['Info']}", axis=1)
    return df_results


## Ejecuntando la búsqueda
# Creamos un nuevo dataframe vacío para almacenar los resultados de búsqueda
df_results = pd.DataFrame()
#creamos un ciclo while con el fin de realizar varias busquedas hasta que el usuario decida detener la busqueda mediante la palabra salir
while True:
    query_description = input("Ingrese descripción de la película o escriba 'salir' para detener la búsqueda: ")
    if query_description.lower() == 'salir':
        break

    #convertimos la descripcion de la consulta en un embedding.
    """aqui aplicamos la funcion a cada fila del dataframe; lambda x representa una funcion anonima que toma una fila x del dataframe pelis.
    Para cada película (x), la función calcula la similitud entre el embedding de esa película y el embedding de la consulta, utilizando la similitud del coseno."""
    query_embedding = model.encode([query_description])[0] 
    pelis['similarity'] = pelis.apply(lambda x: compute_similarity(x, query_embedding), axis=1) 
   
    pelis = pelis.sort_values(by='similarity', ascending=False)
    pelis['Description_Cast'] = pelis['Description'] + ' ' + pelis['Cast']

    # Seleccionamos las columnas relevantes
    search_result = pelis[['Title', 'Description_Cast']].head()

    # Guardamos los resultados en el nuevo dataframe
    df_results = pd.concat([df_results, search_result])

    print(search_result)



# Imprimimos o guardamos el dataframe con todos los resultados
print("Resultados acumulados:")
print(df_results)
print("Busqueda Finalizada.")
