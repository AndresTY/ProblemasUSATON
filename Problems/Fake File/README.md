# Eliminación de Virus en Archivos Binarios

## Descripción del Problema

Un nuevo virus ha demostrado la capacidad de infectar los códigos de ciertos robots, alterando su archivo binario original mediante la inserción de fragmentos que generan comportamientos anómalos.

### Contexto del Problema

- **Objetivo**: Desarrollar un algoritmo de antivirus capaz de eliminar fragmentos de código introducidos por el virus.
- **Característica especial**: Si después de eliminar los fragmentos no queda ningún carácter, se considera un "fake file".

### Reglas de Eliminación de Virus

1. El archivo binario es una secuencia de caracteres en el rango ASCII ['a',...,'z'].
2. El proceso de limpieza funciona de la siguiente manera:
   - En cada paso, se seleccionan y eliminan pares de letras adyacentes idénticas.
   - La operación se repite sobre la nueva cadena hasta que no queden más caracteres duplicados adyacentes.

### Ejemplos

1. `s = "aab"` 
   - Resultado: `"b"` 
   - Se eliminan los caracteres 'a' adyacentes

2. `s = "abba"`
   - Paso 1: Eliminar 'bb' → `"aa"`
   - Paso 2: Eliminar 'aa' → cadena vacía 
   - Resultado final: `"fake file"`

### Formato de Entrada y Salida

- **Entrada**: Cadena de caracteres infectada
- **Salida**: 
  - Cadena limpia de virus
  - O la palabra `"fake file"` si no queda ningún carácter

## Solución Propuesta

La solución implementada utiliza un algoritmo de pila (stack) para procesar la cadena:

```python
def reduce_string(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Eliminar el último elemento si coincide con el carácter actual
        else:
            stack.append(char)  # Agregar carácter actual a la pila
    
    # Unir los caracteres restantes en la pila
    reduced_string = ''.join(stack)
    return reduced_string if reduced_string else "fake file"
```

### Funcionamiento del Algoritmo

1. Inicializar una pila vacía
2. Recorrer cada carácter de la cadena:
   - Si el último carácter de la pila coincide con el carácter actual, eliminarlo
   - Si no coincide, agregar el carácter a la pila
3. Unir los caracteres restantes en la pila
4. Si la pila queda vacía, devolver "fake file"

## Análisis de Complejidad

- **Tiempo**: O(n), donde n es la longitud de la cadena de entrada
- **Espacio**: O(n) para almacenar la pila

## Casos de Prueba

1. `"aaabccddd"` → `"abd"`
2. `"aa"` → `"fake file"`

## Posibles Mejoras

- Manejo de entradas no válidas
- Optimización del espacio utilizado
- Validación de rango de caracteres ASCII

## Aplicaciones

- Limpieza de archivos binarios
- Detección de código malicioso
- Procesamiento de cadenas con reglas de eliminación específicas

## Consideraciones Adicionales

El algoritmo es especialmente útil para:
- Restaurar archivos binarios a su estado original
- Identificar archivos completamente corrompidos
- Proporcionar una solución rápida y eficiente de limpieza de código
