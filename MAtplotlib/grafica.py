import matplotlib.pyplot as plt
from math import *

sqrt(5)


def graficas2(x, y):
    pass


def graficas(x, y):
    plt.title("Ejemplo de uso de Matplotlib")
    plt.xlabel("Dias del mes")
    plt.ylabel("Casos de covid")
    plt.axis([0, 5, 0, 10])  # xmin, xmax, ymin, ymax

    x2 = ["01/10/2021", " ", "03/10/2021", ""]
    plt.xticks(x, x2, rotation=75)
    plt.plot(x, y)
    plt.show()


def main():
    x = [0, 1, 2, 3]
    y = [0.5, 3, 2, 6]
    graficas(x, y)


if __name__ == "__main__":
    main()
