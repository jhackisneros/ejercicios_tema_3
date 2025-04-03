from torre_de_hanoi.class_torre_de_hanoi import PuzzlePiramide
from cifra_magica.matriz import CalculadoraDeterminante
from carrera_espacial.naves import NaveEspacial, GestorNaves
from grimorio_matematico.polinomio import PolinomioMagico


def resolver_torre_de_hanoi():
    """Resuelve el problema de la Torre de Hanoi."""
    piramide_egipcia = PuzzlePiramide(74)
    solucion = piramide_egipcia.resolver()
    return solucion


def resolver_cifra_magica():
    """Calcula la cifra mágica usando determinantes."""
    matriz_magica = [
        [2, 0, 1],
        [3, 4, 5],
        [1, 6, 7]
    ]
    calculadora = CalculadoraDeterminante(matriz_magica)
    resultado_recursivo = calculadora.metodo_recursivo()
    resultado_iterativo = calculadora.metodo_iterativo()
    return {
        "determinante_recursivo": resultado_recursivo,
        "determinante_iterativo": resultado_iterativo,
        "cifra_magica": resultado_recursivo
    }


def analizar_naves():
    """Analiza las naves espaciales."""
    naves = [
        NaveEspacial("Cometa Veloz", 120, 5, 15),
        NaveEspacial("Titán del Cosmos", 300, 20, 50),
        NaveEspacial("GX-2000", 80, 3, 8),
        NaveEspacial("GX-Quantum", 150, 8, 25),
        NaveEspacial("Estrella Fugaz", 90, 4, 10),
        NaveEspacial("Neptuno Viajero", 200, 12, 30)
    ]
    gestor = GestorNaves(naves)
    return {
        "ordenadas": gestor.ordenar_naves(),
        "naves_especificas": gestor.buscar_por_nombre("Cometa Veloz", "Titán del Cosmos"),
        "top_pasajeros": gestor.top_pasajeros(),
        "max_tripulacion": gestor.max_tripulacion(),
        "prefijo_gx": gestor.filtrar_prefijo("GX"),
        "pasajeros_6+": gestor.filtrar_pasajeros(),
        "extremos": gestor.extremos_longitud()
    }


def ejemplo_polinomios():
    """Ejemplo de operaciones con polinomios mágicos."""
    p1 = PolinomioMagico([(3, 2), (-1, 1), (5, 0)])  # 3x² - x + 5
    p2 = PolinomioMagico([(2, 2), (4, 1)])           # 2x² + 4x
    resta = p1.restar(p2)
    p3 = PolinomioMagico([(1, 3), (6, 2), (11, 1), (6, 0)])  # x³ + 6x² + 11x + 6
    p4 = PolinomioMagico([(1, 1), (1, 0)])                   # x + 1
    cociente, resto = p3.dividir(p4)
    return {
        "resta": resta,
        "cociente": cociente,
        "resto": resto,
        "p1_sin_x2": p1,
        "p3_contiene_x3": p3.contiene_termino(3)
    }


def main():
    """Función principal para ejecutar el programa."""
    print("=== Torre de Hanoi ===")
    movimientos = resolver_torre_de_hanoi()
    print("Primeros 5 movimientos:", movimientos[:5])
    print(f"Total de movimientos: {len(movimientos)}\n")

    print("=== Cifra Mágica ===")
    secretos = resolver_cifra_magica()
    print("Determinante recursivo:", secretos["determinante_recursivo"])
    print("Determinante iterativo:", secretos["determinante_iterativo"])
    print("Cifra mágica:", secretos["cifra_magica"], "\n")

    print("=== Análisis de Naves ===")
    naves = analizar_naves()
    print("Naves ordenadas:", naves["ordenadas"])
    print("Naves específicas:", naves["naves_especificas"])
    print("Top 5 naves por pasajeros:", naves["top_pasajeros"])
    print("Nave con mayor tripulación:", naves["max_tripulacion"])
    print("Naves con prefijo GX:", naves["prefijo_gx"])
    print("Naves con 6+ pasajeros:", naves["pasajeros_6+"])
    print("Extremos de longitud:", naves["extremos"], "\n")

    print("=== Polinomios Mágicos ===")
    polinomios = ejemplo_polinomios()
    print("Resta de polinomios:", polinomios["resta"])
    print("Cociente:", polinomios["cociente"])
    print("Resto:", polinomios["resto"])
    print("Polinomio p1 sin x²:", polinomios["p1_sin_x2"])
    print("¿p3 contiene x³?:", polinomios["p3_contiene_x3"])


if __name__ == "__main__":
    main()