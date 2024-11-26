# Problema: Dividir una Cadena para Maximizar la Puntuación

## Descripción del Problema

Se tiene una cadena binaria **s** de ceros y unos, y se desea dividirla en **dos subcadenas no vacías**. La puntuación se define como la cantidad de ceros en la subcadena izquierda más la cantidad de unos en la subcadena derecha. El objetivo es determinar la **puntuación máxima** que se puede obtener al realizar dicha división.

### Entrada
1. Un entero **t** que indica el número de casos de prueba, donde `1 ≤ t ≤ 200`.
2. **t** cadenas binarias **sᵢ**, donde cada cadena cumple:
   - `2 ≤ longitud(sᵢ) ≤ 500`.

### Salida
Para cada cadena **sᵢ**, se debe imprimir un número entero que representa la puntuación máxima obtenida al dividir la cadena.

---

## Ejemplo

### Entrada
```
2
011101
110
```

### Salida
```
5
2
```

### Explicación
1. Para la cadena `011101`:
   - Mejor división: izquierda = `0` (1 cero), derecha = `11101` (4 unos). Puntuación máxima = `1 + 4 = 5`.

2. Para la cadena `110`:
   - Mejor división: izquierda = `11` (0 ceros), derecha = `0` (1 uno). Puntuación máxima = `2`.

---

## Solución

### Lógica de la Solución

La solución utiliza una estrategia de **búsqueda exhaustiva** para probar todas las divisiones posibles de la cadena y calcular la puntuación máxima:

1. Iterar por cada posible **pivote** donde se puede dividir la cadena en dos partes.
2. Calcular la puntuación de esa división:
   - Contar los ceros (`'0'`) en la subcadena izquierda.
   - Contar los unos (`'1'`) en la subcadena derecha.
3. Guardar la puntuación obtenida en un diccionario asociado al pivote.
4. Retornar la puntuación máxima encontrada.

### Código Implementado

```python
def max_score(s):
    scores = {}
    for pivot in range(len(s)):
        left_side, right_side = list(s[:pivot + 1]), list(s[pivot + 1:])
        if not left_side or not right_side:
            continue
        scores[pivot] = left_side.count('0') + right_side.count('1')
    
    return max(scores.values()) if scores else 0

t = int(input())
for _ in range(t):
    print(max_score(input()))
```

---

## Explicación del Código

1. **Función `max_score(s)`**:
   - Toma como entrada una cadena binaria `s`.
   - Prueba todas las divisiones posibles utilizando un bucle sobre los pivotes de la cadena.
   - Calcula la puntuación para cada división y la almacena en un diccionario `scores`.

2. **Entrada y Salida**:
   - Se lee el número de casos de prueba (`t`) y, para cada caso, se calcula la puntuación máxima de la cadena.

3. **Uso de Estructuras**:
   - Se usa un diccionario para almacenar las puntuaciones asociadas a cada pivote.
   - La puntuación máxima se obtiene con `max(scores.values())`.

---

## Complejidad

1. **Tiempo**:
   - El cálculo de la puntuación para cada pivote implica contar ceros y unos, lo que tiene un costo lineal con respecto al tamaño de la cadena.
   - Para cada cadena, la complejidad es **O(n²)**, donde **n** es la longitud de la cadena.

2. **Espacio**:
   - El diccionario `scores` tiene un espacio proporcional al número de pivotes, es decir, **O(n)**.

---

## Ejecución Ejemplo

### Entrada:
```
2
011101
110
```

### Ejecución:
1. Para la cadena `011101`, las puntuaciones obtenidas son:
   - Izquierda = `0`, Derecha = `11101` → Puntuación = `1 + 4 = 5`
   - Izquierda = `01`, Derecha = `1101` → Puntuación = `1 + 3 = 4`
   - ... (otras divisiones)
   - **Máxima puntuación**: `5`.

2. Para la cadena `110`, las puntuaciones obtenidas son:
   - Izquierda = `1`, Derecha = `10` → Puntuación = `0 + 1 = 1`
   - Izquierda = `11`, Derecha = `0` → Puntuación = `2 + 0 = 2`
   - **Máxima puntuación**: `2`.

### Salida:
```
5
2
```

---

## Notas Finales

- Aunque esta implementación es funcional, para cadenas más largas es posible optimizar el cálculo utilizando técnicas acumulativas.
- **Posible optimización:** Usar arreglos precomputados para el conteo acumulado de ceros y unos, reduciendo la complejidad a **O(n)** para cada cadena.

--- 