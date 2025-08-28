package figuras2d

// Cuadrado representa una figura bidimensional definida por la longitud de su lado.
type Cuadrado struct {
	Lado float64
}

// CalcularArea retorna el área del cuadrado usando la fórmula lado².
func (c Cuadrado) CalcularArea() float64 {
	return c.Lado * c.Lado
}

// CalcularPerimetro retorna el perímetro del cuadrado usando la fórmula 4 * lado.
func (c Cuadrado) CalcularPerimetro() float64 {
	return 4 * c.Lado
}
