"""
Use singleton pattern and classes of your choice.
 Create a structure where you have some resource that has states busy
  and free and 3 users that try to use the resource and change the state to busy while they are using it.
   The resource should be singleton.
   Implement using 2 different methods for singleton implementation that we have discussed.
"""


class Availability:
    # state shared by each instance
    __shared_state = dict()

    # constructor method
    def __init__(self):
        self.__dict__ = self.__shared_state  # stores class attributes
        self.state = 'free'


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        try:
            del SingletonType._instances[cls]
        except KeyError:
            pass


class SingletonAvailability(metaclass=SingletonType):

    def __init__(self, state="free"):
        self.state = state


if __name__ == "__main__":
    av1 = Availability()
    av2 = Availability()
    av3 = Availability()
    print("#" * 30, "Shared states implementation", "#" * 30, sep="\n")
    print("Av1 state: ", av1.state)

    av2.state = "busy"
    print("Av2 state is changed to: ", av2.state)
    if av1.state == "busy":
        print(f"State of av1 changed too as it's shares the state of av2 object")

    # classic singleton
    print("#" * 30, "Classic Implementation", "#" * 30, sep="\n")
    obj1 = SingletonAvailability()
    print("State of obj1: ", obj1.state)

    obj2 = SingletonAvailability(state="busy")
    print(f"State of obj2: {obj2.state}")
    if obj2.state == "free":
        print("Despite of we explicitly changed the object initialization parameter it did not changed")

    obj2.state = "free"
    print(f"Obj2 state is: {obj2.state}")
    if obj2.state == "free":
        print("Despite of we explicitly changed the object attribute it did not changed")
