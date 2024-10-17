"""
PATRON DE DISEÑO
Con el objetivo de mejorar el diseño y hacerlo mas escalable y mantenible, implementamos el patrón de diseño "Factory Method", 
Este patrón nos permitirá encapsular la creación de diferentes partes del proceso de búsqueda en clases separadas, 
facilitando la extensión o modificación del comportamiento sin alterar el código existente.

Para la Implementación del patrón Factory Method realizamos lo siguiente:
Crear una clase base SearchEngine que defina la interfaz de búsqueda.
Crear subclases concretas que implementen el comportamiento específico de la búsqueda de similitudes y generación de resultados.
Encapsular la lógica repetitiva y mejorar la separación de responsabilidades.

PRINCIPIOS SOLID

El principio "Liskov Substitution Principle (LSP)" se sigue correctamente, ya que la subclase CosineSimilaritySearchEngine es 
intercambiable con la clase base MotorBusqueda.

Relacionado con el prinicipio "single responsability principle (SRP)", el codigo implementado tiene buena adherencia en la mayoria de sus componentes;
las clases y funciones estan bien separadas, cada una con su propia responsabilidad.

Relacionado con el principio "open/closed principle (OCP)",se ve implementado en la clase base MotorBusuqeda ya que esta diseñada para que se puedan agregar 
nuevos motores de busqueda sin modificar el codigo.

"""

import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Función para ampliar el contexto de los embeddings
def ampliarcontexto(row):
    """
    Ampliamos el contexto de la descripción de la película añadiendo el reparto, director y valor ganado.
    """
    description = row['Description']
    cast = row.get('Cast', '')
    info = row.get('Info', '') 

    # Concatenamos la descripción con la información adicional
    context_description = f"{description}. Cast: {cast}. Info: {info}."
    return context_description

# Ampliamos las descripciones antes de crear los embeddings
def generate_embeddings_with_context(dataset, model):
    """
    Función que genera embeddings utilizando descripciones enriquecidas con contexto adicional.
    """
    # Creamos una nueva columna en el dataset con las descripciones ampliadas
    dataset['context_description'] = dataset.apply(ampliarcontexto, axis=1)

    # Generamos los embeddings para las descripciones ampliadas
    embeddings = model.encode(dataset['context_description'], batch_size=64, show_progress_bar=True)

    # Guardamos los embeddings en una nueva columna
    dataset['embeddings'] = embeddings.tolist()

    return dataset

# Clase base para el motor de búsqueda
class MotorBusqueda:
    def __init__(self, model_name: str):
        # Cargamos el modelo de embeddings
        self.model = SentenceTransformer(model_name)

    def compute_similarity(self, example_embedding, query_embedding):
        raise NotImplementedError("Debe implementarse en subclases")

    def search(self, query_description, dataset):
        raise NotImplementedError("Debe implementarse en subclases")

# Subclase concreta que implementa la búsqueda por similitud de coseno
class CosineSimilaritySearchEngine(MotorBusqueda):
    def __init__(self, model_name: str, dataset_path: str):
        super().__init__(model_name)
        # Cargamos el dataset
        self.dataset = pd.read_csv(dataset_path)

        # Ampliamos las descripciones con contexto antes de generar los embeddings
        self.dataset = generate_embeddings_with_context(self.dataset, self.model)

    def compute_similarity(self, example_embedding, query_embedding):
        # Calculamos la similitud de coseno
        return util.cos_sim(example_embedding, query_embedding).item()

    def search(self, query_description):
        # Convertimos la consulta en un embedding
        query_embedding = self.model.encode([query_description])[0]

        # Calculamos la similitud de cada película con la consulta
        self.dataset['similarity'] = self.dataset.apply(lambda x: self.compute_similarity(x['embeddings'], query_embedding), axis=1)

        # Ordenamos por similitud descendente
        results = self.dataset.sort_values(by='similarity', ascending=False)

        # Retornamos los primeros 5 resultados
        return results[['Title', 'Description', 'Cast',  'Info']].head()

# Función para ejecutar la búsqueda interactiva
def interactive_search(search_engine):
    df_results = pd.DataFrame()

    while True:
        query_description = input("Ingrese descripción de la película o escriba 'salir' para detener la búsqueda: ")
        if query_description.lower() == 'salir':
            break

        # Ejecutamos la búsqueda
        search_result = search_engine.search(query_description)
        
        # Concatenamos los resultados
        df_results = pd.concat([df_results, search_result])

        # Mostramos los resultados de la búsqueda actual
        print(search_result)


    # Imprimimos todos los resultados acumulados
    print("Resultados acumulados:")
    print(df_results)

# Uso del patrón Factory Method
if __name__ == "__main__":
    # Instanciamos el motor de búsqueda con similitud de coseno
    cosine_search_engine = CosineSimilaritySearchEngine('sentence-transformers/all-MiniLM-L6-v2', 'src/IMDBtop1000.csv')

    # Ejecutamos la búsqueda interactiva
    interactive_search(cosine_search_engine)
