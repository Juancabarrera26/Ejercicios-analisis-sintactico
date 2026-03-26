# Analizador sintactico descendente recursivo
# Gramatica:
#   E -> E + T | T
#   T -> T * F | F
#   F -> ( E ) | id | num

tokens = []
pos = 0

def token_actual():
    if pos < len(tokens):
        return tokens[pos]
    return None

def consumir(esperado):
    global pos
    if token_actual() != esperado:
        raise SyntaxError(f"se esperaba '{esperado}' pero llego '{token_actual()}'")
    pos += 1

def es_operando(t):
    if t is None:
        return False
    if t in ('+', '*', '(', ')'):
        return False
    return True

def E():
    nodo = T()
    while token_actual() == '+':
        consumir('+')
        derecha = T()
        nodo = ('E', nodo, '+', derecha)
    return nodo

def T():
    nodo = F()
    while token_actual() == '*':
        consumir('*')
        derecha = F()
        nodo = ('T', nodo, '*', derecha)
    return nodo

def F():
    tok = token_actual()
    if tok == '(':
        consumir('(')
        nodo = E()
        consumir(')')
        return nodo
    if es_operando(tok):
        consumir(tok)
        return (tok,)
    raise SyntaxError(f"token inesperado '{tok}'")

def imprimir_arbol(nodo, nivel=0):
    sangria = "  " * nivel
    if isinstance(nodo, tuple):
        print(sangria + str(nodo[0]))
        for hijo in nodo[1:]:
            if isinstance(hijo, str):
                print(sangria + "  " + hijo)
            else:
                imprimir_arbol(hijo, nivel + 1)
    else:
        print(sangria + str(nodo))

def analizar(cadena):
    global tokens, pos
    tokens = cadena.split()
    pos = 0
    print(f"\nEntrada: '{cadena}'")
    try:
        resultado = E()
        if token_actual() is not None:
            raise SyntaxError(f"token inesperado '{token_actual()}'")
        print("Cadena ACEPTADA")
        print("Arbol sintatico:")
        imprimir_arbol(resultado)
    except SyntaxError as e:
        print(f"Cadena RECHAZADA: {e}")

# Pruebas
analizar("2 + 3 * 4")
analizar("a + b * c")
analizar("2 * ( 3 + 4 )")
analizar("a + * b")       
