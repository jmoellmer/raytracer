from tuples.point import Point
from tuples.vector import Vector
from rays.ray import Ray
from rays.intersection import Intersection
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

def test_an_intersection_encapsulates_t_and_object():
    s = SphereFactory.sphere()
    i = Intersection(3.5, s)
    assert i.t == 3.5
    assert i.object.id == s.id

def test_aggregating_intersections():
    s = SphereFactory.sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, 2)
    xs = list([i1, i2])
    assert len(xs) == 2
    xs[0].t == 1
    xs[1].t == 2

def test_intersect_sets_the_object_on_the_intersection():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = SphereFactory.sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].object.id == s.id
    assert xs[1].object.id == s.id

def test_the_hit_when_all_intersections_have_positive_t():
    s = SphereFactory.sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = list([i1, i2])
    assert i1 == Intersection.hit(xs)

def test_the_hit_when_some_intersections_have_negative_t():
    s = SphereFactory.sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(2, s)
    xs = list([i1, i2])
    assert i2 == Intersection.hit(xs)

def test_the_hit_when_all_intersections_have_negative_t():
    s = SphereFactory.sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(-2, s)
    xs = list([i1, i2])
    assert None == Intersection.hit(xs)

def test_the_hit_is_always_the_lowest_nonnegative_intersection():
    s = SphereFactory.sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = list([i1, i2, i3, i4])
    assert i4 == Intersection.hit(xs)