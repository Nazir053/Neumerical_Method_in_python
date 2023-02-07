# find root of f(x) = x**3 -4*x -9 = 0 using bisection between x=1 to x=1.5 permissible error 0.01%

def f(x):
    return x **3 - 4 * x - 9


def bisection(a, b, e):
    i = 1
    x = a
    error = e + 1
    while error > e:
        g = f(x)
        x = (a + b) / 2
        if f(x) < 0:
            a = x
        else:
            b = x

        error = abs(f(x) - g)

        print("iteration = ", i, "\t x = ", x, "\t f(x) = ", f(x), "\terror = ", error)
        i = i + 1
    return x


a = float(input("First approximate root: "))
b = float(input("Secound approximate root: "))
e = float(input("permisible error: "))

if f(a) * f(b) > 0:
    print("Given approximate value are not braket the root. \n Try "
          "again with different value")
else:
    print("answare is: ", bisection(a, b, e))
