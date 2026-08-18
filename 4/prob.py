class Shape:
    def __init__(self):
        print("I am a shape")

    def calc_area(self):
        print(0)

    def calc_perimeter(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        print("I am also a square")

    def calc_area(self):
        print(self.length * self.length)

    def calc_perimeter(self):
        print(4 * self.length)


sh = Shape()
sh.calc_area()
sh.calc_perimeter()

sq = Square(5)
sq.calc_area()
sq.calc_perimeter()