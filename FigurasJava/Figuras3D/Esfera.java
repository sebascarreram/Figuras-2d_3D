package Figuras3D;



public class Esfera extends Figura3D {
    private double radio;

    // Constructor
    public Esfera(double radio) {
        this.radio = radio;
        this.calcularVolumen();
    }

    // Getter y Setter
    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
        this.calcularVolumen();
    }

    @Override
    public double calcularVolumen() {
        volumen = (4.0 / 3) * Math.PI * Math.pow(radio, 3);
        return volumen;
    }
}
