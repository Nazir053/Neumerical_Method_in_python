def newton_raphson(f, df, x0, epsilon=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        x1 = x - f(x) / df(x)
        if abs(x1 - x) < epsilon:
            return x1
        x = x1
    return x

def f(x):
    return x**3 - 5*x + 1

def df(x):
    return 3*x**2 - 5

x0 = 1 # initial guess
root = newton_raphson(f, df, x0)
print(root)

