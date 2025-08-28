package figuras2d

import "math"

// Circulo representa una figura bidimensional definida por su radio.
type Circulo struct {
	Radio float64
}

// CalcularArea retorna el área del círculo usando la fórmula π * r².
func (c Circulo) CalcularArea() float64 {
	return math.Pi * c.Radio * c.Radio
}

// CalcularPerimetro retorna el perímetro del círculo usando la fórmula 2 * π * r.
func (c Circulo) CalcularPerimetro() float64 {
	return 2 * math.Pi * c.Radio
}
