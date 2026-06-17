# “Ce programme est un analyseur lexical écrit en Python 
# avec PLY Il transforme une entrée en tokens comme les nombres,
#  identifiants, opérateurs et mots-clés.”

#On importe la bibliothèque PLY qui permet de créer un analyseur lexical.
import ply.lex as lex 
#On définit la liste des tokens que le lexer peut reconnaître.
tokens = (
    'NUMBER','IDENTIFIER',
    'PLUS','MINUS','MULTIPLY','DIVIDE',
    'LPAREN','RPAREN',
    'EQUAL','ASSIGN',
    'STRING','IF','WHILE','PRINT'
)

# -------- KEYWORDS + IDENTIFIER --------
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == "if":
        print("KEYWORD_IF")
    elif t.value == "while":
        print("KEYWORD_WHILE")
    elif t.value == "print":
        print("KEYWORD_PRINT")
    else:
        print(f"IDENTIFIER: {t.value}")
    return t

# -------- NUMBER --------
def t_NUMBER(t):
    r'\d+'
    print(f"NUMBER: {t.value}")
    return t

# -------- OPERATORS --------
def t_EQUAL(t):
    r'=='
    print("EQUAL")
    return t

def t_ASSIGN(t):
    r'='
    print("ASSIGN")
    return t

def t_PLUS(t):
    r'\+'
    print("PLUS")
    return t

def t_MINUS(t):
    r'-'
    print("MINUS")
    return t

def t_MULTIPLY(t):
    r'\*'
    print("MULTIPLY")
    return t

def t_DIVIDE(t):
    r'/'
    print("DIVIDE")
    return t

def t_LPAREN(t):
    r'\('
    print("LPAREN")
    return t

def t_RPAREN(t):
    r'\)'
    print("RPAREN")
    return t

# -------- STRING --------
def t_STRING(t):
    r'\"([^\"\n])*\"'
    print(f"STRING: {t.value}")
    return t

# -------- IGNORE --------
t_ignore = ' \t\n'

# -------- ERROR --------
def t_error(t):
    print("ERROR:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

print("=== LEXER START ===")

while True:
    try:
        data = input(">> ")
    except EOFError:
        break
    lexer.input(data)
    for tok in lexer:
        pass

print("=== LEXER END ===")