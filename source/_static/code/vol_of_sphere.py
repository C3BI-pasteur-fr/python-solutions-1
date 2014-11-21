import math

def vol_of_sphere(radius):
    """
    compute the volume of sphere of a given radius
    """
    
    vol = float(4)/float(3) * float(math.pi) * pow(radius, 3)
    return vol
