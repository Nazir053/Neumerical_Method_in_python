#find root of x ** 3 - 5 * x + 1 using bisection
def f(x):
    return x ** 3 - 5 * x + 1


def bisection(a, b, n):
    i = 1
    while i <= n:
        x = (a + b) / 2
        if f(x) < 0:
            a = x
        else:
            b = x
        print("iteration = ", i, "\t x = ", x, "\t f(x) = ", f(x))
        i = i+1
    return x


a = float(input("First approximate root: "))
b = float(input("Secound approximate root: "))
n = int(input("Number of itaration: "))

if f(a) * f(b) > 0:
    print("Given approximate value are not baraket the root. \n Try "
          "again with different value")
else:
    bisection(a, b, n)
