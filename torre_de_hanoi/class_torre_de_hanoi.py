class PuzzlePiramide:
    def __init__(self, num_piedras=74):
        self.num_piedras = num_piedras
        self.movimientos = []

    def resolver(self, origen='Columna A', destino='Columna B', auxiliar='Columna C'):
        """Inicia la solución del puzzle"""
        self._mover_piedras(self.num_piedras, origen, destino, auxiliar)
        return self.movimientos

    def _mover_piedras(self, n, origen, destino, auxiliar):
        """Método recursivo interno"""
        if n == 1:
            self.movimientos.append(f"Mover piedra 1 de {origen} a {destino}")
            return
        self._mover_piedras(n - 1, origen, auxiliar, destino)
        self.movimientos.append(f"Mover piedra {n} de {origen} a {destino}")
        self._mover_piedras(n - 1, auxiliar, destino, origen)

if __name__ == "__main__":
    # Ejecución directa del módulo para pruebas
    puzzle = PuzzlePiramide(3)  # Ejemplo con 3 piedras
    movimientos = puzzle.resolver()
    for movimiento in movimientos:
        print(movimiento)