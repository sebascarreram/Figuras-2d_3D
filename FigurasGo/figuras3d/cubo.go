package figuras3d

import "math"

// Cubo representa una figura tridimensional con lados iguales.
type Cubo struct {
	Lado float64
}

// CalcularVolumen retorna el volumen del cubo usando la fórmula Lado³.
func (c Cubo) CalcularVolumen() float64 {
	return math.Pow(c.Lado, 3)
}
