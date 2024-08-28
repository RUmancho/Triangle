def isTriangle(sides: list):
    """проверка на треугольник"""
    if len(sides) != 3:
        return False

    # & длина стороны > 0
    for side in sides:
        if side <= 0:
            return False

    # * длина любой стороны в треугольнике
    # * должны быть меньше чем сумма 2-х остальных
    for side1 in sides:
        summ = 0
        for side2 in sides:
            summ += side2
        summ -= side1

        if summ <= side1:
            return False
    return True


def isosceles(sides: tuple):
    """равнобедренный треугольник?"""
    for side in sides:
        if sides.count(side) == 2:
            return True
    return False


def equilateral(sides: tuple):
    """равносторонний треугольник?"""
    return sides.count(sides[0]) == 3


def rightTriangle(sides: list):
    """прямоугольный треугольник?"""
    hypotenuse = round(max(sides), 2)
    i = 0
    for side in sides:
        if side == hypotenuse:
            del sides[i]
            break
        i += 1

    summ = sides[0] * sides[0] + sides[1] * sides[1]
    return round(pow(summ, 0.5), 2) == hypotenuse
