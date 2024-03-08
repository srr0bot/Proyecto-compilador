function calcular_estadisticas(datos)
    n = length(datos)
    
    suma = sum(datos)
    media = suma / n
    
    datos_ordenados = sort(datos)
    if n % 2 == 0
        indice_medio1 = n ÷ 2
        indice_medio2 = indice_medio1 + 1
        mediana = (datos_ordenados[indice_medio1] + datos_ordenados[indice_medio2]) / 2.0
    else
        indice_medio = (n + 1) ÷ 2
        mediana = datos_ordenados[indice_medio]
    end
    
    suma_cuadrados_diff = sum((dato - media)^2 for dato in datos)
    desviacion_estandar = sqrt(suma_cuadrados_diff / n)
    
    println("Media: ", media)
    println("Mediana: ", mediana)
    println("Desviación estándar: ", desviacion_estandar)
end

datos = [12.3, 45.6, 78.9, 23.4, 56.7, 89.0, 34.5, 67.8, 90.1, 43.2, 76.5, 98.7, 54.3, 87.6, 21.0, 65.4, 32.1, 43.8, 76.9, 98.2]

calcular_estadisticas(datos)