"""
Zeroth example of Monte Carlo simulations
Utilising probabilistic calculations to estimate pi
Considering a circle of radius r = 1 inside a square of l = 2
Pi can be calculated as 4 * # (points in circle / # points)
"""

# TODO: add visualisation to this process using matplotlib

import random, math

def main():
    random.seed(1)
    points = 1000000
    print(f"Estimating pi with {points} points")

    points_in_circle = 0

    for i in range(points):
        x, y = generate_random_point()
        if (x*x + y*y < 1):
            points_in_circle += 1

    pi_approximation = 4.0 * (points_in_circle / points)
    accuracy_pct = pi_approximation / math.pi * 100

    print(f"Calculated pi as {pi_approximation} with an accuracy of {accuracy_pct}%")

def generate_random_point():
    """
    Returns a pair of random values
    """
    x = 2.0 * random.random() - 1.0
    y = 2.0 * random.random() - 1.0
    return x, y

if __name__ == "__main__":
    main()
