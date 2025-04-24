from src.procesador import Analizador

def main():
    archivo = "data/sri_ventas_2024.csv"
    analizador = Analizador(archivo)
    
    # Mostrar ventas totales por provincia
    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"\t{prov}: ${total:.2f}")
    
    # Obtener ventas de una provincia específica
    print("\nCompras para una provincia")
    provincia = input("\tIngrese el nombre de una provincia: ")
    try:
        ventas = analizador.ventas_por_provincia(provincia)
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()

