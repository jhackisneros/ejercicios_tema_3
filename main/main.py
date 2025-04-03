from torre_de_hanoi.class_torre_de_hanoi import PuzzlePiramide

if __name__ == "__main__":
    # Crear instancia con 74 piedras
    piramide_egipcia = PuzzlePiramide(74)
    
    # Resolver el puzzle
    solucion = piramide_egipcia.resolver()
    
    # Mostrar los primeros 5 movimientos como ejemplo
    print("Primeros 5 movimientos:")
    for movimiento in solucion[:5]:
        print(movimiento)
    
    print(f"\nTotal de movimientos requeridos: {len(solucion)}")