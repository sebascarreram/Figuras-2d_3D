package main

import (
	"fmt"
	"miapp/figuras2d"
	"miapp/figuras3d"
	"miapp/utils"
)

// MostrarMenu despliega el menú principal de la aplicación y
// permite navegar entre las opciones de figuras 2D, 3D o salir.
func MostrarMenu() {
	for {
		fmt.Println("\n--Menu de FIGURAS--")
		fmt.Println("1. Figuras 2D")
		fmt.Println("2. Figuras 3D")
		fmt.Println("3. Salir")

		opcion := utils.LeerEntero("Seleccione una opcion: ")

		switch opcion {
		case 1:
			menuFiguras2D()
		case 2:
			menuFiguras3D()
		case 3:
			fmt.Println("Saliendo...")
			return
		default:
			fmt.Println("Opcion no valida")
		}
	}
}

func menuFiguras2D() {
	for {
		fmt.Println("\n--Figuras 2D--")
		fmt.Println("1. Area de cuadrado")
		fmt.Println("2. Area de circulo")
		fmt.Println("3. Volver al menu principal")

		opcion := utils.LeerEntero("Seleccione una opcion: ")
		switch opcion {
		case 1:
			lado := utils.LeerFloat("Ingrese el lado del cuadrado: ")
			c := figuras2d.Cuadrado{Lado: lado}
			fmt.Println("Area del cuadrado: ", c.CalcularArea())
		case 2:
			radio := utils.LeerFloat("Ingrese el radio del circulo: ")
			c := figuras2d.Circulo{Radio: radio}
			fmt.Println("Area del circulo: ", c.CalcularArea())
		case 3:
			return
		default:
			fmt.Println("Opcion no valida.")
		}
	}
}

func menuFiguras3D() {
	for {
		fmt.Println("\n--Figuras 3D--")
		fmt.Println("1. Volumen de Cubo")
		fmt.Println("2. Volumen de Esfera")
		fmt.Println("3. Volver al menu Principal")

		opcion := utils.LeerEntero("Seleccion una opcion: ")

		switch opcion {
		case 1:
			lado := utils.LeerFloat("Ingrese el lado del cubo: ")
			c := figuras3d.Cubo{Lado: lado}
			fmt.Println("Volumen del cubo: ", c.CalcularVolumen())
		case 2:
			radio := utils.LeerFloat("Ingrese el radio de la esfera: ")
			e := figuras3d.Esfera{Radio: radio}
			fmt.Println("Volumen de la esfera: ", e.CalcularVolumen())
		case 3:
			return
		default:
			fmt.Println("Opcion no valida.")
		}
	}
}
