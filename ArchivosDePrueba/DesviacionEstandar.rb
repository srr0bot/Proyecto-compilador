def calcular_media(datos)
    suma = datos.reduce(0, :+)
    return suma / datos.length.to_f
  end
  
  def calcular_desviacion_estandar(datos)
    media = calcular_media(datos)
    suma_cuadrados_diferencia = datos.reduce(0) { |sum, x| sum + (x - media) ** 2 }
    varianza = suma_cuadrados_diferencia / datos.length.to_f
    return Math.sqrt(varianza)
  end
  
  # Ejemplo de uso
  conjunto_de_datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  desviacion_estandar = calcular_desviacion_estandar(conjunto_de_datos)
  
  puts "Conjunto de datos: #{conjunto_de_datos}"
  puts "Desviación estándar: #{desviacion_estandar}"
  