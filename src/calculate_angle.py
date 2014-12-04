from visual import *
from attrdict import *

g = 6.6738e-11

sun = AttrDict(pos=(0,0,0), radius=1e9, mass = 1.989e30)

planet = AttrDict(pos=(4.4445e12,0,0),
                  radius = 1e9,
                  mass = 1.0242e26,
                  velocity = vector(0,5.5e3,0),
                  momentum = planet.mass * planet.velocity)

x = 4.123e12
y = -1.74e12

dt = 1e3
t = 0

while True:
    planet.force = -g * sun.mass * planet.mass / mag2(planet.pos) * norm(planet.pos)
    planet.momentum = planet.momentum + planet.force * dt
    planet.velocity = planet.momentum / planet.mass
    planet.pos = planet.pos + planet.velocity * dt

    t = t + dt

    if (diff_angle(planet.pos,vector(x,y)) < 0.05):
        break

print diff_angle(vector(1,0,0),planet.velocity)
