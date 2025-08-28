package utils

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func LeerFloat(mensaje string) float64 {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print(mensaje)
		input, _ := reader.ReadString('\n')
		valor, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
		if err == nil && valor >= 0 {
			return valor
		}
		fmt.Println("❌ Entrada inválida. Solo se permiten números positivos o cero.")
	}
}

func LeerEntero(mensaje string) int {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print(mensaje)
		input, _ := reader.ReadString('\n')
		valor, err := strconv.Atoi(strings.TrimSpace(input))
		if err == nil && valor >= 0  {
			return valor
		}
		fmt.Println("❌ Entrada inválida. Solo se permiten números enteros positivos o cero.")
	}
}