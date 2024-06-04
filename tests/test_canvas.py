from pytest import mark, raises, skip
from pathlib import Path

from ..canvas.canvas import Canvas
from ..tuples.color import Color

def test_creating_a_canvas():
    c = Canvas(10, 20)
    assert sum(sum(row) for row in c._img) == 0

def test_writing_pixels_to_canvas():
    c = Canvas(10, 20)
    red = Color(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red

def test_construction_a_PPM_header():
    c = Canvas(5, 3)
    ppm = c.canvas_to_ppm()
    assert ppm == "P3\n5 3\n255\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0\n"

def test_constructing_the_PPM_image_data():
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = c.canvas_to_ppm()
    assert ppm ==  "P3\n5 3\n255\n382 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 128 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 255\n"

def test_splitting_long_lines_in_PPM_files():
    color = Color(1, 0.8, 0.6)
    c = Canvas(10, 2, color)
    ppm = c.canvas_to_ppm()
    c.save(f"{Path.home()}/Desktop/canvas.ppm", ppm)
    assert ppm ==  "P3\n10 2\n255\n\
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153\n\
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153\n\
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153\n\
255 204 153 255 204 153 255 204 153 255 204 153 255 204 153\n"

def test_PPM_files_are_terminated_by_a_newline_char():
    canvas = Canvas(5, 3)
    ppm = canvas.canvas_to_ppm()
    assert ppm[-1] == '\n'

