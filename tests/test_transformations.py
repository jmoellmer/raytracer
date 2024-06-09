from pytest import mark, raises, skip

import math

from matrices.transforms import Transform
from tuples.point import Point
from tuples.vector import Vector

def test_Multiplying_by_a_translation_matrix():
    transform = Transform.translate(5, -3, 2)
    p = Point(-3, 4, 5)
    assert transform * p == Point(2, 1, 7)

def test_Multiplying_by_the_inverse_of_a_translation_matrix():
    transform = Transform.translate(5, -3, 2)
    inv = transform.inverse()
    p = Point(-3, 4, 5)
    assert inv * p == Point(-8, 7, 3)

def test_Translation_does_not_affect_vectors():
    transform = Transform.translate(5, -3, 2)
    v = Vector(-3, 4, 5)
    assert transform * v == v

def test_A_scaling_matrix_applied_to_a_point():
    transform = Transform.scale(2, 3, 4)
    p = Point(-4, 6, 8)
    assert transform * p == Point(-8, 18, 32)

def test_A_scaling_matrix_applied_to_a_vector():
    transform = Transform.scale(2, 3, 4)
    v = Vector(-4, 6, 8)
    assert transform * v == Vector(-8, 18, 32)

def test_Multiplying_by_the_inverse_of_a_scaling_matrix():
    transform = Transform.scale(2, 3, 4)
    inv = transform.inverse()
    v = Vector(-4, 6, 8)
    assert inv * v == Vector(-2, 2, 2)

def test_Reflection_is_scaling_by_a_negative_value():
    transform = Transform.scale(-1, 1, 1)
    p = Point(2, 3, 4)
    assert transform * p == Point(-2, 3, 4)

def test_Rotating_a_point_around_the_x_axis():
    p = Point(0, 1, 0)
    half_qtr = Transform.rotate_x(math.pi / 4)
    full_qtr = Transform.rotate_x(math.pi / 2)
    assert half_qtr * p == Point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
    tmp = full_qtr * p
    assert full_qtr * p == Point(0, 0, 1)

def test_The_inverse_of_an_x_rotation_rotates_in_opposite_direction():
    p = Point(0, 1, 0)
    half_qtr = Transform.rotate_x(math.pi / 4)
    inv = half_qtr.inverse()
    assert inv * p == Point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)

def test_Rotating_a_point_around_the_y_axis():
    p = Point(0, 0, 1)
    half_qtr = Transform.rotate_y(math.pi / 4)
    full_qtr = Transform.rotate_y(math.pi / 2)
    assert half_qtr * p == Point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
    assert full_qtr * p == Point(1, 0, 0)

def test_Rotating_a_point_around_the_z_axis():
    p = Point(0, 1, 0)
    half_qtr = Transform.rotate_z(math.pi / 4)
    full_qtr = Transform.rotate_z(math.pi / 2)
    assert half_qtr * p == Point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
    assert full_qtr * p == Point(-1, 0, 0)

def test_A_shearing_transformation_moves_x_in_proportion_to_y():
    transform = Transform.shear(1, 0, 0, 0, 0, 0)
    p = Point(2, 3, 4)
    assert transform * p == Point(5, 3, 4)

def test_A_shearing_transformation_moves_x_in_proportion_to_z():
    transform = Transform.shear(0, 1, 0, 0, 0, 0)
    p = Point(2, 3, 4)
    assert transform * p == Point(6, 3, 4)

def test_A_shearing_transformation_moves_y_in_proportion_to_x():
    transform = Transform.shear(0, 0, 1, 0, 0, 0)
    p = Point(2, 3, 4)
    assert transform * p == Point(2, 5, 4)

def test_A_shearing_transformation_moves_y_in_proportion_to_z():
    transform = Transform.shear(0, 0, 0, 1, 0, 0)
    p = Point(2, 3, 4)
    assert transform * p == Point(2, 7, 4)

def test_A_shearing_transformation_moves_z_in_proportion_to_x():
    transform = Transform.shear(0, 0, 0, 0, 1, 0)
    p = Point(2, 3, 4)
    assert transform * p == Point(2, 3, 6)

def test_A_shearing_transformation_moves_z_in_proportion_to_y():
    transform = Transform.shear(0, 0, 0, 0, 0, 1)
    p = Point(2, 3, 4)
    assert transform * p == Point(2, 3, 7)

def test_Individual_transformations_are_applied_in_sequence(): 
    p = Point(1, 0, 1)
    A = Transform.rotate_x(math.pi / 2)
    B = Transform.scale(5, 5, 5)
    C = Transform.translate(10, 5, 7)
    p2 = A * p
    assert p2 == Point(1, -1, 0)
    p3 = B * p2
    assert p3 == Point(5, -5, 0)
    p4 = C * p3
    assert p4 == Point(15, 0, 7)

def test_Chained_transformations_must_be_applied_in_reverse_order():
    p = Point(1, 0, 1)
    A = Transform.rotate_x(math.pi / 2)
    B = Transform.scale(5, 5, 5)
    C = Transform.translate(10, 5, 7)
    T = C * B * A
    assert T * p == Point(15, 0, 7)
    assert T * p == C * (B * (A * p))