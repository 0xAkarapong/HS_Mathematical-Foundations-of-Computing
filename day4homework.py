import matplotlib.pyplot as plt
import numpy as np

# Define the functions and their derivatives
def f(x):
    return (x - 1)**3 # From Google classroom

def f_prime(x):
    return 3 * (x - 1)**2 # From Google Classroom

# Root-finding algorithms (Newton and Bisection)
def find_root_newton(f, f_prime, x0, num_iter):
    x_vals = []
    it = 0
    for i in range(num_iter):
        x_vals.append(x0)
        try:
            x0 = x0 - f(x0) / f_prime(x0)
        except ZeroDivisionError:
            print("Zero division error in Newton's method. Stopping.")
            break
        it += 1
    return x0, it, x_vals


def find_root_bisect(f, a, b, num_iters):
    x_vals = []
    if f(a) * f(b) > 0:
        print("No root found")
        return 0,0,0
    else:
        it = 0
        while it < num_iters:
            c = (a + b) / 2
            x_vals.append(c)
            if f(c) == 0:
                return c, it, x_vals
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            it += 1
        return (a + b) / 2, it, x_vals

# Configuration
a = 0.5 #Bisection interval start
b = 3 #Bisection interval end
newton_x0 = -5 #Newton starting point
num_iter = 50 #Number of iterations
real_solution = 1 # Known solution

# Run algorithms
newton_c, newton_it, newton_x_vals = find_root_newton(f, f_prime, newton_x0, num_iter)
bisect_c, bisect_it, bisect_x_vals = find_root_bisect(f, a, b, num_iter)

# Calculate errors
newton_it_nums = [i for i in range(newton_it)]
newton_err_values = [abs(x - real_solution) for x in newton_x_vals]

bisect_it_nums = [i for i in range(bisect_it)]
bisect_err_values = [abs(x - real_solution) for x in bisect_x_vals]

# Print results
print(f"Newton Root: {newton_c} found in {newton_it} iterations. F(x) = {f(newton_c)}")
print(f"Bisection Root: {bisect_c} found in {bisect_it} iterations. F(x) = {f(bisect_c)}")

# Plotting
fig, ax = plt.subplots()
ax.plot(newton_it_nums, newton_err_values, label="Newton")
ax.plot(bisect_it_nums, bisect_err_values, label="Bisect")
ax.set_yscale('log')
ax.set_title("Error on each step")
ax.set_xlabel("Iteration")
ax.set_ylabel("Error")
ax.legend()
plt.show()