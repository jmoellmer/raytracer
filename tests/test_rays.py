from tuples.point import Point
from tuples.vector import Vector
from rays.rays import Ray
from shapes.sphere import Sphere, SphereFactory

def test_creating_and_querying_a_ray():
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)
    r = Ray(origin, direction)
    assert r.origin == origin
    assert r.direction == direction

def test_computing_a_point_from_a_distance():
    r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
    assert r.position(0) == Point(2, 3, 4)
    assert r.position(1) == Point(3, 3, 4)
    assert r.position(-1) == Point(1, 3, 4)
    assert r.position(2.5) == Point(4.5, 3, 4)

def test_a_ray_intersects_a_sphere_at_two_points():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0] == 4.0
    assert xs[1] == 6.0

def test_a_ray_intersects_a_sphere_at_a_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0] == 5.0
    assert xs[0] == 5.0

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
    assert xs[0] == -1.0
    assert xs[1] == 1.0

def test_a_sphere_is_behind_a_ray():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0] == -6.0
    assert xs[1] == -4.0
