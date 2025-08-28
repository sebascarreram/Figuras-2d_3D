# -*- coding: utf-8 -*-
"""
Módulo que define la clase base FigurasEn2D para figuras bidimensionales.

Este módulo contiene una clase abstracta que sirve como base para otras figuras geométricas
en 2D. Las clases derivadas deben implementar los métodos para calcular el área y el perímetro
de la figura.
"""

from abc import ABC, abstractmethod

class FigurasEn2D(ABC):
    """
    Clase abstracta que representa una figura en dos dimensiones.

    Esta clase proporciona una interfaz para calcular el área y el perímetro de cualquier figura 2D.
    Las clases que hereden de FigurasEn2D deben implementar estos métodos.
    """

    @abstractmethod
    def calcular_area(self) -> float:
        """
        Método abstracto para calcular el área de la figura.

        Devuelve:
        float: El área de la figura.
        """
        

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """
        Método abstracto para calcular el perímetro de la figura.

        Devuelve:
        float: El perímetro de la figura.
        """
        
