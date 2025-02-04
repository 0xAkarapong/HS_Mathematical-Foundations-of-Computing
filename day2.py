import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4 + x**3 * 3 + x**2 - 2 * x - 0.5

def bisection_interval_subdivisions(a, b, iterations=1000000, tolerance=1e-6) -> list:
    roots = []
    if f(a) * f(b) >= 0:
        print("Function values at endpoints do not have opposite signs in interval [",a,b,"].")
        return roots

    while iterations > 0:
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            roots.append(c)
            return roots
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations -= 1

    print("Maximum iterations reached in interval [",a,b,"].")
    return roots

def find_all_roots(start, end, step, iterations=1000000, tolerance=1e-6):
  all_roots = []
  current_interval_start = start
  while current_interval_start < end:
      current_interval_end = current_interval_start + step
      
      new_roots = bisection_interval_subdivisions(current_interval_start,current_interval_end,iterations,tolerance)
      if(len(new_roots) > 0):
        if new_roots[0] not in all_roots :
          all_roots.extend(new_roots)

      current_interval_start = current_interval_end
  return all_roots
  
all_roots_found = find_all_roots(-3, 3, 0.1)
print("All roots found:", all_roots_found)

# Plotting
x = np.linspace(-3, 3, 400)
y = f(x) 

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x^4 + 3x^3 + x^2 - 2x - 0.5')
plt.axhline(0, color='black',linewidth=0.5)  # 
plt.axvline(0, color='black',linewidth=0.5) 
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5) # Add grid

# Plot roots
for root in all_roots_found:
    plt.plot(root, 0, 'ro', label='Root' if root == all_roots_found[0] else "") 

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) and its Roots')
plt.legend()
plt.show()
