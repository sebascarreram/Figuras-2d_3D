# -*- coding: utf-8 -*-
"""
Módulo que define la clase Esfera.

Este módulo contiene la implementación de la clase Esfera, que hereda de FigurasEn3D y proporciona
la implementación para calcular el volumen de una esfera dado su radio.
"""

import math
from .interfaz3d import FigurasEn3D

class Esfera(FigurasEn3D):
    """
    Clase que representa una esfera y sus operaciones.

    La clase Esfera hereda de la clase abstracta FigurasEn3D y proporciona la implementación
    específica para calcular el volumen de una esfera dada su radio.
    """
    def __init__(self, radio: float):
        """
        Inicializa una nueva instancia de la clase Esfera.

        Parámetros:
        radio (float): El radio de la esfera.
        """
        self.radio = radio

    def calcular_volumen(self) -> float:
        """
        Calcula el volumen de la esfera.

        Devuelve:
        float: El volumen de la esfera.
        """
        return (4 / 3) * math.pi * self.radio ** 3
