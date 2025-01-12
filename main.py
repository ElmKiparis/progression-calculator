def main():

    print("Kryzhanovskyi Oleksandr")

    a1 = float(input("Enter a1: "))
    diff = float(input("Enter diff: "))
    n = int(input("Enter n: "))

    an = a1 + (n - 1) * diff

    summa = ((a1 + an) / 2) * n

    print(f"Summa from a1 to a{n}: {summa}.")


if __name__ == '__main__':
    main()
