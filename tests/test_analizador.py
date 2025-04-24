import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")
    
    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict) 

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        #El archivo contiene registros "ND" en provincias
        self.assertEqual(total_provincias, 24)
    
    def test_ventas_totales_mayores_5K(self):
        resumen = self.analizador.ventas_totales_por_provincia() 
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")
        
    def test_ventas_por_provincia_mayusculas_minusculas(self):
            """Prueba que la búsqueda no sea sensible a mayúsculas o minúsculas"""
            # Asegurarse de que "quito" y "QUITO" devuelvan el mismo resultado
            resultado_mayusculas = self.analizador.ventas_por_provincia("PICHINCHA")
            resultado_minusculas = self.analizador.ventas_por_provincia("pichincha")
            self.assertEqual(resultado_mayusculas, resultado_minusculas)
    
    #def test_ventas_por_provincia_3(self):
    
         