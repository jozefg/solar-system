from collections import namedtuple
import copy
from visual import vector, mag


# Time between simulation steps, this should
# be tweaked as we go.
TIME_STEP = 60 * 60 * 12 # Half a day in seconds

# mass is in kg and distance is in meters.
SolarObject = namedtuple('SolarObject', ['mass', 'velocity', 'pos'])

# At the center is
sun = SolarObject(1.988 * 10e30, vector(0, 0, 0), vector(0, 0, 0))

# The planets
mercury = SolarObject(mass     = 3.301 * 10e23,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 6.751 * 10e10, 0))

venus   = SolarObject(mass     = 4.873 * 10e24,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 1.088 * 10e11, 0))

earth   = SolarObject(mass     = 5.972 * 10e24,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 1.475 * 10e11, 0))

mars    = SolarObject(mass     = 6.417 * 10e23,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 2.068 * 10e11, 0))

jupiter = SolarObject(mass     = 1.898 * 10e27,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 7.943 * 10e11, 0))

saturn  = SolarObject(mass     = 5.683 * 10e26,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 1.481 * 10e12, 0))

uranus  = SolarObject(mass     = 8.681 * 10e25,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 2.997 * 10e12, 0))

neptune = SolarObject(mass     = 1.024 * 10e26,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 4.492 * 10e12, 0))

# TODO the asteroids

# All together
solar_system = [sun,
                mercury,
                venus,
                mars,
                jupiter,
                saturn,
                uranus,
                neptune]

def momentum(planet):
    '''calculate the momentum for a given planet'''
    return planet.mass * planet.velocity

def update_velocity(planet, dt, force):
    '''Update a planet's velocity component after being acted on by
       a force for t, seconds'''
    new_mom = force * dt + momentum(planet)
    planet.velocity = new_mom / planet.mass

def mag_gravity(a, b):
    '''Magnitude of gravity between a and b. Since gravity is always attractive
    we can easily calculuate the force on a with norm(b - a) and symmetrically
    for b'''

    G = 6.67 * 10e-11
    dist = mag(a.pos - b.pos)**2
    if dist == 0:
        return 0 # The objects were the same
    else:
        G * a.mass * b.mass / (1.0 * dist)

def arr(a, b):
    '''The unit vector starting at a.pos and ending at b.pos'''
    return norm(a.pos - b.pos)

def gravity_on(planet):
    '''Sum of all the gravitational forces on a planet from everything
    else in the solar system'''
    return sum(mag_gravity(planet, op) * arr(planet, op) for op in planets)

def step_planet(planet):
    '''Step a planet by the time step'''
    update_velocity(planet, TIME_STEP, gravity_on(planet))

def step_solar_system():
    new_solar_system = []
    for planet in solar_system:
        new_planet = copy.deepcopy(planet)
        step_planet(new_planet)
        new_solar_system.append(planet)
    solar_system = new_solar_system
