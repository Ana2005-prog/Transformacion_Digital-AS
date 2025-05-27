def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numeros (list): Lista de números (int o float).

    Retorna:
    float: El promedio de los números en la lista.
           Retorna None si la lista está vacía.
    """
    if not numeros:
        return None
    return sum(numeros) / len(numeros)

# Ejemplo de uso
lista = [4, 8, 15, 16, 23, 42]
print("Promedio:", calcular_promedio(lista))
