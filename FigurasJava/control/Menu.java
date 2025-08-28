package control;

import Figuras2D.Cuadrado;
import Figuras2D.Circulo;
import Figuras3D.Cubo;
import Figuras3D.Esfera;

import java.util.Scanner;

public class Menu {
    public void mostrarMenu() {
        Scanner sc = new Scanner(System.in);
        System.out.println("=== Menú ===");
        System.out.println("1. Calcular área y perímetro de figuras 2D");
        System.out.println("2. Calcular volumen de figuras 3D");
        System.out.println("3. Salir");
        System.out.print("Selecciona una opción: ");
        int opcion = sc.nextInt();
        seleccionarFigura(opcion);
    }

    public void seleccionarFigura(int opcion) {
        Scanner sc = new Scanner(System.in);
        if (opcion == 1) {
            System.out.println("Seleccione una figura:");
            System.out.println("1. Cuadrado");
            System.out.println("2. Círculo");
            System.out.print("Opción: ");
            int figura = sc.nextInt();
            if (figura == 1) {
                System.out.print("Introduce el lado del cuadrado: ");
                double lado = sc.nextDouble();
                Cuadrado cuadrado = new Cuadrado(lado);
                System.out.println("Área: " + cuadrado.calcularArea());
                System.out.println("Perímetro: " + cuadrado.calcularPerimetro());
            } else if (figura == 2) {
                System.out.print("Introduce el radio del círculo: ");
                double radio = sc.nextDouble();
                Circulo circulo = new Circulo(radio);
                System.out.println("Área: " + circulo.calcularArea());
                System.out.println("Perímetro: " + circulo.calcularPerimetro());
            }
        } else if (opcion == 2) {
            System.out.println("Seleccione una figura 3D:");
            System.out.println("1. Esfera");
            System.out.println("2. Cubo");
            System.out.print("Opción: ");
            int figura = sc.nextInt();
            if (figura == 1) {
                System.out.print("Introduce el radio de la esfera: ");
                double radio = sc.nextDouble();
                Esfera esfera = new Esfera(radio);
                System.out.println("Volumen: " + esfera.calcularVolumen());
            } else if (figura == 2) {
                System.out.print("Introduce el lado del cubo: ");
                double lado = sc.nextDouble();
                Cubo cubo = new Cubo(lado);
                System.out.println("Volumen: " + cubo.calcularVolumen());
            }
        } else if (opcion == 3) {
            System.out.println("Saliendo...");
        }
    }
}
