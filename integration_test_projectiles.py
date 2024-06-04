from tuples.point import Point
from tuples.vector import Vector, norm

import matplotlib.pyplot as plt
import numpy as np

def tick(env, proj):
    proj['position'] = proj['position'] + proj['velocity']
    proj['velocity'] = proj['velocity'] + env['gravity'] + env['wind']

def update_plot(x, y, scatter):
    scatter.set_offsets(np.c_[x, y])
    plt.draw()
    plt.pause(0.1)

def main():

    # projectile starts one unit above the origin.
    # velocity is normalized to 1 unit/tick.
    proj = {'position': Point(0, 1, 0),
            'velocity': norm(Vector(1, 1, 0))}

    # gravity -0.1 unit/tick, and wind is -0.01 unit/tick
    env = {'gravity': Vector(0, -0.1, 0),
           'wind': Vector(-0.01, 0, 0)}
    
    _, ax = plt.subplots()
    scatter = ax.scatter([], [])
    ax.set_xlim(-12, 12)
    ax.set_ylim(-1, 10)
    plt.ion()
    plt.show()

    x_values = []
    y_values = []

    n_ticks = 0
    while proj['position'].y > 0:
        tick(env, proj)
        n_ticks = n_ticks + 1
        print(proj['position'])

        x_values.append(proj['position'].x)
        y_values.append(proj['position'].y)
        update_plot(x_values, y_values, scatter)
    print(f"n_ticks = {n_ticks}")

if __name__ == '__main__':
    main()