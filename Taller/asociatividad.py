# Analisis de asociatividad y precedencia

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
            raise SyntaxError(f"se esperaba '{esperado}' pero llego '{self.actual()}'")
        self.pos += 1

    def es_id(self, t):
        return t is not None and re.match(r'^[a-zA-Z0-9]+$', t)

    def atomico(self):
        tok = self.actual()
        if not self.es_id(tok):
            raise SyntaxError(f"se esperaba identificador pero llego '{tok}'")
        self.consumir(tok)
        return Nodo(tok)

# VERSION 1: Asociatividad izquierda
# a + b + c = (a + b) + c
    def E_izquierda(self):
        nodo = self.atomico()

        while self.actual() in ('+', '*'):
            op = self.actual()
            self.consumir(op)
            nodo = Nodo('E', [nodo, Nodo(op), self.atomico()])

        return nodo

# VERSION 2: Asociatividad derecha
# a + b + c = a + (b + c)
    def E_derecha(self):
        nodo = self.atomico()

        if self.actual() in ('+', '*'):
            op = self.actual()
            self.consumir(op)
            nodo = Nodo('E', [nodo, Nodo(op), self.E_derecha()])

        return nodo

# VERSION 3: Precedencia normal
# * tiene mayor prioridad que +
    def E_prec_normal(self):
        nodo = self.T_prec_normal()

        while self.actual() == '+':
            self.consumir('+')
            nodo = Nodo('E', [nodo, Nodo('+'), self.T_prec_normal()])

        return nodo

    def T_prec_normal(self):
        nodo = self.atomico()

        while self.actual() == '*':
            self.consumir('*')
            nodo = Nodo('T', [nodo, Nodo('*'), self.atomico()])

        return nodo

# VERSION 4: Precedencia invertida
# + tiene mayor prioridad que *
    def E_prec_inversa(self):
        nodo = self.T_prec_inversa()

        while self.actual() == '*':
            self.consumir('*')
            nodo = Nodo('E', [nodo, Nodo('*'), self.T_prec_inversa()])

        return nodo

    def T_prec_inversa(self):
        nodo = self.atomico()

        while self.actual() == '+':
            self.consumir('+')
            nodo = Nodo('T', [nodo, Nodo('+'), self.atomico()])

        return nodo

# PRUEBAS
def probar(cadena):
    print("\n" + "=" * 50)
    print("Cadena:", cadena)
    print("=" * 50)

    versiones = [
        ("Asociatividad izquierda", "E_izquierda"),
        ("Asociatividad derecha", "E_derecha"),
        ("Precedencia normal", "E_prec_normal"),
        ("Precedencia inversa", "E_prec_inversa"),
    ]

    for nombre, metodo in versiones:
        parser = Parser(cadena.split())

        print("\n[" + nombre + "]")

        try:
            funcion = getattr(parser, metodo)
            arbol = funcion()

            if parser.actual() is not None:
                raise SyntaxError("sobran tokens")

            arbol.imprimir()

        except SyntaxError as e:
            print("Error:", e)

# EJECUCION

probar("a + b * c")
probar("a + b + c")