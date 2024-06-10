"Line-sphere intersections" article on Wikipedia (1)
"Ray-Sphere Intersection" tutorial at Lighthouse3d (2)


1. en.wikipedia.org/wiki/Line–sphere_intersection
2. www.lighthouse3d.com/tutorials/maths/ray-sphere-intersection
3. https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-sphere-intersection.html

"A Minimal Ray-Tracer" from Scratchapixel's series (3)

Ray-Sphere: simplest ray-geometry intersection test.
- Why ray tracers showcase images of spheres
- Speed

Two Methods
- Solve with geometry
- Preferred solution: analytic (or algebraic) solution

# Solve with geometry

1. Get distance (t_ca) from ray origin (O) and location between the circle's center line (d) and the ray (passing though the two intersection points (P and P')).

2. Calclate the distance between P and d (t_hc)

Then, t0 = t_ca - t_hc and t1 = t_ca + t_hc

and find P with:

    P = O + t0D
    P' = O + t1D

## First Right Triangle
## (Compute t_ca and t_hc)

There is a right triangle formed between the center of the sphere (C) and O (call it L), d, and t_ca.

L, t_ca, and d form a right triangle.

### Calculate L

L is the vector between O and C:

L = C - O
L = Point(0, 0, 0) - Point(0, 0, -5) = Vector(0, 0, 5)

Note: O == Tuple(0, 0, -5, 1) and C == Tuple(0, 0, 0, 1). Therefore,
      L = C - O = Tuple(0, 0, 5, 0) == Vector(0, 0, 5). When w == 0, it is a point. When w == 1, it is a vector.

### Calculate t_ca

We know L = Vector(0, 0, 5) and we know D = (0, 0, 1).

We also know the dot product. The dot product of L and D give us t_ca.

L = C - O
t_ca = dot(L, D)
if t_ca < 0: return False

## Second Right Triangle

Rt triangle defined by: d, t_hc, and shere's radius.

radius = 1.0

Need t_hc to find t0 and t1.

### Calculate d

d is the opposite side of the right triangle defined by d, t_ca, and L. Use (opposite)**2 + (adj)**2 == (hyp)**2

d**2 + t_ca**2 = L**2
d = sqrt(L**2 - t_ca**2)
if d < 0: return False

Note: if d is greater than the sphere's radius, the ray misses the sphere! No intersection.

### Calculate t_hc

d**2 + t_hc**2 = radius**2
t_hc = sqrt(radius**2 - d**2)
t0 = t_ca - t_ca
t1 = t_ca + t_hc

# Solve Analytically

Ray: O + tD

## Equation of the sphere

x**2 + y**2 + z**2 = R**2

Note: The set of points where this equation holds true is the surface of the sphere.

This set of points defines the surface of a sphere centered at the origin with a radius R:

P**2 - R**2 = 0

This is the "implicit function."

Now, we replace P with the Ray equation:

(O + tD)**2 - R^2 = 0

Expand the equation:

O**2 + (Dt)**2 + 2ODt - R**2 = O**2 + D**2t**2 + 2ODt - R**2 = 0

This is an equation in the form of:

ax^2 + bx + c (quadratic equation)

where a = D**2, b = 2OD, and c = O**2 - R**2

Solve the quadratic equation, the two roots are intersection points.


