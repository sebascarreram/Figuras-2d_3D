# -*- coding: utf-8 -*-
"""
Módulo que contiene la clase Cuadrado.

Este módulo define la clase Cuadrado, que permite calcular el área y el perímetro de un cuadrado dado su lado.
"""

from interfaz2d import FigurasEn2D

class Cuadrado(FigurasEn2D):
    """
    Clase que representa un cuadrado y sus operaciones.

    Hereda de la clase FigurasEn2D y permite calcular el área y el perímetro de un cuadrado.
    """
    def __init__(self, lado: float):
        """
        Inicializa una instancia de la clase Cuadrado.

        Parámetros:
        lado (float): El valor del lado del cuadrado.
        """
        self.lado = lado

    def calcular_area(self) -> float:
        """
        Calcula el área del cuadrado.

        Devuelve:
        float: El área del cuadrado.
        """
        return self.lado ** 2

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del cuadrado.

        Devuelve:
        float: El perímetro del cuadrado.
        """
        return 4 * self.lado  # Dividir si la línea de código es muy larga
