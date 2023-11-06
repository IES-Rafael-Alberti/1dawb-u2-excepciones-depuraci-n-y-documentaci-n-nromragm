def pedir_numero():
    numero = None

    try:
        numero = int(input("Introduze un numero entero positivo: "))

    except:
        print("El numero no es correcto")

    return numero


def main():
    
    numero = pedir_numero()

    if numero != None:

        print(numero)


if __name__ == "__main__":
    main()