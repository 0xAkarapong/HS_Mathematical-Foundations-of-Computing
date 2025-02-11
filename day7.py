import random
import numpy as np
import matplotlib.pyplot as plt

def generate_diagonally_dominant_slr(n, solution_range=(-10, 10)):
    x_exact = np.array([random.uniform(solution_range[0], solution_range[1]) for _ in range(n)])
    A = np.random.rand(n, n) * 20 - 10
    for i in range(n):
        row_sum = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
        A[i, i] = row_sum + random.uniform(1, 5)
    b = np.dot(A, x_exact)
    return A, b, x_exact

def generate_hilbert_system(n):
    H = np.array([[1 / (i + j + 1) for j in range(n)] for i in range(n)])
    x_exact = np.ones(n)
    b = np.dot(H, x_exact)
    return H, b, x_exact

def generate_initial_approximation(x_exact, noise_range=(-0.5, 0.5)):
    noise = np.array([random.uniform(noise_range[0], noise_range[1]) for _ in range(len(x_exact))])
    x0 = x_exact + noise
    return x0

def jacobi_iteration_method(A, b, x0, x_exact, max_iterations=50, tolerance=1e-6):
    n = len(b)
    x = x0.copy()
    x_prev = x0.copy()
    converged = False
    error_history = []
    for k in range(max_iterations):
        for i in range(n):
            summation = 0
            for j in range(n):
                if i != j:
                    summation += A[i, j] * x_prev[j]
            x[i] = (b[i] - summation) / A[i, i]
        error = np.linalg.norm(x - x_exact)
        error_history.append(error)
        if error < tolerance:
            converged = True
            break
        # norm_change = np.linalg.norm(x - x_prev) # big_distance condition removed
        # if norm_change > big_distance:
        #     break
        x_prev = x.copy()
    return x, k + 1, converged, error_history

def gauss_seidel_iteration_method(A, b, x0, x_exact, max_iterations=50, tolerance=1e-6):
    n = len(b)
    x = x0.copy()
    x_prev = x0.copy()
    converged = False
    error_history = []
    for k in range(max_iterations):
        x_prev = x.copy()
        for i in range(n):
            summation = 0
            for j in range(n):
                if i != j:
                    summation += A[i, j] * x[j if j < i else j] # corrected index for Gauss-Seidel to use updated x
            x[i] = (b[i] - summation) / A[i, i]
        error = np.linalg.norm(x - x_exact)
        error_history.append(error)
        if error < tolerance:
            converged = True
            break
        # norm_change = np.linalg.norm(x - x_prev) # big_distance condition removed
        # if norm_change > big_distance:
        #     break
        x_prev = x.copy()
    return x, k + 1, converged, error_history

def main():
    dimensions = [3, 5, 10, 20]
    print("Testing Jacobi and Gauss-Seidel on Diagonally Dominant Systems")
    for n in dimensions:
        print(f"\n--- Dimension: {n} ---")
        A, b, x_exact = generate_diagonally_dominant_slr(n)
        print("Exact solution:", x_exact)
        x0 = generate_initial_approximation(x_exact)
        print("Initial approximation:", x0)

        x_jacobi, iter_jacobi, conv_jacobi, error_jacobi = jacobi_iteration_method(A, b, x0, x_exact, max_iterations=500, tolerance=1e-8)
        print(f"Jacobi: Final approximation after {iter_jacobi} iterations: {x_jacobi}, Converged: {conv_jacobi}")

        x_gs, iter_gs, conv_gs, error_gs = gauss_seidel_iteration_method(A, b, x0, x_exact, max_iterations=500, tolerance=1e-8)
        print(f"Gauss-Seidel: Final approximation after {iter_gs} iterations: {x_gs}, Converged: {conv_gs}")

        # Plotting convergence history
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(error_jacobi) + 1), error_jacobi, label='Jacobi', marker='o', linestyle='-')
        plt.plot(range(1, len(error_gs) + 1), error_gs, label='Gauss-Seidel', marker='x', linestyle='--')
        plt.xlabel('Iteration Number')
        plt.ylabel('Error (||x - x_exact||)')
        plt.title(f'Convergence for Diagonally Dominant System (Dimension {n})')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    main()