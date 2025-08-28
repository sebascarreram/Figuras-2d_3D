package figuras3d

// Figura3D define el comportamiento que deben implementar
// todas las figuras tridimensionales para calcular su volumen.
type Figura3D interface {
	calcularVolumen() float64
}
