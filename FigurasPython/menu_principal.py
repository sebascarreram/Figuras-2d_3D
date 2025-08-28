from FigurasEn2D.cuadrado import Cuadrado
from FigurasEn2D.circulo import Circulo
from FigurasEn3D.cubo import Cubo
from FigurasEn3D.esfera import Esfera
from utils.entrada import leer_float, leer_entero


class MenuFiguras:
    def mostrar_menu_figuras_2d(self):
        while True:
            print("\n-- Figuras 2D --")
            print("1. Área de Cuadrado")
            print("2. Perímetro de Cuadrado")
            print("3. Área de Círculo")
            print("4. Perímetro de Círculo")
            print("5. Volver al Menú Principal")

            opcion = leer_entero("Seleccione una opción: ")

            if opcion == 1:
                lado = leer_float("Ingrese el lado del cuadrado: ")
                c = Cuadrado(lado)
                print(f"Área del cuadrado: {c.calcular_area():.2f}")
            elif opcion == 2:
                lado = leer_float("Ingrese el lado del cuadrado: ")
                c = Cuadrado(lado)
                print(f"Perímetro del cuadrado: {c.calcular_perimetro():.2f}")
            elif opcion == 3:
                radio = leer_float("Ingrese el radio del círculo: ")
                c = Circulo(radio)
                print(f"Área del círculo: {c.calcular_area():.2f}")
            elif opcion == 4:
                radio = leer_float("Ingrese el radio del círculo: ")
                c = Circulo(radio)
                print(f"Perímetro del círculo: {c.calcular_perimetro():.2f}")
            elif opcion == 5:
                break
            else:
                print("Opción no válida.")

    def mostrar_menu_figuras_3d(self):
        while True:
            print("\n-- Figuras 3D --")
            print("1. Volumen de Cubo")
            print("2. Volumen de Esfera")
            print("3. Volver al Menú Principal")

            opcion = leer_entero("Seleccione una opción: ")

            if opcion == 1:
                lado = leer_float("Ingrese el lado del cubo: ")
                c = Cubo(lado)
                print(f"Volumen del cubo: {c.calcular_volumen():.2f}")
            elif opcion == 2:
                radio = leer_float("Ingrese el radio de la esfera: ")
                e = Esfera(radio)
                print(f"Volumen de la esfera: {e.calcular_volumen():.2f}")
            elif opcion == 3:
                break
            else:
                print("Opción no válida.")

    def mostrarMenu(self):
        while True:
            print("\n-- MENÚ DE FIGURAS --")
            print("1. Figuras 2D")
            print("2. Figuras 3D")
            print("3. Salir")

            opcion = leer_entero("Seleccione una opción: ")

            if opcion == 1:
                self.mostrar_menu_figuras_2d()
            elif opcion == 2:
                self.mostrar_menu_figuras_3d()
            elif opcion == 3:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
