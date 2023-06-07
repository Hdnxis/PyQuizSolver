import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples
num_samples = 1000000
pi_estimate = monte_carlo_pi(num_samples)
pi_rounded = round(pi_estimate, 2)
print("输出计算的结果):", pi_rounded)