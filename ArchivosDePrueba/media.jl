function calcular_media(arreglo)
    if length(arreglo) != 15
        throw(ArgumentError("El arreglo debe contener exactamente 15 números"))
    end
    
    suma = sum(arreglo)
    media = suma / length(arreglo)
    
    return media
end

# Ejemplo de uso
arreglo_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
media_resultado = calcular_media(arreglo_numeros)

println("El resultado de la media es: $media_resultado")