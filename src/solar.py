from collections import namedtuple
import visual as v

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
