# Comparacion entre CYK (O(n^3)) y parser lineal (O(n))

import time
import re

# GRAMATICA PARA CYK 
# S -> id | S P S
# P -> + | *

gramatica = {
    'S': [['id'], ['S', 'P', 'S']],
    'P': [['+'], ['*']]
}
def es_id(t):
    return re.match(r'^[a-zA-Z0-9]+$', t) is not None

def convertir_token(t):
    if t in ('+', '*'):
        return t
    if es_id(t):
        return 'id'
    return t

# ALGORITMO CYK

def cyk(cadena):
    n = len(cadena)

    if n == 0:
        return False, 0

    tabla = [[set() for _ in range(n)] for _ in range(n)]
    operaciones = 0

    # llenar diagonal
    for i in range(n):
        simbolo = convertir_token(cadena[i])

        for A in gramatica:
            for prod in gramatica[A]:
                operaciones += 1
                if prod == [simbolo]:
                    tabla[i][i].add(A)

    # combinar subcadenas
    for l in range(2, n + 1):  # longitud
        for i in range(n - l + 1):
            j = i + l - 1

            for k in range(i, j):
                for A in gramatica:
                    for prod in gramatica[A]:
                        operaciones += 1

                        if len(prod) == 2:
                            if (prod[0] in tabla[i][k] and
                                prod[1] in tabla[k + 1][j]):
                                tabla[i][j].add(A)

    aceptada = 'S' in tabla[0][n - 1]
    return aceptada, operaciones


# PARSER LINEAL (simple)
# acepta: id op id op id 

def parser_lineal(cadena):
    operaciones = 0
    i = 0
    n = len(cadena)

    try:
        # debe empezar con id
        if not es_id(cadena[i]):
            return False, operaciones
        i += 1
        operaciones += 1

        # patron: operador + id
        while i < n:
            if cadena[i] not in ('+', '*'):
                return False, operaciones
            i += 1
            operaciones += 1

            if i >= n or not es_id(cadena[i]):
                return False, operaciones
            i += 1
            operaciones += 1

        return True, operaciones

    except:
        return False, operaciones

# COMPARACION
def comparar(cadena):
    print("\n" + "=" * 50)
    print("Cadena:", cadena)
    print("Numero de tokens:", len(cadena))
    print("=" * 50)

    # CYK
    inicio = time.time()
    ok_cyk, ops_cyk = cyk(cadena)
    tiempo_cyk = (time.time() - inicio) * 1000

    # Lineal
    inicio = time.time()
    ok_lin, ops_lin = parser_lineal(cadena)
    tiempo_lin = (time.time() - inicio) * 1000

    print("\nCYK (O(n^3))")
    print("Aceptada:", ok_cyk)
    print("Operaciones:", ops_cyk)
    print("Tiempo:", f"{tiempo_cyk:.4f} ms")

    print("\nParser Lineal (O(n))")
    print("Aceptada:", ok_lin)
    print("Operaciones:", ops_lin)
    print("Tiempo:", f"{tiempo_lin:.4f} ms")

    if ops_lin > 0:
        print("\nCYK hizo", ops_cyk // ops_lin, "veces mas operaciones")

# PRUEBAS

comparar(['a', '+', 'b'])
comparar(['a', '+', 'b', '*', 'c'])
comparar(['a', '+', 'b', '+', 'c', '+', 'd'])
comparar(['a', '*', 'b', '+', 'c', '*', 'd', '+', 'e'])