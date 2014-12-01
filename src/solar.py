from collections import namedtuple

# mass is in kg and distance is in meters.
SolarObject = namedtuple('SolarObject', ['mass', 'distance'])

# At the center is
sun = SolarObject(1.988 * 10e30, 0)

# The planets
mercury = SolarObject(3.301 * 10e23, 6.751 * 10e10)
venus   = SolarObject(4.873 * 10e24, 1.088 * 10e11)
earth   = SolarObject(5.972 * 10e24, 1.475 * 10e11)
mars    = SolarObject(6.417 * 10e23, 2.068 * 10e11)
jupiter = SolarObject(1.898 * 10e27, 7.943 * 10e11)
saturn  = SolarObject(5.683 * 10e26, 1.481 * 10e12)
uranus  = SolarObject(8.681 * 10e25, 2.997 * 10e12)
neptune = SolarObject(1.024 * 10e26, 4.492 * 10e12)

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
