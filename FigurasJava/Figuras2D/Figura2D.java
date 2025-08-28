package Figuras2D;


public abstract class Figura2D {
    protected double area;
    protected double perimetro;

    // Constructor
    public Figura2D() {}

    // Getters
    public double getArea() {
        return area;
    }

    public double getPerimetro() {
        return perimetro;
    }

    // Setters
    public void setArea(double area) {
        this.area = area;
    }

    public void setPerimetro(double perimetro) {
        this.perimetro = perimetro;
    }

    // Métodos abstractos
    public abstract double calcularArea();
    public abstract double calcularPerimetro();
}
