# -*- coding: utf-8 -*-
"""
Módulo que define la clase Circulo.

Este módulo contiene la implementación de la clase Circulo, que hereda de FigurasEn2D y proporciona
las implementaciones para calcular el área y el perímetro de un círculo.
"""

import math
from interfaz2d import FigurasEn2D

class Circulo(FigurasEn2D):
    """
    Clase que representa un círculo y sus operaciones.

    La clase Circulo hereda de la clase abstracta FigurasEn2D y proporciona implementaciones específicas
    para calcular el área y el perímetro de un círculo dado su radio.
    """
    def __init__(self, radio: float):
        """
        Inicializa una nueva instancia de la clase Circulo.

        Parámetros:
        radio (float): El radio del círculo.
        """
        self.radio = radio

    def calcular_area(self) -> float:
        """
        Calcula el área del círculo.

        Devuelve:
        float: El área del círculo.
        """
        return math.pi * self.radio ** 2

    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del círculo.

        Devuelve:
        float: El perímetro del círculo.
        """
        return 2 * math.pi * \
                        self.radio
