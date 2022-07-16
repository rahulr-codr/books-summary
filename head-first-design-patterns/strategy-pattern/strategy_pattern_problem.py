from abc import ABCMeta, abstractmethod

class Duck(meta=ABCMeta):
    
    def __init__(self) -> None:
        pass

    def swim():
        print("Swim")

    def quack():
        print("quack")

    def fly():
        print("flying")

    @abstractmethod
    def display():
        pass


class RubberDuck(Duck):

    def __init__(self) -> None:
       super().__init__()
    
    def display():
        print("I'm a rubber duck")

    def fly():
        print("I do not fly")

class MallardDuck(Duck):

    def __init__(self) -> None:
        super().__init__()

    def display():
        print("I'm a mallard duck")

    def fly():
        print("I do not fly")


class RedheadDuck(Duck):

    def __init__(self) -> None:
        super().__init__()

    def display():
        print("I'm a red head duck")


if __name__ == "__main__":
    
    rubber_duck: Duck = RubberDuck()
    rubber_duck.display()
    rubber_duck.fly()

