# Problema: Máquina Expendedora de Bebidas

## Descripción del Problema

En una cafetería, se instaló una máquina expendedora de bebidas que tiene un error en su función de cálculo de precios. La máquina recibe dos listas que representan números enteros no negativos, pero estos están almacenados **en orden inverso**. Cada elemento de la lista es un solo dígito. El objetivo es implementar una función que calcule la **suma total** de los números representados por estas listas, y retorne el resultado también como una lista con los dígitos en orden inverso.

### Ejemplo

Si se reciben las siguientes listas:

- Entrada: `l1 = [2, 4, 3]` y `l2 = [5, 6, 4]`
- Estas listas representan los números 342 y 465.
- La suma de estos números es 807.
- Salida esperada: `[7, 0, 8]`

---

## Solución

### Lógica de la Solución

La solución implementa la suma dígito a dígito de las listas de entrada, manejando el acarreo (carry) en cada paso:

1. **Alinear las Listas por Tamaño**:
   - Se determina cuál de las listas es más larga.
   - Si la lista más corta se queda sin dígitos, se considera un `0` para continuar la suma.

2. **Suma con Acarreo**:
   - Se suman los elementos correspondientes de ambas listas junto con un valor auxiliar (`aux`) que guarda el acarreo de la operación anterior.
   - Si la suma de dos dígitos es mayor o igual a 10, se calcula el acarreo (`aux = r // 10`) y se almacena el residuo (`r % 10`) como parte del resultado.

3. **Acarreo Final**:
   - Si al final de la suma queda un acarreo, se agrega como un nuevo dígito al resultado.

4. **Salida del Resultado**:
   - El resultado se imprime como una lista de dígitos separados por espacios.

---

### Código Implementado

```python
def addTwoArrays(l1, l2):
    aux = 0  # Carries the decimal
    result = []

    # Determinar las listas más largas y más cortas
    lx = l1 if len(l1) >= len(l2) else l2
    ly = l1 if len(l1) < len(l2) else l2

    for idx, val1 in enumerate(lx):
        val2 = ly[idx] if len(ly) > idx else 0

        r = val1 + val2 + aux
        # El nuevo dígito es el residuo de r dividido por 10
        result.append(r % 10)
        # Actualizar el carry
        aux = r // 10

    if aux:
        result.append(aux)

    # Imprimir los valores del resultado separados por espacios
    print(" ".join(map(str, result)))

# Test de la función
if __name__ == '__main__':
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]

    addTwoArrays(l1, l2)
```

---

### Ejemplo de Ejecución

#### Entrada:
```
2 4 3
5 6 4
```

#### Salida:
```
7 0 8
```

#### Explicación:
1. Las listas representan los números 342 y 465 (en orden inverso).
2. La suma es 807.
3. El resultado `[7, 0, 8]` es la representación inversa de 807.

---

## Complejidad

1. **Tiempo**:
   - La función recorre la lista más larga una vez, por lo que la complejidad es **O(n)**, donde **n** es la longitud de la lista más larga.

2. **Espacio**:
   - Se utiliza una lista para almacenar el resultado, lo que también requiere **O(n)** espacio adicional.

---

## Notas

- La implementación asume que las listas de entrada siempre contienen dígitos válidos (`0-9`) y están en el formato requerido (orden inverso).
- El programa maneja casos en los que las listas tienen tamaños diferentes.

---

## Casos de Prueba

1. **Entrada:**
   ```
   9 9
   1
   ```
   **Salida:**
   ```
   0 0 1
   ```
   **Explicación:**
   - La suma de 99 y 1 es 100, representada como `[0, 0, 1]`.

2. **Entrada:**
   ```
   2 4 3
   5 6 4
   ```
   **Salida:**
   ```
   7 0 8
   ```

3. **Entrada:**
   ```
   0
   0
   ```
   **Salida:**
   ```
   0
   ```

---

