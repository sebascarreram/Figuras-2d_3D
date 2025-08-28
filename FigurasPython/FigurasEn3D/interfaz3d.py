# -*- coding: utf-8 -*-
"""
Módulo que define la clase base FigurasEn3D para figuras tridimensionales.

Este módulo contiene una clase abstracta que sirve como base para otras figuras geométricas en 3D.
Las clases derivadas deben implementar el método para calcular el volumen de la figura.
"""

from abc import ABC, abstractmethod

class FigurasEn3D(ABC):
    """
    Clase abstracta que representa una figura en tres dimensiones.

    Esta clase proporciona una interfaz para calcular el volumen de cualquier figura 3D.
    Las clases que hereden de FigurasEn3D deben implementar este método.
    """
    @abstractmethod
    def calcular_volumen(self) -> float:
        """
        Método abstracto para calcular el volumen de la figura tridimensional.

        Devuelve:
        float: El volumen de la figura.
        """
        pass