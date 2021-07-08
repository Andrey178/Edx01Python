import math


def polysum(n, s):
    """"
    parameters: n - number of sides, s - side length
    count area of regular polygon with tan and Pi number from imported math
    and sum with square of the perimeter of the polygon
    """
    answer = (0.25*n*(s**2)) / (math.tan(math.pi/n)) + ((n*s)**2)
    return round(answer, 4)
