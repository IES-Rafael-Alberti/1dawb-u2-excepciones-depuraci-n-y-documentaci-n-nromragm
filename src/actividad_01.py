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
    años_cumplidos  = ""
    for i in range (1, edad + 1):
        años_cumplidos += str(i) + "\n"
    
    return años_cumplidos


def main():
    
    edad = pedir_edad("Introduzca su edad: ")

    if edad != None and edad > 0:
        print(años_cumplidos(edad))


if __name__ == "__main__":
    main()