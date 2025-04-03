from torre_de_hanoi.class_torre_de_hanoi import TorreDeHanoi

if __name__ == "__main__":
    hanoi = TorreDeHanoi(74)
    hanoi.mover_piedras(74, 'Columna A', 'Columna B', 'Columna C')
    hanoi.imprimir_resultados()

class TorreDeHanoi:
    def __init__(self, n):
        self.n = n
        self.movimientos = []

    def mover_piedras(self, n, origen, auxiliar, destino):
        stack = [(n, origen, auxiliar, destino)]
        while stack:
            n, origen, auxiliar, destino = stack.pop()
            if n == 1:
                self.movimientos.append((origen, destino))
            else:
                stack.append((n-1, auxiliar, origen, destino))
                stack.append((1, origen, auxiliar, destino))
                stack.append((n-1, origen, destino, auxiliar))

    def obtener_movimientos(self):
        return self.movimientos

    def obtener_numero_movimientos(self):
        return 2**self.n - 1

    def imprimir_resultados(self):
        print("Movimientos (primeros 10):", self.obtener_movimientos()[:10])
        print("Número total de movimientos necesarios:", self.obtener_numero_movimientos())

