package tests;

import Figuras3D.Esfera;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EsferaTest {

    @Test
    public void testCalcularVolumen() {
        Esfera esfera = new Esfera(5);
        // Volumen esperado de la esfera con radio 5
        assertEquals(523.598, esfera.calcularVolumen(), 0.001);
    }

    @Test
    public void testSetters() {
        Esfera esfera = new Esfera(5);
        esfera.setRadio(7);
        // Volumen esperado de la esfera con radio 7
        assertEquals(1436.756, esfera.calcularVolumen(), 0.001);
    }
}
