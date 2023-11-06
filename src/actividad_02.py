def pedir_numero():
    numero = None
    salir = False
    while not salir:
        try:
            numero = int(input("Introduze un numero entero positivo: "))

            if numero < 0: raise ValueError("El numero no puede ser negativo")
            
            else:
                salir = True
        except ValueError as e:
            print("**Error**", e)

    return numero


def numeros_impares(numero):
    print(f"Numeros impares hasta {numero}:", end=" ")

    for i in range (1, numero + 1, 2):
        if i != 1:
            print(", ", end="")
        
        print(i, end=".")    
    

def main():
    
    numero = pedir_numero()

    if numero != None and numero > 0:
        numeros_impares(numero)


if __name__ == "__main__":
    main()