def equilateral(sides):
    if 0 in sides:
        return False
    else:    
        return sides[0] == sides [1] and sides[0] == sides[2]


def isosceles(sides):
    if 0 in sides:
        return False
    else:
        return sorted(sides)[1] == sorted(sides)[2]


def scalene(sides):
    if 0 in sides:
        return False
    return sorted(sides)[0] + sorted(sides)[1] >= sorted(sides)[2] and(sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2])
