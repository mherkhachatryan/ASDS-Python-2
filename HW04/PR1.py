"""Let say you want to send a message to someone.
You have 2 options - you can Email the message or SMS the message
to the corresponding person. So, you have two options
to send the message and the client side code will use one of
the implementations to send the message to the corresponding person.
Use Bridge Design Pattern to implement the logic with classes of your
choice and make sure to test the implementation with some concrete objects.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class MessageTransfer:
    def __init__(self, operator):
        self.operator = operator

    def send_message(self, message):
        print(f"message was sent successfully, operator info:\n"
              f"{self.operator.transfer_data(message)}")


class Operator(ABC):
    @abstractmethod
    def transfer_data(self, message):
        pass


class Email(Operator):
    def transfer_data(self, message):
        return f"{datetime.now()} : msg: {message} : Operator name {self.__class__.__name__}"


class SMS(Operator):
    def transfer_data(self, message):
        return f"{datetime.now()} : msg: {message} : Operator name {self.__class__.__name__} : Cost per message - 25"


if __name__ == "__main__":
    email = Email()
    sms = SMS()

    mt = MessageTransfer(email)
    mt.send_message("Hello world")
    print("*" * 100, end="\n\n")
    sms_mt = MessageTransfer(sms)
    sms_mt.send_message("This is mobile version")
