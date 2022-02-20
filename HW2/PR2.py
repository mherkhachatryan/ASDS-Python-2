from abc import ABCMeta, abstractmethod
import copy


class Shape(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def draw(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Rectangle"

    def draw(self):
        print(f"{self.type} has 4 corners")


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Square"

    def draw(self):
        print(f"{self.type} has 4 corners and equal lengths")


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.type = "Circle"

    def draw(self):
        print(f"{self.type} has 0 corners")


class ShapeCache:
    cache = {}

    @staticmethod
    def get_shape(sid):
        shape = ShapeCache.cache.get(sid, None)
        return shape.clone()

    @staticmethod
    def load():
        circle = Circle()
        circle.set_id("1")
        ShapeCache.cache[circle.get_id()] = circle

        square = Square()
        square.set_id("2")
        ShapeCache.cache[square.get_id()] = square

        rectangle = Rectangle()
        rectangle.set_id("3")
        ShapeCache.cache[rectangle.get_id()] = rectangle


if __name__ == '__main__':
    ShapeCache.load()

    circle = ShapeCache.get_shape("1")
    print(circle.get_type())

    square = ShapeCache.get_shape("2")
    print(square.get_type())

    rectangle = ShapeCache.get_shape("3")
    print(rectangle.get_type())
