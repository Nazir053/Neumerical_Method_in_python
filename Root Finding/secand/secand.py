def secant(f, x0, x1, epsilon=1e-10, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < epsilon:
            return x2
        x0, x1 = x1, x2
    return x2
def f(x):
    return x**3 - 5*x + 1

x0 = 0 # initial guess 1
x1 = 1 # initial guess 2
root = secant(f, x0, x1)
print(root)
