from actividad_02 import pedir_numero

def cuenta_atras(numero):
    resultado = f"Cuenta atras hasta 0 desde {numero}: "
    
    while numero >= 0:
        if numero != 0:
            resultado += str(numero) + ", "
        
        else:
            resultado += str(numero)
        numero -= 1  
    return resultado

def main():
    
    numero = pedir_numero()
    
    print(cuenta_atras(numero))


if __name__ == "__main__":
    main()