from ply import lex

class RubyAnalyzer:
    def __init__(self):
        # Crear el lexer
        self.lexer = lex.lex(module=self)

    # Lista de tokens
    tokens = (
        'IDENTIFIER',
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'NEWLINE',
        'HASHTAG',
        'QUOTE',
        'COLON',
        'COMMA',
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'EQUAL',
        'NOT_EQUAL',
        'LESS_THAN',
        'LESS_THAN_EQUAL',
        'GREATER_THAN',
        'GREATER_THAN_EQUAL',
        'DOUBLE_QUOTE',
        'SINGLE_QUOTE',
        'COMMENT',
        'PRINT',
        'FOR',
        'WHILE',
        'IF',
        'ELSE',
        'INPUT',
        'OUTPUT',
    )

    # Reglas de expresiones regulares para tokens
    t_EQUAL = r'=='
    t_NOT_EQUAL = r'!='
    t_LESS_THAN = r'<'
    t_LESS_THAN_EQUAL = r'<='
    t_GREATER_THAN = r'>'
    t_GREATER_THAN_EQUAL = r'>='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'

    # Nueva regla para reconocer '#'
    def t_HASHTAG(self, t):
        r'\#.*'
        t.value = t.value[1:]  # Eliminar el '#' del token
        return t

    # Nueva regla para reconocer '"'
    def t_DOUBLE_QUOTE(self, t):
        r'"'
        return t

    # Nueva regla para reconocer ':'
    def t_COLON(self, t):
        r':'
        return t

    # Nueva regla para reconocer ','
    def t_COMMA(self, t):
        r','
        return t

    # Ignorar espacios y tabulaciones
    t_ignore = ' \t'

    # Definir un token para identificadores (variables y métodos)
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    # Definir un token para números
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Definir un token para saltos de línea
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    # Nueva regla para reconocer comentarios
    def t_COMMENT(self, t):
        r'\#.*'
        t.value = t.value[1:]  # Eliminar el '#' del token
        return t

    # Nueva regla para reconocer impresiones por consola
    def t_PRINT(self, t):
        r'puts|print(?=\()'
        return t

    # Nueva regla para reconocer ciclos (for, while)
    def t_FOR(self, t):
        r'for'
        return t

    def t_WHILE(self, t):
        r'while'
        return t

    # Nueva regla para reconocer condicionales (if, else)
    def t_IF(self, t):
        r'if'
        return t

    def t_ELSE(self, t):
        r'else'
        return t

    # Nueva regla para reconocer entradas y salidas
    def t_INPUT(self, t):
        r'gets'
        return t

    def t_OUTPUT(self, t):
        r'puts|print(?=\()'
        return t

    # Manejar errores de tokens no reconocidos
    def t_error(self, t):
        print(f"Error: Caracter no reconocido '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)

    # Método para analizar un código de Ruby
    def analyze_code(self, ruby_code):
        # Configurar el lexer
        self.lexer.input(ruby_code)

        # Lista para almacenar los tokens reconocidos (sin duplicados)
        unique_tokens = set()

        # Obtener y almacenar los tokens únicos
        for token in self.lexer:
            unique_tokens.add((token.type, token.value))

        return list(unique_tokens)
