import re

cadena = "rand(A)"

expresion_regular = r'\b([a-z]+)\(([a-zA-Z]+)\)$'

if re.match(expresion_regular, cadena):
    print("La cadena coincide con la expresión regular")
else:
    print("La cadena no coincide con la expresión regular")
