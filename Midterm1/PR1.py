"""The company gets a project which consists of several tasks (project is a list and each task is of
type string). Each task should be implemented by a specific team, depending on its contents.
The teams are the following: Data Science, Design and QA. Your program should use a chain
of responsibility design pattern. If the given task contains any of the words analyze, research or
model - it should be handled by the Data Science team, if the task contains the words color or
decoration - it should be handled by the Design team, if it contains the word test - it should be
handled by the QA team. You should also have a default handler which will handle the tasks that
don’t fall under the 3 categories.
Sample input is a list similar to this: [‘a model to separate the background’, ‘test the
application’,
etc.]
Make sure to test your code with some input."""

from abc import ABC, abstractmethod
from typing import List, Optional

DATA_TEAM_TERMS = ["analyze", "research", "model"]
QA_TEAM_TERMS = ["test"]
DESIGN_TEAM_TERMS = ["decoration", "color"]
ALL_TERMS = DATA_TEAM_TERMS + QA_TEAM_TERMS + DESIGN_TEAM_TERMS


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, task: str) -> Optional[str]:
        pass


class BaseHandler(Handler):
    _next_handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, task):
        if self._next_handler:
            return self._next_handler.handle(task)


class DataTeam(BaseHandler):
    def handle(self, task: str) -> Optional[str]:
        if any(x in task.lower() for x in DATA_TEAM_TERMS):
            return f"Data Science team will handle this task!: {task}"
        else:
            return super().handle(task)


class QATeam(BaseHandler):
    def handle(self, task: str) -> Optional[str]:
        if any(x in task.lower() for x in QA_TEAM_TERMS):
            return f"QA team will handle this task!: {task}"
        else:
            return super().handle(task)


class DesignTeam(BaseHandler):
    def handle(self, task: str) -> Optional[str]:
        if any(x in task.lower() for x in DESIGN_TEAM_TERMS):
            return f"Design team will handle this task!: {task}"
        else:
            return super().handle(task)


class Management(BaseHandler):
    def handle(self, task: str) -> Optional[str]:
        if all(x not in task.lower() for x in ALL_TERMS):
            return f"Management team will decide whom to handle this task!: {task}"
        else:
            return super().handle(task)


def client_code(handler):
    task_list = ["a model to separate the background",
                 "test the application",
                 "decoration of the product",
                 "buy some cookies for ALL teams!!"]
    for task in task_list:
        result = handler.handle(task)
        if result:
            print(result)
        else:
            print(f"{task} is anter")


if __name__ == '__main__':
    data_team = DataTeam()
    qa_team = QATeam()
    design_team = DesignTeam()
    management = Management()

    print("Chain: management> data_team> qa_team> design_team")
    management.set_next(data_team).set_next(qa_team).set_next(design_team)
    client_code(management)

    print("\n\nSubchain: is qa_team>design_team")
    client_code(qa_team)
