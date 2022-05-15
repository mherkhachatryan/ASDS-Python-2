"""Follow the diagram below and use Composite Design Pattern to implement and test the logic.
Add any other classes of your choice. The top of your hierchy will be the box which will contain
Instrument Collection which will contain instruments. """

from abc import ABC, abstractmethod


class InstrumentCollection(ABC):
    @abstractmethod
    def make(self):
        pass

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent


class Pen(InstrumentCollection):
    def __init__(self, action):
        self.action = action

    def make(self):
        print(f"Instrument does {self.action}")


class Pencil(InstrumentCollection):
    def __init__(self, action):
        self.action = action

    def make(self):
        print(f"Instrument does {self.action}")


class Rubber(InstrumentCollection):
    def __init__(self, action):
        self.action = action

    def make(self):
        print(f"Instrument does {self.action}")


class Box(InstrumentCollection):
    def __init__(self):
        self._instruments = []

    def make(self):
        for instruments in self._instruments:
            instruments.make()

    def add(self, instrument: InstrumentCollection):
        self._instruments.append(instrument)
        instrument.parent = self

    def remove(self, instrument: InstrumentCollection):
        print(f"Deleting instrument {instrument.__class__.__name__}")
        self._instruments.remove(instrument)
        instrument.parent = None

    def get_children(self, index):
        return self._instruments[index].__class__.__name__


if __name__ == "__main__":
    pen = Pen("draw blue")
    pencil = Pencil("draw black")
    rubber = Rubber("clear")

    top_box = Box()
    top_box.add(pen)
    top_box.add(rubber)

    top_box.make()

    print("first element of instruments")
    print(top_box.get_children(0))

    top_box.remove(pen)
    print("first element of instruments")
    print(top_box.get_children(0))
