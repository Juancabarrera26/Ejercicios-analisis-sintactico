# Ejercicio 1: Analizador Sintactico en Python

En este ejercicio se implementó un analizador sintáctico descendente recursivo en Python, capaz de procesar expresiones aritmeticas simples y generar su correspondiente arbol sintáctico, parse tree.

La implementacion se basa en la gramática proporcionada en las diapositivas del curso.

---

## Gramatica utilizada

La gramatica definida para el analisis es:

```
E → E + T | T
T → T * F | F
F → id | num | ( E )
```

### Significado:

- **E (Expresión)**: combinación de términos mediante suma.
- **T (Término)**: combinación de factores mediante multiplicación.
- **F (Factor)**:
  - identificadores (`id`)
  - números (`num`)
  - expresiones entre paréntesis

---

## Implementacion

Se desarrolla un parser en Python utilizando el enfoque de descenso recursivo, donde cada regla de la gramatica se representa como una funcion:

- `E()` → maneja sumas
- `T()` → maneja multiplicaciones
- `F()` → maneja numeros, identificadores y paréntesis

Ademas, se implemento una clase `Nodo` para construir el arbol sintactico.

---

## Arbol Sintactico

El arbol sintactico representa la estructura jerarquica de la expresion analizada.

Ejemplo:

Entrada:

```
2 + 3 * 4
```
Salida del arbol:

```
E
2
+
  T
  3
  *
  4
```
Esto refleja correctamente la precedencia de operadores (* antes que +).

---

## Caracteristicas del Analizador

- Manejo de operadores:
  - Suma (`+`)
  - Multiplicacion (`*`)
- Soporte para:
  - Numeros (`num`)
  - Identificadores (`id`)
  - Parentesis `( )`
- Validacion sintactica de la entrada
- Generacion de arbol sintactico
- Deteccion de errores (tokens inesperados o incompletos)

---

## Ejemplos de prueba

```python
analizar("2 + 3 * 4")
analizar("a + b * c")
analizar("2 + 3 * ( 4 + 5 )")
```

## Limitaciones

- No se incluye el operador de resta (-) en la gramatica.
- La entrada debe estar separada por espacios (ej: 2 + 3, no 2+3).
- No se realiza analisis lexico avanzado, con tokenizacion simple.

## Conclusion

Se logro implementar un analizador sintactico funcional basado en una gramática formal, capaz de validar expresiones y representar su estructura mediante arboles sintácticos, aplicando correctamente la precedencia de operadores.
