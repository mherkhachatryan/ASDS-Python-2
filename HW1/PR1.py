from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        return "Circle has 0 corners"


class Square(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        return "Square has 4 corners"


class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        return "Triangle has 3 corners"


class Creator(ABC):
    @abstractmethod
    def choose_shape(self, shape):
        pass


class ShapeFactory(Creator):
    def __init__(self):
        self.shape_container = {"triangle": Triangle(),
                                "circle": Circle(),
                                "square": Square()}

    def choose_shape(self, shape):
        return self.shape_container.get(shape.lower())


class Client:
    def __init__(self, shape):
        self.shape = shape
        shape_factory = ShapeFactory()
        circle = shape_factory.choose_shape(self.shape)

        self.output = circle.draw()


if __name__ == "__main__":
    client1 = Client("Square")
    client2 = Client("Circle")
    client3 = Client("Triangle")
    assert client1.output == "Square has 4 corners"
    assert client2.output == "Circle has 0 corners"
    assert client3.output == "Triangle has 3 corners"

