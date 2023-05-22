def compute(bigger, smaller) -> int:
    mod = bigger % smaller
    print(str(bigger) + " = " + str(int(bigger / smaller)) + "(" + str(smaller) + ")" + " + " + str(mod))
    if (mod == 0):
        return int(smaller)
    else:
        return compute(smaller, mod)


def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    smaller = 0
    bigger = 0

    if (x == y):
        return x
    else :
        bigger = max(x, y)
        smaller = min(x, y)
    

    print("We find the gcd of " + str(bigger) + " and " + str(smaller) + " using the Euclidean Algorithm.")
    result = compute(bigger, smaller)

    print("The gcd is: ")
    print(result);

if __name__ == "__main__":
    main()