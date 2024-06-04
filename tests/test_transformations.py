from pytest import mark, raises, skip

from matrices.transforms import Transform
from tuples.point import Point
from tuples.vector import Vector

def test_Multiplying_by_a_translation_matrix():
    transform = Transform.translation(5, -3, 2)
    p = Point(-3, 4, 5)
    assert transform * p == Point(2, 1, 7)

def test_Multiplying_by_the_inverse_of_a_translation_matrix():
    transform = Transform.translation(5, -3, 2)
    inv = transform.inverse()
    p = Point(-3, 4, 5)
    assert inv * p == Point(-8, 7, 3)

def test_Translation_does_not_affect_vectors():
    transform = Transform.translation(5, -3, 2)
    v = Vector(-3, 4, 5)
    assert transform * v == v
