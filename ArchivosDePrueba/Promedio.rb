def calcular_promedio(datos)
    suma = datos.reduce(0, :+)
    return suma / datos.length.to_f
  end
  
  # Ejemplo de uso
  conjunto_de_datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  promedio = calcular_promedio(conjunto_de_datos)
  
  puts "Conjunto de datos: #{conjunto_de_datos}"
  puts "Promedio: #{promedio}"
  