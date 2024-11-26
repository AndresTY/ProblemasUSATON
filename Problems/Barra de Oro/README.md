
# Problema B - Barra de Oro

## Descripción del Problema

Un prestamista quiere recibir pagos diarios durante **n días** de un minero endeudado. El minero posee un lingote de oro de longitud **nµ** y debe entregar una parte diaria equivalente a 1µ, pero puede reutilizar trozos previamente entregados para minimizar el número de cortes necesarios en la barra de oro. El objetivo es calcular el **mínimo número de cortes** que debe realizar el minero para cumplir con las entregas diarias.

### Entrada
- Múltiples casos de prueba, cada uno con un entero positivo **n** (`0 < n < 20000`), que representa la longitud del lingote en micras y el número de días.
- Termina con un `0`.

### Salida
- Para cada caso de prueba, un único número que representa el **mínimo número de cortes** necesarios para dividir el lingote.

#### Ejemplo

**Entrada**  
```
1  
5  
6  
0
```

**Salida**  
```
0  
2  
1
```

---

## Solución

El problema puede resolverse utilizando el concepto de **representación binaria** y la estrategia del **problema del intercambio de oro**. La clave es observar que para minimizar el número de cortes, necesitamos dividir la barra en piezas que correspondan a potencias de 2. Estas piezas permiten cubrir todas las combinaciones posibles de pagos diarios mediante sumas de trozos reutilizados.

### Observaciones Clave

1. **Regla de las potencias de 2**:  
   - Dividiendo el lingote en piezas de tamaños correspondientes a las potencias de 2 (1, 2, 4, 8, ...), podemos pagar cualquier cantidad entre 1 y **n** sin necesidad de realizar más cortes.
   
2. **Relación con logaritmos**:  
   - El número mínimo de cortes necesarios es igual al **número de bits necesarios** para representar el número **n** en binario. Esto se calcula como `floor(log₂(n))`.

3. **Ejemplo con n = 6**:  
   - Binario de 6: `110`  
   - Se necesitan piezas de 4, 2 y 1 (2 cortes para obtener estas piezas).

---

## Implementación en Python

El archivo `solution.py` contiene la implementación de la solución:

```python
from math import log

while True:
    n = int(input())
    if n == 0:
        break
    print(int(log(n, 2)))
```

### Explicación del Código
1. **Entrada de Datos**:
   - Lee múltiples casos de prueba hasta encontrar un `0`.

2. **Cálculo del Mínimo de Cortes**:
   - Usa la fórmula `log(n, 2)` para calcular el número de cortes necesarios.

3. **Salida**:
   - Imprime el resultado para cada caso de prueba.

---

## Complejidad

1. **Tiempo**:  
   - Calcular `log₂(n)` para cada caso tiene complejidad **O(1)**.  
   - Para **m casos**, la complejidad total es **O(m)**.

2. **Espacio**:  
   - Uso constante de memoria, por lo que la complejidad espacial es **O(1)**.

---

## Ejecución

### Entrada de Ejemplo:
```
1
5
6
0
```

### Salida Correspondiente:
```
0
2
1
```

---

## Notas

- Esta solución aprovecha propiedades matemáticas para garantizar la eficiencia incluso para valores grandes de **n** (hasta 20,000).
- El código está diseñado para manejar múltiples casos de prueba de manera continua hasta que se introduce el valor `0`.
