import random
import numpy as np

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

def jacobi_iteration_method(A, b, x0, max_iterations=10, tolerance=1e-6, big_distance=1e-2):
    n = len(b)
    x = x0.copy()
    x_prev = x0.copy()
    converged = False
    for k in range(max_iterations):
        print(f"Jacobi Iteration {k+1}: {x}")
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
            print(f"Jacobi stopping early due to big distance: {norm_change}")
            break
        x_prev = x.copy()
    return x, k + 1, converged

def gauss_seidel_iteration_method(A, b, x0, max_iterations=10, tolerance=1e-6, big_distance=1e-2):
    n = len(b)
    x = x0.copy()
    x_prev = x0.copy()
    converged = False
    for k in range(max_iterations):
        print(f"Gauss-Seidel Iteration {k+1}: {x}")
        for i in range(n):
            summation = 0
            for j in range(i):
                summation += A[i, j] * x[j]
            for j in range(i + 1, n):
                summation += A[i, j] * x_prev[j]
            x[i] = (b[i] - summation) / A[i, i]
        norm_change = np.linalg.norm(x - x_prev)
        if norm_change < tolerance:
            converged = True
            break
        if norm_change > big_distance:
            print(f"Gauss-Seidel stopping early due to big distance: {norm_change}")
            break
        x_prev = x.copy()
    return x, k + 1, converged

def main():
    dimensions = [3, 5, 10, 20]
    print("Testing Jacobi and Gauss-Seidel on Diagonally Dominant Systems")
    for n in dimensions:
        print(f"\n--- Dimension: {n} ---")
        A, b, x_exact = generate_diagonally_dominant_slr(n)
        print("Exact solution:", x_exact)
        x0 = generate_initial_approximation(x_exact)
        print("Initial approximation:", x0)
        
        x_jacobi, iter_jacobi, conv_jacobi = jacobi_iteration_method(A, b, x0, max_iterations=10)
        print(f"Jacobi: Final approximation after {iter_jacobi} iterations: {x_jacobi}, Converged: {conv_jacobi}")
        
        x_gs, iter_gs, conv_gs = gauss_seidel_iteration_method(A, b, x0, max_iterations=10)
        print(f"Gauss-Seidel: Final approximation after {iter_gs} iterations: {x_gs}, Converged: {conv_gs}")

    print("\nTesting Gauss-Seidel on Hilbert Systems")
    for n in dimensions:
        print(f"\n--- Hilbert Matrix Dimension: {n} ---")
        H, b, x_exact = generate_hilbert_system(n)
        print("Exact solution:", x_exact)
        x0 = generate_initial_approximation(x_exact)
        print("Initial approximation:", x0)
        
        x_gs, iter_gs, conv_gs = gauss_seidel_iteration_method(H, b, x0, max_iterations=50, tolerance=1e-8)
        print(f"Gauss-Seidel (Hilbert): Final approximation after {iter_gs} iterations: {x_gs}, Converged: {conv_gs}")

if __name__ == "__main__":
    main()


