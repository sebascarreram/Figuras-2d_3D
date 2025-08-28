package figuras3d

import "math"

// Esfera representa una figura tridimensional definida por su radio.
type Esfera struct {
	Radio float64
}

// CalcularVolumen retorna el volumen de la esfera usando la fórmula (4/3) * π * r³.
func (e Esfera) CalcularVolumen() float64 {
	return (4.0 / 3.0) * math.Pi * math.Pow(e.Radio, 3)
}
