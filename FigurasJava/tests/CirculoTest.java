package tests;

import Figuras2D.Circulo;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CirculoTest {

    @Test
    public void testCalcularArea() {
        Circulo circulo = new Circulo(5);
        assertEquals(78.5398, circulo.calcularArea(), 0.001);
    }

    @Test
    public void testCalcularPerimetro() {
        Circulo circulo = new Circulo(5);
        assertEquals(31.4159, circulo.calcularPerimetro(), 0.001);
    }

    @Test
    public void testSetters() {
        Circulo circulo = new Circulo(5);
        circulo.setRadio(7);
        assertEquals(153.938, circulo.calcularArea(), 0.001);
        assertEquals(43.982, circulo.calcularPerimetro(), 0.001);
    }
}
