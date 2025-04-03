from torre_de_hanoi.class_torre_de_hanoi import PuzzlePiramide
from cifra_magica import matriz
from carrera_espacial.naves import NaveEspacial, GestorNaves


def resolver_torre_de_hanoi():
    # Crear instancia con 74 piedras
    piramide_egipcia = PuzzlePiramide(74)
    
    # Resolver el puzzle
    solucion = piramide_egipcia.resolver()
    
    # Mostrar los primeros 5 movimientos como ejemplo
    print("Primeros 5 movimientos:")
    for movimiento in solucion[:5]:
        print(movimiento)
    
    print(f"\nTotal de movimientos requeridos: {len(solucion)}")


def resolver_cifra_magica():
    # Matriz del libro antiguo (3x3)
    matriz_magica = [
        [2, 0, 1],
        [3, 4, 5],
        [1, 6, 7]
    ]
    
    # Crear calculadora
    calculadora = CalculadoraDeterminante(matriz_magica)
    
    # Calcular determinantes
    resultado_recursivo = calculadora.metodo_recursivo()
    resultado_iterativo = calculadora.metodo_iterativo()
    
    # Revelar el secreto
    secretos = {
        "determinante_recursivo": resultado_recursivo,
        "determinante_iterativo": resultado_iterativo,
        "cifra_magica": resultado_recursivo  # Ambos métodos deben coincidir
    }
    
    print("Secretos revelados del libro antiguo:")
    print(f"• Determinante recursivo: {secretos['determinante_recursivo']}")
    print(f"• Determinante iterativo: {secretos['determinante_iterativo']}")
    print(f"¡La cifra mágica es: {secretos['cifra_magica']}!")


def cargar_datos_naves():
    return [
        NaveEspacial("Cometa Veloz", 120, 5, 15),
        NaveEspacial("Titán del Cosmos", 300, 20, 50),
        NaveEspacial("GX-2000", 80, 3, 8),
        NaveEspacial("GX-Quantum", 150, 8, 25),
        NaveEspacial("Estrella Fugaz", 90, 4, 10),
        NaveEspacial("Neptuno Viajero", 200, 12, 30)
    ]


def analizar_naves():
    # Configuración inicial
    naves = cargar_datos_naves()
    gestor = GestorNaves(naves)
    
    # Ejecutar todos los análisis
    resultados = {
        "ordenadas": gestor.ordenar_naves(),
        "naves_especificas": gestor.buscar_por_nombre(
            "Cometa Veloz", "Titán del Cosmos"),
        "top_pasajeros": gestor.top_pasajeros(),
        "max_tripulacion": gestor.max_tripulacion(),
        "prefijo_gx": gestor.filtrar_prefijo("GX"),
        "pasajeros_6+": gestor.filtrar_pasajeros(),
        "extremos": gestor.extremos_longitud()
    }
    
    return resultados

if __name__ == "__main__":
    datos = main()
    
    print("=== Naves ordenadas ===")
    for nave in datos["ordenadas"]:
        print(nave)
    
    print("\n=== Naves específicas ===")
    for nave in datos["naves_especificas"]:
        print(nave)
    
    print("\n=== Top 5 naves por pasajeros ===")
    for nave in datos["top_pasajeros"]:
        print(nave)
    
    print("\n=== Nave con mayor tripulación ===")
    print(datos["max_tripulacion"])
    
    print("\n=== Naves con prefijo GX ===")
    for nave in datos["prefijo_gx"]:
        print(nave)
    
    print("\n=== Naves con 6+ pasajeros ===")
    for nave in datos["pasajeros_6+"]:
        print(nave)
    
    print("\n=== Extremos de longitud ===")
    print("Más pequeña:", datos["extremos"][0])
    print("Más grande:", datos["extremos"][1])