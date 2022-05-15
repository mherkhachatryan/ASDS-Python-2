from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def create_account(self):
        pass


class PersonalAccount(BankAccount):
    def create_account(self):
        return "Personal Account Successfully Created!"


class BusinessAccount(BankAccount):
    def create_account(self):
        return "Business Account Successfully Created!"


class Creator(ABC):
    @abstractmethod
    def choose_account(self, account_type):
        pass


class BankAccountFactory(Creator):
    def __init__(self):
        self.account_container = {"business": BusinessAccount(),
                                  "personal": PersonalAccount()}

    def choose_account(self, account_type):
        return self.account_container.get(account_type.lower())


class Client:
    def __init__(self, account_type):
        account = BankAccountFactory().choose_account(account_type)

        self.account_info = account.create_account()


if __name__ == "__main__":
    personal = Client("personal")
    business = Client("business")
    assert personal.account_info == "Personal Account Successfully Created!"
    assert business.account_info == "Business Account Successfully Created!"
