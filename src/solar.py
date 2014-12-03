import attrdict
import copy
from visual import vector, mag, sphere, color, display, norm

# Time between simulation steps, this should
# be tweaked as we go.
TIME_STEP = 60 * 60 * 12 # Half a day in seconds

# Radius to render everything with
RADIUS = 6.955 * 10e8

scene = display(title = "Solar System", width = 600,
                height = 600, range = 40 * RADIUS)
scene.autoscale = 0 # Turn off auto scaling.

def SolarObject(mass, velocity, pos):
    s = sphere(pos = pos,
               radius = RADIUS,
               color = color.red)
    s.mass = mass
    s.velocity = velocity
    return s

def shadow_planet(planet):
    return attrdict.AttrDict(pos = planet.pos,
                             velocity = planet.velocity,
                             mass = planet.mass)

# At the center is
sun = SolarObject(1.988 * 10e30, vector(0, 0, 0), vector(0, 0, 0))

# The planets
mercury = SolarObject(mass     = 3.301 * 10e23,
                      velocity = vector(58000.98, 0, 0),
                      pos      = vector(0, 6.751 * 10e10, 0))

venus   = SolarObject(mass     = 4.873 * 10e24,
                      velocity = vector(35000.26, 0, 0),
                      pos      = vector(0, 1.088 * 10e11, 0))

earth   = SolarObject(mass     = 5.972 * 10e24,
                      velocity = vector(30000.29, 0, 0),
                      pos      = vector(0, 1.475 * 10e11, 0))

mars    = SolarObject(mass     = 6.417 * 10e23,
                      velocity = vector(26000.5, 0, 0),
                      pos      = vector(0, 2.068 * 10e11, 0))

jupiter = SolarObject(mass     = 1.898 * 10e27,
                      velocity = vector(13000.72, 0, 0),
                      pos      = vector(0, 7.943 * 10e11, 0))

saturn  = SolarObject(mass     = 5.683 * 10e26,
                      velocity = vector(10000.18, 0, 0),
                      pos      = vector(0, 1.481 * 10e12, 0))

uranus  = SolarObject(mass     = 8.681 * 10e25,
                      velocity = vector(7000.11, 0, 0),
                      pos      = vector(0, 2.997 * 10e12, 0))

neptune = SolarObject(mass     = 1.024 * 10e26,
                      velocity = vector(5000.5, 0, 0),
                      pos      = vector(0, 4.492 * 10e12, 0))

# WHOA the asteroids
ceres   = SolarObject(mass     = 9.47 * 10e20,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 3.852 * 10e11, 0))

vesta   = SolarObject(mass     = 2.59 * 10e20,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 3.218 * 10e11, 0))

pallas  = SolarObject(mass     = 2.11 * 10e20,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 3.189 * 10e11, 0))

hygiea  = SolarObject(mass     = 8.67 * 10e19,
                      velocity = vector(10, 0, 0),
                      pos      = vector(0, 4.144 * 10e11, 0))

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

    G = 6.67 * 10e-11
    dist = mag(a.pos - b.pos)**2
    if dist == 0:
        return 0 # The objects were the same
    else:
        return G * a.mass * b.mass / (1.0 * dist)

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

while True:
    step_solar_system()
