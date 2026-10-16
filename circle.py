import math


# Вычисляет площадь круга по радиусу r.
# Пример вызова: round(area(2), 2) -> 12.57.
def area(r):
    """Возвращает площадь круга: pi * r * r."""
    return math.pi * r * r


# Вычисляет длину окружности по радиусу r.
# Пример вызова: round(perimeter(3), 2) -> 18.85.
def perimeter(r):
    """Возвращает длину окружности: 2 * pi * r."""
    return 2 * math.pi * r
