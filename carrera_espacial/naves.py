class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros
    
    def __repr__(self):
        return (f"{self.nombre}: "
                f"Longitud: {self.longitud}m, "
                f"Tripulación: {self.tripulantes}, "
                f"Pasajeros: {self.pasajeros}")

class GestorNaves:
    def __init__(self, naves):
        self.naves = naves
    
    def ordenar_naves(self):
        """Ordena por nombre (A-Z) y longitud (descendente)"""
        return sorted(self.naves, 
                     key=lambda x: (x.nombre, -x.longitud))
    
    def buscar_por_nombre(self, *nombres):
        """Busca naves por nombre exacto"""
        return [n for n in self.naves if n.nombre in nombres]
    
    def top_pasajeros(self, cantidad=5):
        """Naves con más pasajeros"""
        return sorted(self.naves, 
                     key=lambda x: x.pasajeros, 
                     reverse=True)[:cantidad]
    
    def max_tripulacion(self):
        """Nave con mayor tripulación"""
        return max(self.naves, key=lambda x: x.tripulantes)
    
    def filtrar_prefijo(self, prefijo):
        """Naves que empiezan con un prefijo"""
        return [n for n in self.naves 
               if n.nombre.startswith(prefijo)]
    
    def filtrar_pasajeros(self, minimo=6):
        """Naves con capacidad mínima de pasajeros"""
        return [n for n in self.naves if n.pasajeros >= minimo]
    
    def extremos_longitud(self):
        """Nave más pequeña y más grande"""
        return (min(self.naves, key=lambda x: x.longitud),
                max(self.naves, key=lambda x: x.longitud))