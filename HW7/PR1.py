"""
Imagine that you have the following scenario: you have a file containing some text,
in case the text contains the word "error", you want to log it as an error using the
 ErrorLogger, otherwise, if the text contains the word "file", you should log something in
 a new file using the FileLogger, otherwise, if its not one of the 2 cases, you need to log
 something in the console, using the ConsoleLogger. Feel free to simulate the work of the loggers
 however you wish, you don't even have to actually wrote something in the file, just differentiate
 the 3 operations in some way. The actions of logging can be simple print statements, they just
 need to be different for error logs, console logs and file logs. You need to implement this
 logic using chain of responsibility design pattern and classes of your choice. You may (or may not)
 use the diagram below as a guide.

"""
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def log(self, message):
        pass


class BaseLogger(Logger):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def log(self, message):
        if self._next_handler:
            self._next_handler.log(message)

        return None


class ErrorLogger(BaseLogger):
    def log(self, message):
        if "error" in message.lower():
            return f"[!]* ERROR MESSAGE\n{message}\n[i]*"
        else:
            return super().log(message)


class FileLogger(BaseLogger):
    def log(self, message):
        if "file" in message.lower():
            return f"Writing to file...\n{message}\nFinish!"
        else:
            return super().log(message)


class ConsoleLogger(BaseLogger):
    def log(self, message):
        if any(x in message.lower() for x in ["error", "file"]):
            return "*" * 5, "\nOutputting in console\n", message
        else:
            return super().log(message)


def client_code(logger):
    messages = ["File",
                "Error",
                "Registered"]

    for message in messages:
        result = logger.log(message)
        if result:
            print(result)
        else:
            print(f"'{message}' is  not logged", end="\n")


if __name__ == "__main__":
    error_logger = ErrorLogger()
    file_logger = FileLogger()
    console_logger = ConsoleLogger()

    error_logger.set_next(file_logger).set_next(console_logger)
    print("Chain: ErrorLogger> FileLogger> ConsoleLogger")
    client_code(error_logger)

    print("Chain: FileLogger> ConsoleLogger")
    client_code(file_logger)
