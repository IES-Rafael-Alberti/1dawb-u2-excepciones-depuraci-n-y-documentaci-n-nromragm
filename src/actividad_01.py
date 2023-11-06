def pedir_edad(msj: str) -> int:
    """Solicita una edad

    Args:
        msj (str): mensaje que se muestra en consola para solicitar la edad.
    
    Returns:
        int: edad introducida por el usuario.
    """

    # Inicializar a None para no retornar un número si se produjo un error    
    edad = None
    salir = False
    while not salir:
        try:
            edad = int(input(msj))
            
            if edad < 0: raise ValueError("Edad no puede ser negativa")
            
            else:    
                salir = True

        except ValueError as e:
            print("ERROR", e)

    return edad

def años_cumplidos(edad):

    resultado = None
    
    print("Años que has cumplido: ")
    
    for i in range (1, edad + 1):
        resultado = print(i)

    return resultado    


def main():
    
    edad = pedir_edad("Introduzca su edad: ")

    if edad != None and edad > 0:
      años_cumplidos(edad)


if __name__ == "__main__":
    main()