# Pseudocodigo de la solucion


def es_edad(edad):
    """Metodo que dice en que etapa de su desarrollo
    tiene una persona

    Args:
        edad ([int]): [La edad de la persona]

    Returns:
        [str]: [Etapa de desarrollo]
    """
    etapa = ""

    if edad >=0 and edad < 2:
        return "bebe"
    else:
        if edad >= 2 and edad < 4:
            return "huerco"
        else:
            if edad >= 4 and edad < 13:
                return "chico"
            else:
                if edad >= 13 and edad < 20:
                    return "adolescente"
                else:
                    if edad >= 20 and edad < 65:
                        return "adulto"
                    else:
                        if edad >= 65:
                            return "adulto mayor"
                        else:
                            return "Error"    


def main():
    f = open("edades.csv", "r")
    for edad in f:
        print(es_edad(int(edad)))


if __name__ == "__main__":
    main()
