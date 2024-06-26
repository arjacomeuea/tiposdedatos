# area_calculator.py

"""
Este programa calcula el área de un círculo dado su radio.
Utiliza diferentes tipos de datos: integer, float, string y boolean.
Sigue las convenciones de nomenclatura recomendadas para Python.
"""

import math  # Importamos el módulo math para usar la constante pi


def calculate_circle_area(radius):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radius (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    # Calculamos el área usando la fórmula: área = pi * radio^2
    area = math.pi * (radius ** 2)
    return area


def main():
    """
    Función principal del programa. Solicita al usuario el radio del círculo,
    calcula el área y muestra el resultado.
    """
    # Solicitamos al usuario que introduzca el radio del círculo
    user_input = input("Introduce el radio del círculo: ")

    try:
        # Convertimos la entrada del usuario a un número de punto flotante
        radius = float(user_input)

        # Verificamos que el radio no sea negativo
        if radius < 0:
            raise ValueError("El radio no puede ser negativo.")

        # Calculamos el área del círculo llamando a la función calculate_circle_area
        area = calculate_circle_area(radius)

        # Mostramos el resultado al usuario con dos decimales
        print(f"El área del círculo con radio {radius} es: {area:.2f}")

    except ValueError as e:
        # Manejamos entradas no válidas e informamos al usuario
        print(f"Entrada no válida: {e}")


# Verificamos si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()  # Llamamos a la función principal
