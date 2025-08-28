package Figuras3D;



public abstract class Figura3D {
    protected double volumen;

    // Constructor
    public Figura3D() {}

    // Getter
    public double getVolumen() {
        return volumen;
    }

    // Setter
    public void setVolumen(double volumen) {
        this.volumen = volumen;
    }

    // Método abstracto
    public abstract double calcularVolumen();
}
