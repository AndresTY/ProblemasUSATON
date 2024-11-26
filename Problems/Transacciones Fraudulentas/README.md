# Problema: Detección de Transacciones Fraudulentas

## Descripción del Problema

Un banco desea detectar posibles transacciones fraudulentas en las cuentas de sus clientes. Si el gasto diario de un cliente es **mayor o igual al doble de la mediana** de los gastos de un número específico de días previos, el banco envía una **notificación de advertencia**. La tarea es implementar un programa que determine cuántas notificaciones de advertencia se envían en un período determinado.

### Entrada

1. **`n`**: Número total de días.
2. **`d`**: Tamaño de la ventana de días previos para calcular la mediana.
3. **`expenditure`**: Lista de enteros que representan los gastos diarios del cliente.

### Salida

- Un entero que indica la cantidad de notificaciones enviadas.

---

## Ejemplo

### Entrada
```
9 5
2 3 4 2 3 6 8 4 5
```

### Salida
```
2
```

### Explicación

1. **Día 6**: Ventana de días previos = `[2, 3, 4, 2, 3]`.  
   - Mediana = `3`.  
   - Gasto actual = `6`.  
   - Dado que `6 >= 2 × 3`, se envía una notificación.

2. **Día 7**: Ventana de días previos = `[3, 4, 2, 3, 6]`.  
   - Mediana = `4`.  
   - Gasto actual = `8`.  
   - Dado que `8 >= 2 × 4`, se envía otra notificación.

3. **Día 8**: Ventana de días previos = `[4, 2, 3, 6, 8]`.  
   - Mediana = `4`.  
   - Gasto actual = `4`.  
   - No se envía notificación.

4. **Día 9**: Ventana de días previos = `[2, 3, 6, 8, 4]`.  
   - Mediana = `6`.  
   - Gasto actual = `5`.  
   - No se envía notificación.

Total: **2 notificaciones**.

---

## Solución

La solución implementa una técnica eficiente para calcular la mediana de una ventana deslizante y determinar si se debe enviar una notificación.

### Lógica de la Solución

1. **Cálculo de la Mediana**:
   - Si el tamaño de la ventana `d` es impar, la mediana es el valor central de la lista ordenada.
   - Si `d` es par, la mediana es el promedio de los dos valores centrales.

2. **Ventana Deslizante**:
   - Se mantiene una ventana ordenada de tamaño `d` que contiene los gastos de los días previos.
   - Para cada nuevo día:
     - Calcular la mediana de la ventana.
     - Comparar el gasto del día actual con el doble de la mediana.
     - Actualizar la ventana deslizante eliminando el gasto que sale y agregando el nuevo gasto.

3. **Notificación**:
   - Si el gasto del día actual es mayor o igual al doble de la mediana, se incrementa el contador de notificaciones.

### Código Implementado

```python
from bisect import insort, bisect_left

def median(sorted_window, d):
    if d % 2 == 1:
        return sorted_window[d // 2]
    else:
        return (sorted_window[d // 2] + sorted_window[d // 2 - 1]) / 2

def activityNotifications(expenditure, d):
    notifications = 0
    sorted_window = sorted(expenditure[:d])
    
    for i in range(d, len(expenditure)):
        med = median(sorted_window, d)
        if expenditure[i] >= 2 * med:
            notifications += 1
        
        old_value = expenditure[i - d]
        del sorted_window[bisect_left(sorted_window, old_value)]
        insort(sorted_window, expenditure[i])
        
    return notifications

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(str(result))
```

---

## Complejidad

1. **Tiempo**:
   - **Ordenamiento inicial**: Ordenar los primeros `d` elementos toma **O(d log d)**.
   - **Actualización de la ventana**: Cada inserción o eliminación toma **O(log d)**.
   - Para `n - d` días, la complejidad total es **O((n - d) × log d)**.

2. **Espacio**:
   - Se utiliza espacio adicional para almacenar la ventana ordenada, que tiene un tamaño de **O(d)**.

---

## Casos de Prueba

1. **Entrada:**
   ```
   5 3
   10 20 30 40 50
   ```
   **Salida:**
   ```
   1
   ```

2. **Entrada:**
   ```
   9 5
   2 3 4 2 3 6 8 4 5
   ```
   **Salida:**
   ```
   2
   ```

3. **Entrada:**
   ```
   4 4
   1 2 3 4
   ```
   **Salida:**
   ```
   0
   ```

---

## Notas Finales

- Este enfoque es eficiente y funciona bien para ventanas de tamaño moderado.
- Si `d` es muy grande, es posible que se necesiten optimizaciones adicionales para mejorar el rendimiento.
