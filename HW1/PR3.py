"""In this implementation of the code diagram function names have been refactored to PEP standards
"""

from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def set(self):
        pass


class WinButton(Button):
    def paint(self):
        return "Windows Button"


class MacButton(Button):
    def paint(self):
        return "Mac Button"


class WinCheckbox(Checkbox):
    def set(self):
        return "Windows Checkbox"


class MacCheckbox(Checkbox):
    def set(self):
        return "Mac Checkbox"


class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def create_ui(self):
        return self.button.paint(), self.checkbox.set()


class ApplicationConfig:
    def __init__(self, os):
        self.factory_container = {"windows": WinFactory(),
                                  "mac": MacFactory()}
        self.os = os

    def create_ui(self):
        os_factory = self.factory_container.get(self.os.lower())
        if not os_factory:
            raise ValueError("Unknown OS")

        return Application(os_factory).create_ui()


if __name__ == "__main__":
    mac_run = ApplicationConfig("mac")
    win_run = ApplicationConfig("windows")

    assert mac_run.create_ui() == ('Mac Button', 'Mac Checkbox')
    assert win_run.create_ui() == ('Windows Button', 'Windows Checkbox')
