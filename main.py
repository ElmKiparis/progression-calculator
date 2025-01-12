def get_an(a1, diff, n):
    return a1 + (n - 1) * diff


def get_summa(a1, an, n):
    return ((a1 + an) / 2) * n


def main():

    print("Kryzhanovskyi Oleksandr")

    a1 = float(input("Enter a1: "))
    diff = float(input("Enter diff: "))
    n = int(input("Enter n: "))

    summa = get_summa(a1, get_an(a1, diff, n), n)

    print(f"Summa from a1 to a{n}: {summa}.")


if __name__ == '__main__':
    main()
