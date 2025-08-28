package tests;

import Figuras3D.Cubo;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CuboTest {

    @Test
    public void testCalcularVolumen() {
        Cubo cubo = new Cubo(5);
        assertEquals(125, cubo.calcularVolumen(), 0.001);
    }

    @Test
    public void testSetters() {
        Cubo cubo = new Cubo(5);
        cubo.setLado(7);
        assertEquals(343, cubo.calcularVolumen(), 0.001);
    }
}
