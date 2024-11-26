# Problema de las Donas de Néstor

## Descripción del Problema

Néstor, un abogado exitoso, tiene una peculiar preocupación: llegar tarde al trabajo debido a reflexionar sobre donas cuando su saldo bancario no es divisible por 1.

### Problema Principal

- **Contexto**: Néstor se retrasa cada vez que su saldo bancario no es un número entero.
- **Objetivo**: Calcular cuántas veces llegará tarde al trabajo en los próximos N días.

### Reglas del Problema

1. Precio de una dona: $1.00
2. Condición de retraso: Saldo bancario no divisible por 1 (tiene centavos)
3. Entrada:
   - Primer línea: Número de días N (1 ≤ N ≤ 1000)
   - Segunda línea: Saldo inicial de la cuenta
   - Siguientes N líneas: Depósitos diarios

### Solución Algorítmica

```python
N = int(input())  # Número de días
addition = 0      # Saldo acumulado
debt = 0          # Contador de retrasos

for i in range(N+1):
    # Extraer centavos del depósito
    addition += int(input().split("$")[1].split(".")[1])
    
    # Verificar si hay centavos (no divisible por 100)
    if i != 0 and addition % 100 != 0:
        debt += 1

print(debt)  # Imprimir total de días de retraso
```

### Desglose de la Solución

1. **Parsing de Entrada**:
   - Dividir cada entrada por "$" y "." para extraer centavos
   - Convertir centavos a entero

2. **Lógica de Retraso**:
   - Acumular saldo en `addition`
   - Verificar si hay centavos usando módulo 100
   - Incrementar `debt` si hay centavos
   - Ignorar el primer registro (saldo inicial)

### Ejemplo de Funcionamiento

Entrada:
```
2
$1.57
$3.14
$4.75
```

Proceso:
- Saldo inicial: $1.57 (retraso)
- Primer depósito: $3.14 (retraso)
- Segundo depósito: $4.75 (retraso)

Salida: `3` (3 días de retraso)

## Análisis de Complejidad

- **Tiempo**: O(N)
- **Espacio**: O(1)

## Aspectos Clave

- Manejo de cadenas para extracción de datos
- Uso de operaciones aritméticas simples
- Conteo condicional de retrasos

## Consideraciones Adicionales

- Solución enfocada en la extracción precisa de centavos
- Algoritmo simple y directo
- Manejo eficiente de múltiples casos de prueba

## Posibles Mejoras

- Validación de entrada
- Manejo de formatos de moneda más complejos
- Soporte para diferentes monedas

## Lección de Programación

La solución demuestra cómo problemas aparentemente complejos pueden resolverse con algoritmos simples y precisos.
