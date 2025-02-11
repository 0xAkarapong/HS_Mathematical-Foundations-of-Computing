import random
import numpy as np

def generate_diagonally_dominant_slr(n, solution_range=(-10, 10)):

    x_exact = np.array([random.uniform(solution_range[0], solution_range[1]) for _ in range(n)])

    A = np.random.rand(n, n) * 20 - 10  # Values between -10 and 10

    for i in range(n):
        row_sum = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
        A[i, i] = row_sum + random.uniform(1, 5) 

    b = np.dot(A, x_exact)
    return A, b, x_exact

def generate_initial_approximation(x_exact, noise_range=(-0.5, 0.5)):
    noise = np.array([random.uniform(noise_range[0], noise_range[1]) for _ in range(len(x_exact))])
    x0 = x_exact + noise
    return x0

def jacobi_iteration_method(A, b, x0, max_iterations=10, tolerance=1e-6, big_distance=1e-2):
    n = len(b)
    x = x0.copy()
    x_prev = x0.copy()
    approximations = [x]
    iterations = 0
    converged = False

    for k in range(max_iterations):
        print(f"Iteration {k+1}: {x}")
        for i in range(n):
            summation = 0
            for j in range(n):
                if i != j:
                    summation += A[i, j] * x_prev[j]
            x[i] = (b[i] - summation) / A[i, i]
        
        norm_change = np.linalg.norm(x - x_prev)
        if norm_change < tolerance:
            converged = True
            break

        if norm_change > big_distance:
            print(f"Stopping early due to big distance: {norm_change}")
            break

        x_prev = x.copy()

    return x, k + 1, converged

def main():
    dimensions = [3, 5, 10, 20]  # N dimensions to test

    for n in dimensions:
        print(f"\n--- Testing with dimension: {n} ---")

        A, b, x_exact = generate_diagonally_dominant_slr(n)
        print(f"Exact solution: {x_exact}")

        x0 = generate_initial_approximation(x_exact)
        print(f"Initial approximation: {x0}")
        x_approx, iterations, converged = jacobi_iteration_method(A, b, x0, max_iterations=10)

        print(f"Final approximation after {iterations} iterations: {x_approx}")
        print(f"Converged: {converged}")

if __name__ == "__main__":
    main()


