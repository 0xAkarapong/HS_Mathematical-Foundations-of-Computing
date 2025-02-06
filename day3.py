import math

def fixed_point_iteration(g, x0, tolerance, max_iterations):
    x_prev = x0
    for i in range(max_iterations):
        x_next = g(x_prev)
        if abs(x_next - x_prev) < tolerance:
            return x_next, i + 1, True
        x_prev = x_next
    return x_prev, max_iterations, False

def g1(x):
    return math.sqrt(x + 2)

x0_1 = 1.0
tolerance_1 = 1e-6
max_iterations_1 = 100

root_1, iterations_1, converged_1 = fixed_point_iteration(g1, x0_1, tolerance_1, max_iterations_1)
print("Function 1:")
print(f"Root: {root_1}")
print(f"Iterations: {iterations_1}")
print(f"Converged: {converged_1}")

def g2(x):
    return (x**2 - 2) / 3

x0_2 = 0.0
tolerance_2 = 1e-6
max_iterations_2 = 100

root_2, iterations_2, converged_2 = fixed_point_iteration(g2, x0_2, tolerance_2, max_iterations_2)
print("\nFunction 2:")
print(f"Root: {root_2}")
print(f"Iterations: {iterations_2}")
print(f"Converged: {converged_2}")

def g3(x):
    return 1 + x - x**2/2

x0_3 = 0.0
tolerance_3 = 1e-6
max_iterations_3 = 100

root_3, iterations_3, converged_3 = fixed_point_iteration(g3, x0_3, tolerance_3, max_iterations_3)
print("\nFunction 3:")
print(f"Root: {root_3}")
print(f"Iterations: {iterations_3}")
print(f"Converged: {converged_3}")

def g4(x):
    return x**2 - 2 * x

x0_4 = 3
tolerance_4 = 1e-6
max_iterations_4 = 100
root_4, iterations_4, converged_4 = fixed_point_iteration(g4, x0_4, tolerance_4, max_iterations_4)

print("\nFunction 4:")
print(f"Root: {root_4}")
print(f"Iterations: {iterations_4}")
print(f"Converged: {converged_4}")