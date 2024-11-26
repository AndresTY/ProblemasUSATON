# Identificación de Grupos de Asteroides

## Descripción del Problema

Un grupo de naves espaciales de exploración profunda ha recopilado datos sobre asteroides en un sistema solar desconocido, con el objetivo de identificar y clasificar los tipos de asteroides más frecuentes.

### Contexto del Problema

- **Objetivo**: Desarrollar un programa que identifique los n grupos más grandes de detecciones de asteroides.
- **Características del problema**:
  - Tipología de asteroides: 26 clases diferentes (letras mayúsculas de A a Z)
  - Registro de asteroides puede contener repeticiones
  - Múltiples encuentros del mismo tipo de asteroide

### Reglas de Identificación

1. Contar la frecuencia de cada tipo de asteroide
2. Ordenar los grupos por:
   - Número de detecciones (descendente)
   - En caso de empate, orden alfabético
3. Devolver los n grupos más grandes

### Ejemplos

1. Entrada: `A B C D E F F E D C C E D F F E D C B A A A A A F F F`
   - Salida: `[('F', 7), ('A', 6)]`
   - F aparece 7 veces
   - A aparece 6 veces

2. Entrada: `Z A S D A Z A S D E W Z A S D E W Q A Q A Q S`
   - Salida: `[('A', 6), ('S', 4), ('D', 3)]`

### Formato de Entrada y Salida

- **Entrada**:
  1. Número de casos de prueba
  2. Para cada caso:
     - Número n de grupos a identificar
     - Lista de registros de asteroides
- **Salida**: Lista de n tuplas con (tipo de asteroide, número de detecciones)

## Solución Propuesta

La solución implementa un algoritmo de conteo y ordenamiento:

```python
def identificar_asteroides(cant, asteroides, verbose=False):
    # Contar frecuencia de asteroides
    grupos = dict() 
    for ast in asteroides:
        try:
            grupos[ast] += 1 
        except: 
            grupos[ast] = 1
    del(grupos[' '])  # Eliminar espacios en blanco

    # Convertir a lista de tuplas
    grupos = list(grupos.items())
    
    # Ordenar por:
    # 1. Frecuencia (descendente)
    # 2. Tipo de asteroide (alfabético)
    inter = sorted(grupos, key=lambda x: x[0])
    grupos_ordenados = sorted(inter, key=lambda x: x[1], reverse=True)

    # Devolver n grupos más grandes
    return grupos_ordenados[:cant] if cant <= len(grupos_ordenados) else grupos_ordenados
```

### Funcionamiento del Algoritmo

1. Contar frecuencia de cada tipo de asteroide
2. Eliminar espacios en blanco
3. Convertir diccionario a lista de tuplas
4. Ordenar por:
   - Tipo de asteroide (paso intermedio)
   - Número de detecciones (descendente)
5. Devolver los n grupos más grandes

## Análisis de Complejidad

- **Tiempo**: O(n log n) debido al proceso de ordenamiento
- **Espacio**: O(n) para almacenar el diccionario y la lista de grupos

## Casos de Prueba

1. Entrada con varios tipos de asteroides
2. Entrada con pocos tipos de asteroides
3. Entrada con muchas repeticiones

## Posibles Mejoras

- Manejo de entradas no válidas
- Optimización del algoritmo de ordenamiento
- Soporte para más de 26 tipos de asteroides

## Aplicaciones

- Análisis de datos de exploración espacial
- Clasificación de objetos por frecuencia
- Procesamiento de registros con múltiples categorías

## Consideraciones Adicionales

El algoritmo es útil para:
- Identificar patrones en datos de exploración
- Priorizar tipos de asteroides más frecuentes
- Realizar análisis estadísticos de detecciones
