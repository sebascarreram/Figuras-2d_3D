package control;

import java.util.Scanner;

public class ValidadorEntrada {
    public int validarNumero() {
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();
        return numero;
    }

    public int validarOpcion() {
        Scanner sc = new Scanner(System.in);
        int opcion = sc.nextInt();
        return opcion;
    }
}
