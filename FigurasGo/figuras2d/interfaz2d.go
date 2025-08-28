package figuras2d

// Figura2D define el comportamiento que deben implementar
// todas las figuras bidimensionales para calcular su área y perímetro.
type Figura2D interface {
	CalcularArea() float64
	CalcularPerimetro() float64
}
