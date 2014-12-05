#!/usr/bin/env python
from sys import argv
import attrdict
import copy
from visual import vector, mag, sphere, color, display, norm, rate

CHANGE_FACTOR = int(argv[1])

# Time between simulation steps, this should
# be tweaked as we go.
TIME_STEP_IN_DAYS = 2
TIME_STEP = 60 * 60 * TIME_STEP_IN_DAYS * 24 # Half a day in seconds

# Radius to render everything with
RADIUS = 1e9

def SolarObject(mass, velocity, pos):
    s = attrdict.AttrDict(pos = pos,
                          radius = RADIUS)
    s.mass = mass
    s.velocity = velocity
    return s

def shadow_planet(planet):
    return attrdict.AttrDict(pos = vector(0, 0, 0) + planet.pos,
                             velocity = planet.velocity,
                             mass = planet.mass)

# At the center is
sun = SolarObject(1.988 * 1e30, vector(0, 0, 0), vector(0, 0, 0))

# The planets
mercury = SolarObject(mass     = 3.301 * 1e23,
                      velocity = vector(21414.0, 41456.0, 0),
                      pos      = vector(5.094 * 1e10, -3.0535 * 1e10))

venus   = SolarObject(mass     = 4.873 * 1e24,
                      velocity = vector(19264.98, 28973.0, 0),
                      pos      = vector(8.254 * 1e10, -7.105 * 1e10, 0))

earth   = SolarObject(mass     = 5.972 * 1e24,
                      velocity = vector(-30076.14, 3370.27, 0),
                      pos      = vector(-2.607 * 1e10, 1.448 * 1e11))

mars    = SolarObject(mass     = 6.417 * 1e23,
                      velocity = vector(5844.4426, 25796.73, 0),
                      pos      = vector(2.0318 * 1e11, -3.982 * 1e10, 0))

jupiter = SolarObject(mass     = 1.898 * 1e27,
                      velocity = vector(-6675.818225, -6066.214399, 0),
                      pos      = vector(-5.587 * 1e11, 5.54 * 1e11, 0))

saturn  = SolarObject(mass     = 5.683 * 1e26,
                      velocity = vector(8046.449, -4596.41),
                      pos      = vector(-7.88 * 1e11, -1.26 * 1e12, 0))

uranus  = SolarObject(mass     = 8.681 * 1e25,
                      velocity = vector(-1414.298, 6378.353, 0),
                      pos      = vector(2.8717 * 1e12, 8.18 * 1e11, 0))

neptune = SolarObject(mass     = 1.024 * 1e26,
                      velocity = vector(2343.522, 4929.30, 0),
                      pos      = vector(4.1226 * 1e12, -1.73977e12))

# WHOA the asteroids
ceres   = SolarObject(mass     = 9.47 * 1e20,
                      velocity = vector(17517.03472, 783.533378, 0),
                      pos      = vector(-5.24375 * 1e10, -4.19203 * 1e11, 0))

vesta   = SolarObject(mass     = 2.59 * 1e20,
                      velocity = vector(15130.68296, -8743.800155, 0),
                      pos      = vector(-2.89288 * 1e11, -3.10549 * 1e11, 0))

pallas  = SolarObject(mass     = 2.11 * 1e20,
                      velocity = vector(19343.85281, 7928.782748, 0),
                      pos      = vector(9.89643 * 1e10, -3.11221 * 1e11, 0))

# All together
solar_system = [sun,
                mercury,
                venus,
                earth,
                mars,
                jupiter,
                saturn,
                uranus,
                neptune,
                ceres,
                vesta,
                pallas]


def momentum(planet):
    '''calculate the momentum for a given planet'''
    return planet.mass * planet.velocity

def update_velocity(planet, dt, force):
    '''Update a planet's velocity component after being acted on by
       a force for t, seconds'''
    new_mom = (dt * force) + momentum(planet)
    planet.velocity = new_mom / planet.mass

def update_pos(planet, dt):
    '''Update a planet's position after dt seconds with its new velocity'''
    planet.pos = planet.pos + planet.velocity * dt

def mag_gravity(a, b):
    '''Magnitude of gravity between a and b. Since gravity is always
    attractive we can easily calculuate the force on a with norm(b -
    a) and symmetrically for b

    '''

    G = -6.67 * 1e-11
    dist = mag(a.pos - b.pos)**2
    if dist == 0:
        return 0 # The objects were the same
    else:
        return (G * a.mass * b.mass) / (1.0 * dist)

def arr(a, b):
    '''The unit vector starting at a.pos and ending at b.pos'''
    return norm(a.pos - b.pos)

def gravity_on(planet):
    '''Sum of all the gravitational forces on a planet from everything
    else in the solar system'''
    forces = (mag_gravity(planet, o) * arr(planet, o) for o in solar_system)
    return sum(forces, vector(0, 0, 0))

def step_planet(planet):
    '''Step a planet by the time step'''
    force = gravity_on(planet)
    update_velocity(planet, TIME_STEP, force)
    update_pos(planet, TIME_STEP)

def step_solar_system():
    shadow_system = []
    for planet in map(shadow_planet, solar_system):
        step_planet(planet)
        shadow_system.append(planet)
    for (planet, shadow) in zip(solar_system, shadow_system):
        planet.pos = shadow.pos
        planet.velocity = shadow.velocity

def is_closed():
    for planet in solar_system:
        if mag(planet.pos) > 6e12:
            return False
    return True

def is_stable():
    for a in [ceres, vesta, pallas]:
        dist = mag(a.pos)
        if dist < 1.1e11 or dist > 8.2e11:
            exit(1)
    return True


t = 0
neptune_orbit = 365 * 166 # 166 years

while is_stable() and t < neptune_orbit:
    t += TIME_STEP_IN_DAYS
    step_solar_system()
