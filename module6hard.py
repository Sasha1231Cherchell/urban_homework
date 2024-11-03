import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.filled = filled
        self.__sides = sides
        self.__color = (0, 0, 0)
        self.set_color(*color)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in [r, g, b]:
            if i < 0 or i > 255:
                return False
        return  True

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            return
        self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if type(side) != int or side < 1:
                return  False
        return True

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        new_sides = list(sides)
        if len(sides) != self.sides_count:
            new_sides = [1 for i in range(self.sides_count)]
        super().__init__(new_sides, color, True)
        self.__radius = new_sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        new_sides = list(sides)
        if len(sides) != self.sides_count:
            new_sides = [1 for i in range(self.sides_count)]
        super().__init__(new_sides, color, True)

    def get_square(self):
        sides = super().__sides
        p = sum(sides) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side_value = 1
        if len(sides) == 1:
            side_value = sides[0]
        new_sides = [side_value for i in range(self.sides_count)]
        super().__init__(new_sides, color, True)

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
