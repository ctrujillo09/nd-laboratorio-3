import csv

class ProvinciaNoEncontrada(Exception):
    """Excepción personalizada cuando no se encuentra la provincia solicitada."""
    def __init__(self, provincia):
        self.provincia = provincia
        self.mensaje = f"Provincia '{provincia}' no encontrada en los datos."
        super().__init__(self.mensaje)

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
                # Ignoramos las filas donde la provincia es "ND"
                if fila['PROVINCIA'] != "ND":
                    datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        """
        Retorna un diccionario con el total de ventas agrupado por PROVINCIA,
        ignorando aquellas filas donde la provincia es "ND".
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
        """Retorna el total de ventas de una provincia determinada"""
        ventas_por_provincia = self.ventas_totales_por_provincia()
        nombre_normalizado = nombre.strip().upper()  # Convertir nombre a mayusculas

        if nombre_normalizado not in ventas_por_provincia:
            raise KeyError(f"La provincia '{nombre}' no se encuentra en los datos.")
        return ventas_por_provincia[nombre_normalizado]
