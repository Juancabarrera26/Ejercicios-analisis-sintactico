import re


class Nodo:
    def __init__(self, valor, hijos=None):
        self.valor = valor
        self.hijos = hijos if hijos else []

    def imprimir(self, nivel=0):
        print("  " * nivel + str(self.valor))
        for h in self.hijos:
            h.imprimir(nivel + 1)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self, esperado):
        if self.actual() != esperado:
            raise SyntaxError(f"se esperaba '{esperado}' pero llegó '{self.actual()}'")
        self.pos += 1

    def es_num(self, t):
        return t is not None and t.isdigit()

    def es_id(self, t):
        return t is not None and re.match(r'^[a-zA-Z]+$', t)

    # E → T { + T }
    def E(self):
        nodo = self.T()
        while self.actual() == '+':
            self.consumir('+')
            nodo = Nodo('E', [nodo, Nodo('+'), self.T()])
        return nodo

    # T → F { * F }
    def T(self):
        nodo = self.F()
        while self.actual() == '*':
            self.consumir('*')
            nodo = Nodo('T', [nodo, Nodo('*'), self.F()])
        return nodo

    # F → id | num | ( E )
    def F(self):
        tok = self.actual()

        if tok == '(':
            self.consumir('(')
            nodo = self.E()
            self.consumir(')')
            return nodo

        if self.es_num(tok) or self.es_id(tok):
            self.consumir(tok)
            return Nodo(tok)

        raise SyntaxError(f"token inesperado '{tok}'")


def analizar(cadena):
    tokens = cadena.split()
    parser = Parser(tokens)

    print(f"\nEntrada: {cadena}")

    try:
        arbol = parser.E()

        if parser.actual() is not None:
            raise SyntaxError("sobran tokens")

        print("Cadena ACEPTADA")
        print("Arbol sintactico:")
        arbol.imprimir()

    except SyntaxError as e:
        print("Cadena RECHAZADA:", e)


# Pruebas 
analizar("2 + 3 * 4")
analizar("2 + 3 * ( 4 - 5 )") 
analizar("a + b * c")