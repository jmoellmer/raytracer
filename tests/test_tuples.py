from pytest import mark, raises, skip
from math import sqrt

from tuples.tuple import Tuple
from tuples.point import Point, is_point
from tuples.vector import Vector, is_vector, magnitude, norm, dot, cross
from tuples.color import Color

# Tuples

def test_a_tuple_with_w_1_is_a_point():
    a = Tuple(4.3, -4.2, 3.1, 1.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 1.0
    assert is_point(a) == True
    assert is_vector(a) == False

def test_a_tuple_with_w_0_is_a_vector():
    a = Tuple(4.3, -4.2, 3.1, 0.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 0.0
    assert is_point(a) == False
    assert is_vector(a) == True

def test_point_creates_tuples_with_w_1():
    assert Point(4, -4, 3) == Tuple(4, -4, 3, 1)

def test_vector_creates_tuples_with_w_0():
    assert Vector(4, -4, 3) == Tuple(4, -4, 3, 0)

# Operations

def test_adding_two_tuples():
    assert Tuple(3, -2, 5, 1) + Tuple(-2, 3, 1, 0) == Tuple(1, 1, 6, 1)

def test_subtracting_two_points():
    assert Point(3, 2, 1) - Point(5, 6, 7) == Vector(-2, -4, -6)

def test_subtracting_a_vector_from_a_point():
    assert Point(3, 2, 1) - Vector(5, 6, 7) == Point(-2, -4, -6)

def test_subtracting_two_vectors():
    assert Vector(3, 2, 1) - Vector(5, 6, 7) == Vector(-2, -4, -6)

def test_subtracting_a_vector_from_the_zero_vector():
    assert Vector(0, 0, 0) - Vector(1, -2, 3) == Vector(-1, 2, -3)

def test_negating_a_tuple():
    a = Tuple(1, -2, 3, -4)
    assert -a == Tuple(-1, 2, -3, 4)

def test_multiplying_a_tuple_by_a_scalar():
    a = Tuple(1, -2, 3, -4)
    b = Tuple(3.5, -7, 10.5, -14)
    assert 3.5 * a == b
    assert a * 3.5 == b

def test_multiplying_a_tuple_by_a_fraction():
    a = Tuple(1, -2, 3, -4)
    b = Tuple(0.5, -1, 1.5, -2)
    assert 0.5 * a == b
    assert a * 0.5 == b

def test_dividing_a_tuple_by_a_scalar():
    a = Tuple(1, -2, 3, -4)
    assert a / 2 == Tuple(0.5, -1, 1.5, -2)

def test_computing_the_magnitude_of_vector_1_0_0():
    assert magnitude(Vector(1, 0, 0)) == 1

def test_computing_the_magnitude_of_vector_0_0_1():
    assert magnitude(Vector(0, 0, 1)) == 1

def test_computing_the_magnitude_of_vector_1_2_3():
    assert magnitude(Vector(1, 2, 3)) == sqrt(14)

def test_computing_the_magnitude_of_vector_neg_1_2_3():
    assert magnitude(Vector(-1, -2, -3)) == sqrt(14)

def test_normalizing_vector_4_0_0_gives_1_0_0():
    assert norm(Vector(4, 0, 0)) == Vector(1, 0, 0)

def test_normalizing_vector_1_2_3():
    assert norm(Vector(1, 2, 3)) == Vector(1 / sqrt(14), 
                                           2 / sqrt(14),
                                           3 / sqrt(14))
    
def test_magnitude_of_a_normalized_vector():
    assert magnitude(norm(Vector(1, 2, 3))) == 1

def test_dot_product_of_two_tuples():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert dot(a, b) == 20

def test_cross_product_of_two_vectors():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert cross(a, b) == Vector(-1, 2, -1)
    assert cross(b, a) == Vector(1, -2, 1)

# Colors

def test_colors_are_red_green_blue_tuples():
    c = Color(-0.5, 0.4, 1.7)
    assert c.r == -0.5
    assert c.g == 0.4
    assert c.b == 1.7

def test_adding_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 + c2 == Color(1.6, 0.7, 1.0)

def test_subtracting_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 - c2 == Color(0.2, 0.5, 0.5)

def test_multiplying_a_color_by_a_scalar():
    c = Color(0.2, 0.3, 0.4)
    assert c * 2 == Color(0.4, 0.6, 0.8)

def test_multiplying_colors():
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)
    assert c1 * c2 == Color(0.9, 0.2, 0.04)