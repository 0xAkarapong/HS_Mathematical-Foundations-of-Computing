import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def f(x):
    return x**4 + x**3 * 3 + x**2 - 2 * x - 0.5

def bisection_interval_subdivisions(a, b, iterations=1000000, tolerance=1e-6) -> list:
    roots = []
    if f(a) * f(b) >= 0:
        return roots

    for _ in range(iterations):
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            roots.append(c)
            return roots

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return roots


def bisection_interval_subdivisions_with_history(a, b, iterations=100, tolerance=1e-6) -> list:
    approximations = []
    if f(a) * f(b) >= 0:
        return approximations

    current_a = a # Keep track of interval boundaries for animation
    current_b = b

    for _ in range(iterations):
        c = (current_a + current_b) / 2
        approximations.append(c)
        if abs(f(c)) < tolerance:
            return approximations

        if f(current_a) * f(c) < 0:
            current_b = c
        else:
            current_a = c
    return approximations


def visualize_bisection(a_init, b_init, approximations, root_value=None):
    fig, ax = plt.subplots()
    x = np.linspace(a_init - 0.5, b_init + 0.5, 400)
    ax.plot(x, f(x), label='f(x)')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Bisection Algorithm Convergence')
    ax.set_ylim([-2, 2])

    interval_line, = ax.plot([], [], 'r-', linewidth=2, label='Interval')
    center_point, = ax.plot([], [], 'go', label='Approximation')
    root_point, = ax.plot([], [], 'bo', label='Root' if root_value is not None else None, markersize=8)
    iteration_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    legend = ax.legend(loc='upper right') # Explicitly create legend

    current_a = a_init # Keep track of interval boundaries for animation
    current_b = b_init

    def animate(i):
        nonlocal current_a, current_b # Allow modification of outer scope variables

        frame_pause_iterations = 3 # Number of frames to pause on the first iteration

        if i < frame_pause_iterations: # First few frames - show initial state
            iteration_index = 0 # Show the state for the 0th iteration (initial interval)
        elif i < len(approximations) + frame_pause_iterations: # Normal animation frames
            iteration_index = i - frame_pause_iterations + 1 # Adjust index to start from the 1st approximation
        else:
            iteration_index = len(approximations) # Show final state for extra frames


        if iteration_index < len(approximations):
            c = approximations[iteration_index]

            if iteration_index > 0: # Interval update starts from the second iteration (index 1)
                if f(a_init) * f(c) < 0: # Using a_init to keep original interval sign
                    current_b = c
                else:
                    current_a = c

            interval_line.set_data([current_a, current_b], [0, 0])
            center_point.set_data([c], [f(c)])
            iteration_text.set_text(f'Iteration: {iteration_index+1}, Approximation: {c:.6f}') #iteration_index + 1 for display
            if root_value is not None:
                root_point.set_data([root_value], [0])
            return interval_line, center_point, iteration_text, root_point if root_value is not None else root_point, legend
        else: # For last frame keep the final state
            return interval_line, center_point, iteration_text, root_point if root_value is not None else root_point, legend


    num_pause_frames = 10 # Number of frames to pause at the beginning (beyond initial frame)
    ani_frames = len(approximations) + num_pause_frames + 5 # Total frames, including pauses and extra ending frames
    ani = animation.FuncAnimation(fig, animate, frames=ani_frames, repeat=False, blit=True)
    ani.save('bisection_convergence_paused_start.mp4', writer='ffmpeg', fps=1) # Slower video, fps=1
    plt.show()


# Example Usage:
a_initial = -1.0
b_initial = 0.0
approximations_history = bisection_interval_subdivisions_with_history(a_initial, b_initial, iterations=20)

if approximations_history:
    # For better visualization, we can try to find a root with higher precision first to show as a target.
    # This is just for visual reference in the animation.
    precise_roots = bisection_interval_subdivisions(a_initial, b_initial, iterations=1000, tolerance=1e-9)
    root_value_for_vis = precise_roots[0] if precise_roots else None

    visualize_bisection(a_initial, b_initial, approximations_history, root_value=root_value_for_vis)
else:
    print("No root found in the initial interval or invalid interval.")


print("Approximations for each iteration:", approximations_history)