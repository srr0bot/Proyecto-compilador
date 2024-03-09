import random


class Metodos:
    
    def crearArray (self, cantidad):
        
        array = [random.uniform(0, 1) for _ in range(cantidad)]
        print(array)
        return array
    
    def media (self, array):
        
        media = sum(array) / len(array)
        
        return media
    
    def calcular_moda (self, array):
        
        frecuencias = {}
        for dato in array:
            if dato in frecuencias:
                frecuencias[dato] += 1
            else:
                frecuencias[dato] = 1
        moda = max(frecuencias, key=frecuencias.get)
        return moda
    
    def calcular_varianza(self, array):
        media = sum(array) / len(array)
        varianza = sum((x - media) ** 2 for x in array) / len(array)
        return varianza

    def calcular_desviacion_estandar(self, array):
        varianza = self.calcular_varianza(array)
        desviacion_estandar = varianza ** 0.5
        return desviacion_estandar
    
    def calcular_mediana(self, array):
        array_ordenados = sorted(array)
        n = len(array_ordenados)
        if n % 2 == 0:
            mediana = (array_ordenados[n // 2 - 1] + array_ordenados[n // 2]) / 2
        else:
            mediana = array_ordenados[n // 2]
        return mediana