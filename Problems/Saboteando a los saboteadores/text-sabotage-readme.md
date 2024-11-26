# Algoritmo de Sabotaje de Comentarios

## Descripción del Problema

En un aula virtual de Algoritmos, se han detectado comentarios inapropiados de usuarios infiltrados. El profesor solicita un algoritmo para procesar estos comentarios.

### Objetivo del Algoritmo

Transformar comentarios mediante dos operaciones:
1. Eliminación de todas las vocales
2. Inversión de la cadena resultante

### Especificaciones Técnicas

- **Entrada**: 
  - Cadena de texto
  - Longitud entre 3 y 1000 caracteres
  - Sin tildes
  - Permite signos de puntuación

- **Salida**: 
  - Cadena sin vocales
  - Cadena invertida

### Solución Algorítmica

```python
def disemvowel(string_):
    # Definir conjunto de vocales (mayúsculas y minúsculas)
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    # Filtrar caracteres (eliminar vocales)
    aux = [v for v in string_ if v not in vowels]
    
    # Imprimir cadena invertida
    print(''.join(map(str, aux))[::-1])
```

### Desglose de la Solución

1. **Eliminación de Vocales**:
   - List comprehension para filtrar caracteres
   - Excluir vocales mayúsculas y minúsculas
   - Mantener signos de puntuación y espacios

2. **Inversión de Cadena**:
   - Usar slice `[::-1]` para invertir la cadena
   - Conversión a cadena con `''.join()`

### Ejemplos

1. Entrada: `"This website is for losers LOL!"`
   - Sin vocales: `"Ths wbst s fr lsrs LL!"`
   - Invertido: `"!LL srsl rf s tsbw shT"`

2. Entrada: `"No offense but, your writing is among the worst I've ever read"`
   - Sin vocales: `"N ffns bt, yr wrtng s mng th wrst 'v vr rd"`
   - Invertido: `"dr rv v' tsrw ht gnm s gntrw ry ,tb snff N"`

## Análisis de Complejidad

- **Tiempo**: O(n), donde n es la longitud de la cadena
- **Espacio**: O(n) para almacenar la cadena filtrada

## Características Técnicas

- **Funcionalidad**: Filtrado de texto
- **Flexibilidad**: Maneja mayúsculas, minúsculas y puntuación
- **Precisión**: Elimina solo vocales, preserva otros caracteres

## Consideraciones Importantes

- Algoritmo simple y directo
- Procesamiento en una sola pasada
- No modifica la cadena original

## Posibles Mejoras

- Soporte para idiomas con vocales acentuadas
- Opcionalidad de mayúsculas/minúsculas
- Parámetros configurables de filtrado

## Lección de Programación

Demuestra cómo operaciones simples de manipulación de cadenas pueden crear transformaciones complejas de texto.

## Casos de Uso

- Moderación de comentarios
- Juegos de transformación de texto
- Ejercicios de manipulación de cadenas

### Consejos de Implementación

- Usar list comprehension para filtrado eficiente
- Aprovechar slicing de Python para inversión
- Mantener código conciso y legible
