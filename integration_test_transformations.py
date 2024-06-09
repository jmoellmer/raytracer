from matrices.matrix import Matrix
from matrices.transforms import Transform
from canvas.canvas import Canvas
from tuples.point import Point
from tuples.color import Color

import math

def main():
    w, h = 101, 101
    canvas = Canvas(w, h)
    pt_color = Color(1, 1, 1)

    tweleve = Point(0, 0, 1)
    halo=2
    s = Transform.scale(w/2-halo, w/2-halo, w/2-halo)

    for i in range(0, 12):
        r = Transform.rotate_y(math.pi/6 * i)
        pt = s * r * tweleve
        x = round(max(0, pt.x + w/2 - 1))
        y = round(max(0, h - pt.z - h/2 - 1))
        canvas.write_pixel(x, y, pt_color)

    canvas.save("/Users/jeff/Desktop/clock.ppm", canvas.canvas_to_ppm())

if __name__ == "__main__":
    main()