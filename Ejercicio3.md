# Ejercicio 3: Asociatividad y precedencia de operadores

En este ejercicio se realiza un analisis sobre la asociatividad y la precedencia de operadores en expresiones aritmeticas, modificando la gramatica para observar como cambia la interpretacion de una misma cadena.

Se implementan cuatro versiones de la gramatica:

- Asociatividad izquierda
- Asociatividad derecha
- Precedencia normal (multiplicacion antes que suma)
- Precedencia inversa (suma antes que multiplicacion)

El objetivo es demostrar que la gramatica define la estructura del arbol sintactico y, por lo tanto, el significado de la expresion.

---

## Conceptos clave

### Asociatividad

La asociatividad define como se agrupan los operadores del mismo tipo.

Ejemplo:

- Asociatividad izquierda:

```
a + b + c = (a + b) + c
```

- Asociatividad derecha:
```
a + b + c = a + (b + c)
```

---

### Precedencia

La precedencia define que operador se evalua primero cuando hay diferentes operadores en la expresion.

Ejemplo:

- Precedencia normal:
```
a + b * c = a + (b * c)
```

- Precedencia inversa:
```
a + b * c = (a + b) * c
```


---

## Implementacion

Se desarrollo un analizador sintactico en Python que permite cambiar la forma de analizar la expresion segun la version de la gramatica.

Cada version se implementa como una funcion diferente dentro del parser:

- E_izquierda
- E_derecha
- E_prec_normal
- E_prec_inversa

El programa recibe una cadena, la analiza con cada version y muestra el arbol sintactico resultante.

---

## Pruebas realizadas

Se utilizaron dos cadenas de prueba:

```python
probar("a + b * c")
probar("a + b + c")
```

## Resultados

```
==================================================
Cadena: a + b * c
==================================================

[Asociatividad izquierda]
E
  E
    a
    +
    b
  *
  c

[Asociatividad derecha]
E
  a
  +
  E
    b
    *
    c

[Precedencia normal]
E
  a
  +
  T
    b
    *
    c

[Precedencia inversa]
E
  T
    a
    +
    b
  *
  c

==================================================
Cadena: a + b + c
==================================================

[Asociatividad izquierda]
E
  E
    a
    +
    b
  +
  c

[Asociatividad derecha]
E
  a
  +
  E
    b
    +
    c

[Precedencia normal]
E
  E
    a
    +
    b
  +
  c

[Precedencia inversa]
T
  T
    a
    +
    b
  +
  c
```


---

## Analisis

Los resultados muestran que:

- La asociatividad cambia la forma en que se agrupan los operadores iguales
- La precedencia cambia el orden en que se evaluan diferentes operadores
- Una misma cadena puede generar diferentes arboles sintacticos dependiendo de la gramatica

Esto demuestra que el significado de una expresion no depende solo de los tokens, sino de las reglas de la gramatica utilizada.

---

## Conclusiones

- La gramatica es fundamental en la interpretacion de expresiones
- Cambiar la asociatividad modifica la estructura del arbol sintactico
- Cambiar la precedencia altera el orden de evaluacion de los operadores
- Diferentes gramaticas pueden producir interpretaciones distintas para la misma cadena
