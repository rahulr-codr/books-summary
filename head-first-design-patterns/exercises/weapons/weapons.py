from abc import ABCMeta, abstractmethod
from tkinter import W


class WeaponBehaviour(meta=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def use_weapon(self):
        pass

class NoWeaponBehaviour(WeaponBehaviour):
    def __init__(self) -> None:
        super().__init__()

    def use_weapon(self):
        print("punch with hands")

class KnifeBehaviour(WeaponBehaviour):

    def __init__(self) -> None:
        super().__init__()

    def use_weapon(self):
        print("cutting with knife")

class BowAndArrowBehaviour(WeaponBehaviour):

    def __init__(self) -> None:
        super().__init__()

    def use_weapon(self):
        print("shooting with bow and arrow")

class AxeBehaviour(WeaponBehaviour):

    def __init__(self) -> None:
        super().__init__()

    def use_weapon(self):
        print("chopping with axe")

class SwordBehaviour(WeaponBehaviour):

    def __init__(self) -> None:
        super().__init__()

    def use_weapon(self):
        print("swinging with sword")

class Character(meta=ABCMeta):

    def __init__(self) -> None:
        self.weapon: WeaponBehaviour = NoWeaponBehaviour()

    def set_weapon(self, weapon_behaviour: WeaponBehaviour):
        self.weapon = weapon_behaviour
    
    def fight(self):
        self.weapon.use_weapon()

class King(Character):

    def __init__(self) -> None:
        super().__init__()

class Queen(Character):

    def __init__(self) -> None:
        super().__init__()

class Knight(Character):

    def __init__(self) -> None:
        super().__init__()

class Troll(Character):

    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":

    king: Character = King()
    knight: Character = Knight()
    troll: Character = Troll()

    #king gets a sword
    king.set_weapon(SwordBehaviour())
    knight.set_weapon(SwordBehaviour())
    troll.set_weapon(AxeBehaviour())
    king.fight()
    knight.fight()
    troll.fight()


