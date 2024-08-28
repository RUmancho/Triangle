import Check

while True:
    sides = []
    i = 0

    while i < 3:
        getSide = input("Введите сторону треугольника: ")
        try:
            sides.append(float(getSide))
            i += 1
        except:
            print("Неверный формат данных")
    print()

    if Check.isTriangle(sides):
        equilateral = Check.equilateral(sides)
        isosceles = Check.isosceles(sides)
        rightTriangle = Check.rightTriangle(sides)
        if equilateral:
            print("Ваш треугольник равносторонний\n")
            continue  # ? равносторонний треугольник не может быть равноб. и прямоуг.

        if isosceles:
            print("Ваш треугольник равнобедренный")

        if rightTriangle:
            print("Ваш треугольник прямоугольный")

        if all([equilateral, isosceles, rightTriangle]):
            print("Ваш треугольник произвольный")
    else:
        print("Такого треугольника быть не может")
    print()
