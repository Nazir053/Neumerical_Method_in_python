def false_position(x_lower, x_upper, tol=0.0001):
    x_middle = (x_upper + x_lower) / 2
    i = 1
    while True:
        x_middle = (x_lower * func(x_upper) - x_upper * func(x_lower)) / (func(x_upper) - func(x_lower))
        if func(x_middle) == 0 or abs(x_upper - x_lower) < tol:
            return x_middle
        if func(x_middle) * func(x_lower) < 0:
            x_upper = x_middle
        else:
            x_lower = x_middle
        print("iteration = ", i, "error = ", abs(x_lower - x_upper), "position = ", x_middle)
        i = i +1

def func(x):
    return x**2 - 9

x_lower = float(input("First approximate root: "))
x_upper = float(input("Secound approximate root: "))
print(false_position(x_lower,x_upper))