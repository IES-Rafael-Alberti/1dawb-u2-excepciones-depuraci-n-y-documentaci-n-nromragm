def ordenar_burbuja(lista):

    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista            


def main():
    a = [8, 3, 1, 19, 14]
    ordenar_burbuja(a)
    print("Lista ordenada de menor a mayor:", a)

if __name__ == "__main__":
    main()  