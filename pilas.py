import ply.yacc as yacc
from lexer import tokens  # Supongamos que tienes un archivo lexer.py donde tienes definidos los tokens

# Reglas de gramática
def p_statement_assign(p):
    'statement : ASIGN '
    p[0] = ('assign', p[2])

def p_expression_method(p):
    'expression : METHOD RPAREN'
    p[0] = ('method', p[1])

def p_expression_arg(p):
    'expression : ARGUMENT'
    p[0] = ('argument', p[1])

def p_expression_var(p):
    'expression : VARIABLE'
    p[0] = ('variable', p[1])

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Construir el parser
parser = yacc.yacc()

# Entrada de ejemplo
data = """
x = rand(3)
y = mean(x)
z = 10
"""

# Analizar la entrada
result = parser.parse(data)
print("Resultado del análisis:")
for item in result:
    print(item)
