# Ejercicio 2: Comparacion entre algoritmo CYK y parser lineal

En este ejercicio se realiza una comparacion entre dos metodos de analisis sintactico:

- Algoritmo CYK con complejidad O(n^3)
- Parser lineal con complejidad O(n)

El objetivo es evidenciar la diferencia de rendimiento entre ambos enfoques, tanto en numero de operaciones como en tiempo de ejecucion.

---

## Algoritmo CYK

El algoritmo CYK (Cocke-Younger-Kasami) es un metodo de analisis sintactico basado en programacion dinamica que trabaja con gramaticas en Forma Normal de Chomsky.

En esta implementacion se utiliza la siguiente gramatica simplificada:

```
S -> id
S -> S P S
P -> + | *
```

El algoritmo construye una tabla donde cada celda representa una subcadena de la entrada. A partir de las combinaciones de subcadenas, se determina si la cadena completa puede generarse desde el simbolo inicial.

### Caracteristicas

- Analiza todas las posibles subcadenas
- Utiliza una estructura de tabla bidimensional
- Complejidad cubica O(n^3)
- Metodo general para gramaticas libres de contexto

---

## Parser lineal

El parser lineal es una implementacion sencilla que valida expresiones siguiendo un patron basico:

```
id op id op id 
```


Donde:
- id representa un identificador
- op puede ser + o *

Este parser recorre la cadena una sola vez, validando la estructura sin construir un arbol sintactico completo.

### Caracteristicas

- Analisis secuencial de izquierda a derecha
- No utiliza recursion ni estructuras complejas
- Complejidad lineal O(n)
- Menor capacidad de analisis comparado con CYK

---

## Implementacion

Ambos algoritmos fueron implementados en Python dentro del mismo programa, lo cual permite realizar una comparacion directa bajo las mismas condiciones de ejecucion.

Se mide:

- Numero de operaciones realizadas
- Tiempo de ejecucion en milisegundos

---

## Ejecucion de pruebas

Se realizaron pruebas con diferentes longitudes de cadenas para observar el comportamiento de ambos algoritmos.

Ejemplos:

```python
comparar(['a', '+', 'b'])
comparar(['a', '+', 'b', '*', 'c'])
comparar(['a', '+', 'b', '+', 'c', '+', 'd'])
comparar(['a', '*', 'b', '+', 'c', '*', 'd', '+', 'e'])
```
## Resultados

- El algoritmo CYK realiza una gran cantidad de operaciones incluso para cadenas pequenas
- El parser lineal mantiene un numero de operaciones proporcional al tamano de la entrada
- El tiempo de ejecucion del CYK crece rapidamente a medida que aumenta el numero de tokens

---

## Analisis

La diferencia principal entre ambos algoritmos radica en su complejidad:

- CYK: O(n^3), ya que evalua todas las combinaciones posibles de subcadenas
- Parser lineal: O(n), ya que recorre la cadena una sola vez

Esto demuestra que, aunque CYK es mas general y puede analizar una mayor variedad de gramaticas, su costo computacional es significativamente mayor.

---

## Conclusiones

- El algoritmo CYK es adecuado para analisis sintactico general, pero no es eficiente para entradas grandes
- El parser lineal es mucho mas eficiente, pero limitado en cuanto a la complejidad de las gramaticas que puede manejar
- La eleccion del algoritmo depende del contexto y de los requerimientos del sistema
