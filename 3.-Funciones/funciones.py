def uno(a, b):
    a = a + 5
    b += 10
    print(a, b)
    return b


def main():
    x = 5
    y = 8
    z = uno(x, y)
    print(x, y, z)


if __name__ == "__main__":
    main()
