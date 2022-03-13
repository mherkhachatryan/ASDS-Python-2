class BasePerson:
    def __init__(self, first_name, last_name, age, email):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def info(self):
        pass


class Person(BasePerson):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)

    def info(self):
        return f"{self.first_name} {self.last_name}: {self.age}"


class InfoOutputDecorator:
    _person: BasePerson = None

    def __init__(self, person: BasePerson) -> None:
        self._person = person

    @property
    def person(self) -> BasePerson:
        return self._person

    def info(self):
        return self._person.info()


class ChildInfoOutputDecorator(InfoOutputDecorator):
    def info(self):
        return f"*** &&& {self.person.first_name} - {self.person.last_name}" \
               f" - {self.person.email} &&& ***"


class AdultInfoOutputDecorator(InfoOutputDecorator):
    def info(self):
        return f"&&& {self.person.first_name} - {self.person.last_name}" \
               f" - {self.person.email} &&&"


def client_code(person):
    if person.age < 14:
        print(ChildInfoOutputDecorator(person).info())
    else:
        print(AdultInfoOutputDecorator(person).info())


if __name__ == "__main__":
    emma = Person("Emma", "Watson", 11, "emmaw@hogwarts.com")

    bane = Person("Bane", "Smith", 32, "agentsmith@gov.com")

    print("Simple info")
    print(bane.info())
    print("\n\n")
    print(emma.info())

    print("\nExamples with decorators")
    client_code(bane)
    print("\n\n")
    client_code(emma)
