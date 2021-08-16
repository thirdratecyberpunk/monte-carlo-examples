"""
Zeroth example of Monte Carlo simulations
Utilising probabilistic calculations to estimate pi
Considering a circle of radius r = 1 inside a square of l = 2
Pi can be calculated as 4 * # (points in circle / # points)
"""

# TODO: add visualisation to this process using matplotlib

import random
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ln, = plt.plot([], [], 'ro')
x_data = []
y_data = []

def update(frame):
    # plotting circle for reference
    angle = np.linspace(0 , 2 * np.pi , 150)
    radius = 1
    circle_x = radius * np.cos(angle)
    circle_y = radius * np.sin(angle)
    ax.plot(circle_x, circle_y)
    # plotting values
    x_data.append(frame[0])
    y_data.append(frame[1])
    ln.set_data(x_data, y_data)
    return ln,

def main():
    """
    Main function that generates the visualisation
    """
    random.seed(1)
    points = 1000000
    print(f"Estimating pi with {points} points")

    # generating random points and plotting them
    points_in_circle = 0
    values = []

    for i in range(points):
        value = generate_random_point()
        values.append(value)
        x = value[0]
        y = value[1]
        if (x*x + y*y < 1):
            points_in_circle += 1

    pi_approximation = 4.0 * (points_in_circle / points)
    accuracy_pct = pi_approximation / math.pi * 100

    print(f"Calculated pi as {pi_approximation} with an accuracy of {accuracy_pct}%")

    # plotting results onto animated graph
    ani = FuncAnimation(fig, update, frames=values, interval=1, blit=True)
    # ani.save("estimating_pi.gif")
    plt.show()

def generate_random_point():
    """
    Returns a tuple of random values
    """
    x = 2.0 * random.random() - 1.0
    y = 2.0 * random.random() - 1.0
    return (x,y)

if __name__ == "__main__":
    main()
