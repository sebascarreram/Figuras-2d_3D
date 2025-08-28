package tests;

import Figuras2D.Cuadrado;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CuadradoTest {

    @Test
    public void testCalcularArea() {
        Cuadrado cuadrado = new Cuadrado(5);
        assertEquals(25, cuadrado.calcularArea(), 0.001);
    }

    @Test
    public void testCalcularPerimetro() {
        Cuadrado cuadrado = new Cuadrado(5);
        assertEquals(20, cuadrado.calcularPerimetro(), 0.001);
    }

    @Test
    public void testSetters() {
        Cuadrado cuadrado = new Cuadrado(5);
        cuadrado.setLado(6);
        assertEquals(36, cuadrado.calcularArea(), 0.001);
        assertEquals(24, cuadrado.calcularPerimetro(), 0.001);
    }
}
