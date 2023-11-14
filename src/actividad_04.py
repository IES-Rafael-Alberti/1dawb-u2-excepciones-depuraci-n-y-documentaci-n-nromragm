def pedir_numero():
    numero = None

    try:
        numero = int(input("Introduze un numero entero: "))

    except ValueError as e:
        print(f"La entrada no es correcta \n{e}")

    return numero


def main():
    
    numero = pedir_numero()

    if numero != None:

        print(numero)


if __name__ == "__main__":
    main()