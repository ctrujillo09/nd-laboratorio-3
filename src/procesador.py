import csv

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = self.leer_csv()

    def leer_csv(self):
        """
        Lee el archivo CSV y devuelve los datos en una lista de diccionarios.
        Cada diccionario representa una fila del archivo.
        """
        datos = []
        # Intentamos abrir el archivo con una codificación más flexible (ISO-8859-1)
        with open(self.archivo_csv, mode='r', encoding='ISO-8859-1') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        """
        Retorna un diccionario con el total de ventas agrupado por PROVINCIA.
        """
        ventas_por_provincia = {}
        
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            ventas = float(fila['TOTAL_VENTAS'])
            
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += ventas
            else:
                ventas_por_provincia[provincia] = ventas
        
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre):
        """
        Retorna el total de ventas de una provincia determinada.
        """
        ventas_totales = 0
        for fila in self.datos:
            if fila['PROVINCIA'] == nombre:
                ventas_totales += float(fila['TOTAL_VENTAS'])
        
        return ventas_totales

