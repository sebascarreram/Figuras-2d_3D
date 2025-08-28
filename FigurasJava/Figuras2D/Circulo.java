package Figuras2D;

public class Circulo extends Figura2D {
    private double radio;

    // Constructor
    public Circulo(double radio) {
        this.radio = radio;
        this.calcularArea();
        this.calcularPerimetro();
    }

    // Getter y Setter
    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
        this.calcularArea();
        this.calcularPerimetro();
    }

    @Override
    public double calcularArea() {
        area = Math.PI * radio * radio;
        return area;
    }

    @Override
    public double calcularPerimetro() {
        perimetro = 2 * Math.PI * radio;
        return perimetro;
    }
}
