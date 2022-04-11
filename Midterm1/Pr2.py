"""
Let’s go back to Christmas time. We will decorate christmas trees using a decorator design
pattern. You should have a ChristmasTree class, the main purpose of which is to print “This is a
christmas tree {christmas tree id}. I am decorated with: ”, the christmas tree id should be given
in the class constructor. You should also have a TreeDecorator class and 3 different specific
decorators: ChristmasStar (which should add a string “star” at the end of the output of the
ChristmasTree), Garland (which should add a string “garland” at the end of the output of the
ChristmasTree) and Lights (which should add a string “lights” at the end of the output of the
ChristmasTree). You can add any additional functionality.
Make sure to test your code with some input.
"""

from abc import ABC, abstractmethod
import time


class BaseChristmasTree(ABC):
    @abstractmethod
    def shine(self):
        pass


class ChristmasTree(BaseChristmasTree):
    def __init__(self, id_):
        self.id = id_

    def shine(self):
        return f"This is a christmas tree {self.id}. I am decorated with: "


class ChristmasTreeDecorator(BaseChristmasTree):
    _component: BaseChristmasTree = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def shine(self):
        return self._component.shine()


class ChristmasStar(ChristmasTreeDecorator):
    def shine(self):
        return self.component.shine() + " star "


class Garland(ChristmasTreeDecorator):
    def shine(self):
        return self.component.shine() + " garland "


class Lights(ChristmasTreeDecorator):
    def shine(self):
        return self.component.shine() + " lights "


def client_code(xmastree):
    print(f"\nChristmas tree decoration:\n{xmastree.shine()}")


if __name__ == "__main__":
    simple_tree = ChristmasTree(id_="14")

    print("Simple tree case.")
    client_code(simple_tree)
    print("\nLet's decorate our tree!")
    print("*" * 10)

    star = ChristmasStar(simple_tree)
    lights = Lights(star)
    garland = Garland(lights)
    print("Aaaand the result")
    for char in "....":
        print(char, end="", sep="\n")
        time.sleep(0.25)

    client_code(garland)
