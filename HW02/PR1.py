from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def create_id(self, id):
        pass

    @abstractmethod
    def create_balance(self, balance):
        pass

    @abstractmethod
    def create_rate(self, rate):
        pass


class ConcreteBuilder(Builder):

    def __init__(self):
        self.account = BankAccount()

    def create_id(self, id_):
        self.account.add_id(id_)

    def create_balance(self, balance):
        self.account.add_balance(balance)

    def create_rate(self, rate):
        self.account.add_rate(rate)


class BankAccount:

    def __init__(self):
        self.id_ = []
        self.balance = []
        self.rate = []

    def add_id(self, part):
        self.id_.append(part)

    def add_balance(self, part):
        self.balance.append(part)

    def add_rate(self, part):
        self.rate.append(part)

    def list_account(self):
        print(f"{self.id_}: Balance: {self.balance}, Rate: {self.rate}")


if __name__ == "__main__":
    builder = ConcreteBuilder()
    builder.create_id("12")
    builder.create_rate("12")
    builder.create_balance("1400")

    builder.account.list_account()
