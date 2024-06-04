from pytest import mark, raises, skip

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