from pytest import mark, raises, skip

from rays.ray import Ray
from tuples.point import Point
from tuples.vector import Vector
from shapes.sphere import SphereFactory
from matrices.matrix import Matrix
from matrices.transforms import Transform

def test_a_ray_intersects_a_sphere_at_two_points():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0

def test_a_ray_intersects_a_sphere_at_a_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == 5.0
    assert xs[0].t == 5.0

def test_a_ray_misses_a_sphere():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 0

def test_a_ray_originates_inside_a_sphere():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == -1.0
    assert xs[1].t == 1.0

def test_a_sphere_is_behind_a_ray():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == -6.0
    assert xs[1].t == -4.0

def test_a_spheres_default_transformation():
    s = SphereFactory.sphere()
    assert s.transform == Matrix.identity(4)

def teat_changing_a_spheres_transformation():
    s = SphereFactory.sphere()
    t = Transform.translate(2, 3, 4)
    s.transform = t
    assert s.transform == t

def test_intersecting_a_scald_sphere_with_a_ray():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    s.transform = Transform.scale(2, 2, 2)
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7

def test_intersecting_a_translated_sphere_with_a_ray():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    s.transform = Transform.translate(5, 0, 0)
    xs = r.intersect(s)
    assert len(xs) == 0

