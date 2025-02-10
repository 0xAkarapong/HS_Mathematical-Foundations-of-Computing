import random
import numpy as np

def generate_linear_system(size):
    matrix_A = []
    for _ in range(size):
        row = [random.randint(-10, 10) for _ in range(size)]
        matrix_A.append(row)

    solution_x = list(range(1, size + 1))

    np_A = np.array(matrix_A)
    np_x = np.array(solution_x)
    np_b = np.dot(np_A, np_x)

    right_hand_side_b = np_b.tolist()

    return matrix_A, solution_x, right_hand_side_b

if __name__ == "__main__":
    system_size = 3
    A, x, b = generate_linear_system(system_size)

    print("Generated Matrix A:")
    for row in A:
        print(row)

    print("\nKnown Solution x:", x)
    print("\nRight-hand side vector b (Ax):", b)