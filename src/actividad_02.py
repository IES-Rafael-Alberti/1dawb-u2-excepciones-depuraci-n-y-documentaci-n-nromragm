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
    resultado = f"Numeros impares hasta {numero}:\n"

    for i in range (1, numero + 1, 2):
        if i != 1:
            resultado += ", "
        
        resultado += str(i)
    
    return resultado

def main():
    
    numero = pedir_numero()

    if numero != None and numero > 0:
        print(numeros_impares(numero))


if __name__ == "__main__":
    main()