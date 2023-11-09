def pedir_password():
    contraseña_usuario = input("Ingresa la contraseña: ")
    
    return contraseña_usuario


def validar_password(contraseña_usuario):

    contraseña = "contraseña"
    resultado = ""

    try:
        if contraseña != contraseña_usuario.lower():
            raise NameError("Incorrect Password!!")
        else:
            resultado = "Contraseña correcta"
        
    except NameError as e:
        print(e)
    
    return resultado



def main():
    contraseña_usuario = pedir_password()
    
    print(validar_password(contraseña_usuario))


if __name__ == "__main__":
    main()