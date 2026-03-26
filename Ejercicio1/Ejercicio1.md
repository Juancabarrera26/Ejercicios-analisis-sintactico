# Analizador sintactico descendente recursivo

En este ejercicio se implementa un analizador sintactico descendente recursivo en Python para procesar expresiones aritmeticas simples.

El programa recibe una cadena de entrada, valida su estructura segun una gramatica definida y genera un arbol sintactico que representa la forma en que se interpreta la expresion.

---

## Gramatica utilizada

La gramatica implementada es:
```
E -> E + T | T
T -> T * F | F
F -> ( E ) | operando
```

Donde:

- E representa una expresion
- T representa un termino
- F representa un factor
- operando puede ser un identificador o un numero

---

## Funcionamiento

El analizador esta basado en el enfoque de descenso recursivo, donde cada regla de la gramatica se implementa como una funcion:

- E(): maneja operaciones de suma
- T(): maneja operaciones de multiplicacion
- F(): maneja operandos y parentesis

El analisis se realiza de izquierda a derecha, consumiendo tokens a medida que se validan.

---

## Arbol sintactico

El arbol sintactico se representa mediante tuplas anidadas, donde:

- El primer elemento indica el tipo de nodo (E, T o el operando)
- Los demas elementos representan sus hijos

Ejemplo:

Entrada:
```
2 + 3 * 4
```

Salida:
```
E
2
+
 T
 3 
 *
 4
```

Esto refleja correctamente la precedencia de operadores, donde la multiplicacion se evalua antes que la suma.

---

## Caracteristicas

- Soporte para operadores:
  - Suma (+)
  - Multiplicacion (*)
- Manejo de parentesis
- Soporte para operandos (numeros o identificadores)
- Validacion sintactica de la entrada
- Generacion de arbol sintactico
- Deteccion de errores en la expresion

---

## Ejemplos de prueba

```python
analizar("2 + 3 * 4")
analizar("a + b * c")
analizar("2 * ( 3 + 4 )")
analizar("a + * b")
```

## Resultados esperados

- Expresiones validas son aceptadas y generan un arbol sintactico
- Expresiones invalidas producen un error indicando el problema

---

## Limitaciones

- La entrada debe estar separada por espacios
- No se incluyen otros operadores como resta o division
- No se realiza analisis lexico avanzado

---

## Posibles mejoras

- Agregar soporte para mas operadores
- Permitir expresiones sin espacios
- Implementar un analizador lexico
- Representar el arbol de forma grafica
