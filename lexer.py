import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'ASIGN',
    'ARGUMENT',
    'VARIABLE',
    'METHOD',
    'RPAREN',
    'NEWLINE',
)

# Expresiones regulares para tokens simples
t_ASIGN = r'='
t_RPAREN = r'\)'
t_NEWLINE = r'\n'

# Expresiones regulares con acciones para tokens más complejos
def t_METHOD(t):
    r'rand\(|mean\(|mode\(|var\(|std\(|median\('
    return t

def t_VARIABLE(t):
    r'\b(?![a-z]+\()[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_ARGUMENT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores de token
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    data = """
    x = rand(3)
    y = mean(x)
    z = 10
    && dasd efe
    """

    lexer.input(data)
    for token in lexer:
        print(token)