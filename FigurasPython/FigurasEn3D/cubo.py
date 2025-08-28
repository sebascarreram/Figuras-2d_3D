# -*- coding: utf-8 -*-
"""
Módulo que define la clase Cubo.

Este módulo contiene la implementación de la clase Cubo, que hereda de FigurasEn3D y proporciona
la implementación para calcular el volumen de un cubo dado su lado.
"""

from .interfaz3d import FigurasEn3D

class Cubo(FigurasEn3D):
    """
    Clase que representa un cubo y sus operaciones.

    La clase Cubo hereda de la clase abstracta FigurasEn3D y proporciona la implementación
    específica para calcular el volumen de un cubo dado su lado.
    """
    def __init__(self, lado: float):
        """
        Inicializa una nueva instancia de la clase Cubo.

        Parámetros:
        lado (float): El lado del cubo.
        """
        self.lado = lado

    def calcular_volumen(self) -> float:
        """
        Calcula el volumen del cubo.

        Devuelve:
        float: El volumen del cubo.
        """
        return self.lado ** 3
