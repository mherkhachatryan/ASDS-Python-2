"""
Use adapter pattern and classes of your choice. Create a structure where you
have 1-2 adaptees that have a method that returns some text in spanish.
Have an adapter which will have a method that translates the text to english.
Have examples of the usage of your class structure.
"""


class SpanishLegacy:

    def message(self):  # noqa
        return "Plato o plomo"


class EnglishVersion:

    def proverb(self):
        return "silver or gold"


class Adapter(SpanishLegacy, EnglishVersion):

    def message(self):
        return f"Translation from Spanish: {self.proverb()}"


def client_code(message: SpanishLegacy):
    return message.message()


if __name__ == "__main__":
    print("In old version we used Spanish")
    spanish = SpanishLegacy()
    print(client_code(spanish))

    print("\nNow we use english support")
    adaptee = Adapter()
    print(client_code(adaptee))
