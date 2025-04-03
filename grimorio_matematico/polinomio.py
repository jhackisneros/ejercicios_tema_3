class PolinomioMagico:
    def __init__(self, terminos=None):
        self.terminos = {}
        if terminos:
            for coeficiente, exponente in terminos:
                self.agregar_termino(coeficiente, exponente)
    
    def agregar_termino(self, coeficiente, exponente):
        if exponente in self.terminos:
            self.terminos[exponente] += coeficiente
            if self.terminos[exponente] == 0:
                del self.terminos[exponente]
        else:
            self.terminos[exponente] = coeficiente
    
    def restar(self, otro_polinomio):
        resultado = PolinomioMagico()
        resultado.terminos = self.terminos.copy()
        for exp, coeff in otro_polinomio.terminos.items():
            resultado.agregar_termino(-coeff, exp)
        return resultado
    
    def dividir(self, divisor):
        dividendo = self
        cociente = PolinomioMagico()
        resto = PolinomioMagico([(coeff, exp) for exp, coeff in dividendo.terminos.items()])
        
        divisor_grado = max(divisor.terminos.keys(), default=-1)
        if divisor_grado == -1:
            raise ZeroDivisionError("¡No se puede dividir por el polinomio cero!")
        
        while max(resto.terminos.keys(), default=-1) >= divisor_grado:
            grado_actual = max(resto.terminos.keys())
            coeff_actual = resto.terminos[grado_actual]
            
            divisor_coeff_lider = divisor.terminos[divisor_grado]
            term_coeff = coeff_actual / divisor_coeff_lider
            term_grado = grado_actual - divisor_grado
            
            cociente.agregar_termino(term_coeff, term_grado)
            
            term_polinomio = PolinomioMagico([(term_coeff, term_grado)])
            polinomio_sustraer = divisor.multiplicar(term_polinomio)
            resto = resto.restar(polinomio_sustraer)
        
        return cociente, resto
    
    def multiplicar(self, otro_polinomio):
        resultado = PolinomioMagico()
        for exp1, coeff1 in self.terminos.items():
            for exp2, coeff2 in otro_polinomio.terminos.items():
                resultado.agregar_termino(coeff1 * coeff2, exp1 + exp2)
        return resultado
    
    def eliminar_termino(self, exponente):
        if exponente in self.terminos:
            del self.terminos[exponente]
    
    def contiene_termino(self, exponente):
        return exponente in self.terminos
    
    def __repr__(self):
        terminos_ordenados = sorted(self.terminos.items(), key=lambda x: -x[0])
        if not terminos_ordenados:
            return "0"
        return " + ".join(f"{coeff}x^{exp}" for exp, coeff in terminos_ordenados if coeff != 0)