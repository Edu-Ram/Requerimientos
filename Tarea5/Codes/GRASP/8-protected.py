class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Dibujando un círculo")


class Square(Shape):
    def draw(self):
        print("Dibujando un cuadrado")


shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()
