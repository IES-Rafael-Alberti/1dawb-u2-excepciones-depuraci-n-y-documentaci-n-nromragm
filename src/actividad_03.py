from actividad_02 import pedir_numero

def cuenta_atras(numero):
    print(f"Cuenta atras hasta 0 desde {numero}:", end=" ")
    
    while numero >= 0:
        if numero != 0:
            print(numero, end=", ")
        
        else:
            print(numero, end=".")
        numero -= 1  
    

def main():
    
    numero = pedir_numero()
    
    cuenta_atras(numero)


if __name__ == "__main__":
    main()