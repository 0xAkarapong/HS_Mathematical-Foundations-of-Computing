eps = 1e-10

def f(x):
    return x**2 - 5*x + 4

def f_prime(x):
    return 2*x - 5

def newton_raphson(x0, f, f_prime, eps, max_iter=100):
    def iterate(i, prev_x):
        print(f"{i}-th iteration: x = {prev_x}")
        x = prev_x - f(prev_x) / f_prime(prev_x)
        if abs(x - prev_x) < eps or i >= max_iter:
            return i, x
        else:
            return iterate(i + 1, x)

    i, result = iterate(0, x0)
    print(f"It took {i} iterations to find root in precision of {eps}")
    return result

initial_x = 500000
root = newton_raphson(initial_x, f, f_prime, eps)