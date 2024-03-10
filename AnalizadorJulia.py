from ply import lex

class AnalizadorJulia:

    def __init__(self):
        self.lexer = lex.lex(module=self)
        
    tokens = ('ARGUMENT', 'VARIABLE', 'ASIGN', 'METHOD', 'RPAREN', 'NEWLINE')
    
    t_ASIGN = r'='
    t_ARGUMENT = r'\d+'
    t_VARIABLE = r'\b(?![a-z]+\()[a-zA-Z_][a-zA-Z_0-9]*$'
    t_METHOD = r'rand\(|mean\(|mode\(|var\(|std\(|median\('
    t_ignore = ' \t'
    t_RPAREN = r'\)$'
    t_NEWLINE =r'\n'
    
    def t_error(self, t):
        print(f"Error: Caracter no reconocido '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)
    
    def analyze_code(self, julia_code):
        self.lexer.input(julia_code)
        unique_tokens = set()

        for token in self.lexer:
            unique_tokens.add((token.type, token.value))

        return list(unique_tokens)