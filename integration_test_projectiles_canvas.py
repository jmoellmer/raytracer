from tuples.point import Point
from tuples.vector import Vector, norm
from tuples.color import Color
from canvas.canvas import Canvas

import matplotlib.pyplot as plt
import numpy as np

def tick(env, proj):
    proj['position'] = proj['position'] + proj['velocity']
    proj['velocity'] = proj['velocity'] + env['gravity'] + env['wind']

def main():

    # projectile starts one unit above the origin.
    # velocity is normalized to 1 unit/tick.
    proj = {'position': Point(0, 1, 0),
            'velocity': norm(Vector(1, 1.8, 0)) * 11.25}

    # gravity -0.1 unit/tick, and wind is -0.01 unit/tick
    env = {'gravity': Vector(0, -0.1, 0),
           'wind': Vector(-0.01, 0, 0)}

    w, h = 900, 550
    canvas = Canvas(w, h)
    n_ticks = 0
    while proj['position'].y > 0:
        tick(env, proj)
        n_ticks = n_ticks + 1
        print(proj['position'])
        x = int(proj['position'].x)
        y = h - int(proj['position'].y)
        canvas.write_pixel(x, y, Color(1.0, 0.0, 0.0))

    print(f"n_ticks = {n_ticks}")

    canvas.save("/Users/jeff/Desktop/projectile.ppm", canvas.canvas_to_ppm())

if __name__ == '__main__':
    main()