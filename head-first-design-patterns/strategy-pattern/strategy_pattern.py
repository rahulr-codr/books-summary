from abc import ABCMeta, abstractmethod

class FlyBehaviour(meta=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def fly(self):
        pass

class NoFlyBehaviour(FlyBehaviour):

    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print("I cannot fly")

class NormalFlyBehaviour(FlyBehaviour):

    def __init__(self) -> None:
        super().__init__()

    def fly(self):
        print("I'm flying normally")

class Duck(meta=ABCMeta):
    
    def __init__(self) -> None:
        self.fly_behaviour: FlyBehaviour = NoFlyBehaviour()

    def swim(self):
        print("Swim")

    def quack(self):
        print("quack")

    def fly(self):
        print("flying")

    def set_fly_behaviour(self, fly_behaviour: FlyBehaviour):
        self.fly_behaviour = fly_behaviour

    @abstractmethod
    def display():
        pass


class RubberDuck(Duck):

    def __init__(self) -> None:
       super().__init__()
    
    def display(self):
        print("I'm a rubber duck")

    def fly(self):
        print("I do not fly")

class MallardDuck(Duck):

    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("I'm a mallard duck")

    def fly(self):
        print("I do not fly")


class RedheadDuck(Duck):

    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("I'm a red head duck")


if __name__ == "__main__":
    
    rubber_duck: Duck = RubberDuck()
    rubber_duck.display()
    rubber_duck.fly() # calls no fly behaviour

    red_head_duck: Duck = RedheadDuck()
    red_head_duck.set_fly_behaviour(NormalFlyBehaviour())
    red_head_duck.fly() # calls fly behaviour



