package Figuras2D;

public class Cuadrado extends Figura2D {
    private double lado;

    // Constructor
    public Cuadrado(double lado) {
        this.lado = lado;
        this.calcularArea();
        this.calcularPerimetro();
    }

    // Getter y Setter
    public double getLado() {
        return lado;
    }

    public void setLado(double lado) {
        this.lado = lado;
        this.calcularArea();
        this.calcularPerimetro();
    }

    @Override
    public double calcularArea() {
        area = lado * lado;
        return area;
    }

    @Override
    public double calcularPerimetro() {
        perimetro = 4 * lado;
        return perimetro;
    }
}
