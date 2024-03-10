from ply import lex

class analizadorRuby:

    def __init__(self):
        self.lexer = lex.lex(module=self)
        
    tokens = ('ARGUMENT', 'VARIABLE', 'ASIGN', 'METHOD', 'RPAREN', 'NEWLINE', 'LPAREN', 'RBRACKET', 'LBRACKET', 'POINT', 'INSTANCE', 'RANDOM')
    
    t_ASIGN = r'='
    t_ARGUMENT = r'\d+'
    t_VARIABLE = r'\b(?!Array)[a-zA-Z_][a-zA-Z_0-9]*'
    t_METHOD = r'\.mean|\.mode|\.var|\.std|\.median| \.new'
    t_ignore = ' \t'
    t_RPAREN = r'\)'
    t_LPAREN = r'\('
    t_NEWLINE =r'\n'
    t_POINT = r'\.'
    t_RBRACKET = r'}'
    t_LBRACKET = r'{'
    t_INSTANCE = r'Array'
    t_RANDOM = r'\{\s*rand\s*\}'
    
    def t_error(self, t):
        print(f"Error: Caracter no reconocido '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)
    
    def analyze_code(self, julia_code):
        self.lexer.input(julia_code)
        unique_tokens = set()

        for token in self.lexer:
            unique_tokens.add((token.type, token.value))

        return list(unique_tokens)