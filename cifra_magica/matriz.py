class CalculadoraDeterminante:
    def __init__(self, matriz):
        self.matriz = matriz
        self.tamano = len(matriz)
    
    def metodo_recursivo(self):
        """Calcula el determinante usando recursividad (para cualquier n x n)"""
        return self._determinante_recursivo(self.matriz)
    
    def metodo_iterativo(self):
        """Calcula el determinante usando método iterativo (solo 3x3)"""
        if self.tamano != 3:
            raise ValueError("Método iterativo solo válido para matrices 3x3")
        return self._determinante_iterativo()
    
    def _determinante_recursivo(self, matriz):
        """Método interno recursivo"""
        n = len(matriz)
        if n == 1:
            return matriz[0][0]
        
        det = 0
        for col in range(n):
            signo = (-1) ** col
            menor = [fila[:col] + fila[col+1:] for fila in matriz[1:]]
            det += matriz[0][col] * signo * self._determinante_recursivo(menor)
        return det
    
    def _determinante_iterativo(self):
        """Método interno iterativo (Regla de Sarrus optimizada)"""
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)