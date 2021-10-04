def lectura_archivo(nombre):
    f = open(nombre, "r")
    lista = []
    for elem in f:
        lista1 = elem.split(",")
        lista.append(lista1)
    f.close()
    return lista


def main():
    res = lectura_archivo("covidmx_reducido.csv")
    print(res)


if __name__ == "__main__":
    main()
