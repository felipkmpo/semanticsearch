import unittest
import pandas as pd
from unittest.mock import patch
from src.semantic_search_students import CosineSimilaritySearchEngine, ampliarcontexto, MotorBusqueda,generar_embeddings_con_contexto,interactive_search
from sentence_transformers import SentenceTransformer, util

class TestAmpliarContexto(unittest.TestCase):
    #mediante esta prueba comprobamos que la funcion ampliarcontexto devuleve al desripcion ampliada correctamente
    #Esta función debe devolver la descripción ampliada en forma de cadena de texto, concatenando la descripción original con la información adicional de cast e info
    def test_ampliar_contexto(self):
        row = pd.Series({'Description': 'Esta es una descripción', 'Cast': 'Juan, Ana', 'Info': 'Película de acción'})
        resultado = ampliarcontexto(row)
        self.assertEqual(resultado, 'Esta es una descripción. Cast: Juan, Ana. Info: Película de acción.')

class TestGenerateEmbeddingsWithContext(unittest.TestCase):
    #el resultado esperado de esta prueba prueba qes que la función debe generar los embeddings y agregarlos como una nueva columna en el dataset.
    def test_generate_embeddings_with_context(self):
        dataset = pd.DataFrame({'Description': ['Descripción 1', 'Descripción 2'], 'Cast': ['Juan, Ana', 'Pedro, María'], 'Info': ['Película de acción', 'Película de comedia']})
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        resultado = generar_embeddings_con_contexto(dataset, model)
        self.assertIn('context_description', resultado.columns)
        self.assertIn('embeddings', resultado.columns)

class TestMotorBusqueda(unittest.TestCase):
    def test_init(self):
        model_name ='sentence-transformers/all-MiniLM-L6-v2'
        motor_busqueda = MotorBusqueda(model_name)
        self.assertIsInstance(motor_busqueda.model, SentenceTransformer)

    def test_compute_similarity(self):
        #Probaremos que la función compute_similarity lanza una excepción NotImplementedError.
        motor_busqueda = MotorBusqueda('sentence-transformers/all-MiniLM-L6-v2')
        example_embedding = [1.0, 2.0, 3.0]
        query_embedding = [4.0, 5.0, 6.0]
        with self.assertRaises(NotImplementedError):
            motor_busqueda.compute_similarity(example_embedding, query_embedding)

    def test_search(self):
        #Probar que la función search lanza una excepción NotImplementedError.
        motor_busqueda = MotorBusqueda('sentence-transformers/all-MiniLM-L6-v2')
        with self.assertRaises(NotImplementedError):
            motor_busqueda.search('Consulta de prueba','consulta prueba 2')

class TestCosineSimilaritySearchEngine(unittest.TestCase):
    def test_init(self):
        model_name ='sentence-transformers/all-MiniLM-L6-v2'
        dataset_path = 'src/IMDBtop1000.csv'
        search_engine = CosineSimilaritySearchEngine(model_name, dataset_path)
        self.assertIsInstance(search_engine.model, SentenceTransformer)
        self.assertIsInstance(search_engine.dataset, pd.DataFrame)

    def test_compute_similarity(self):
        #Probaremos que la función compute_similarity devuelve una similitud de coseno entre dos embeddings.
        search_engine = CosineSimilaritySearchEngine('sentence-transformers/all-MiniLM-L6-v2', 'src/IMDBtop1000.csv')
        example_embedding = [1.0, 2.0, 3.0]
        query_embedding = [4.0, 5.0, 6.0]
        resultado = search_engine.compute_similarity(example_embedding, query_embedding)
        self.assertIsInstance(resultado, float)

    def test_search(self):
        #Probar que la función search devuelve un DataFrame con los resultados de la búsqueda.
        search_engine = CosineSimilaritySearchEngine('sentence-transformers/all-MiniLM-L6-v2', 'src/IMDBtop1000.csv')
        query_description = 'Consulta de prueba'
        resultado = search_engine.search(query_description)
        self.assertIsInstance(resultado, pd.DataFrame)

#se comenta esta prueba porque es robusta, ya que valida con la cantidad de registros de conjunto de datos y 
# por tal motivo se extiende la ejecucion de las pruebas
"""class TestInteractiveSearch(unittest.TestCase):


    #probaremos que la función debe ejecutar la búsqueda interactiva y mostrar los resultados.
    def test_interactive_search(self):
        search_engine = CosineSimilaritySearchEngine('sentence-transformers/all-MiniLM-L6-v2', 'IMDBtop1000.csv')
        # Simulamos la entrada del usuario
        with unittest.mock.patch('builtins.input', return_value='Consulta de prueba'):
            with unittest.mock.patch('builtins.print'):
                interactive_search(search_engine) """

if __name__ == '__main__':
    unittest.main()
