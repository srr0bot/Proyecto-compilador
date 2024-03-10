import re

cadena = "A = rand(3)"

expresion_regular = r'[a-zA-Z]+\s*=\s*[a-z]+\(\d+\)'

if re.match(expresion_regular, cadena):
    print("La cadena coincide con la expresión regular")
else:
    print("La cadena no coincide con la expresión regular")
