def leer_entero(mensaje: str) -> int:
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        try:
            valor = int(entrada)
            if valor < 0:
                print("No se permiten numeros negativos. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print(f"'{entrada}' no es un numero entero valido. Intenta de nuevo.")

def leer_float(mensaje: str) -> float:
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        try:
            valor = float(entrada)
            if valor < 0:
                print("No se permiten numeros negativos. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print(f"'{entrada}' no es un numero decimal valido. Intenta de nuevo.")
