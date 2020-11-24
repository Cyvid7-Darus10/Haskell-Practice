from random import randint
from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def announce(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Lizalflos(Monster):
    def throwBoomerang(self):
        pass
    def hide(self):
        pass

class Moblin(Monster):
    def stab(self):
        pass
    def kick(self):
        pass

class Bokoblin(Monster):
    def bludgeon(self):
        pass
    def defend(self):
        pass

class NormalBokoblin(Bokoblin):
    def bludgeon(self):
        print("Normal bokoblin bludgeons you with a boko club for 1 damage")
    def defend(self):
        print("Normal bokoblin defends itself with a boko shield")
    def announce(self):
        print("A normal bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class NormalMoblin(Moblin):
    def stab(self):
        print("Normal Moblin stabs you with a spear for 3 damage")
    def kick(self):
        print("Normal Moblin kicks you for 1 damage")
    def announce(self):
        print("A normal moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class NormalLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Normal lizalflos throws its lizal boomerang at you for 2 damage")
    def hide(self):
        print("Normal lizalflos camouflages itself")
    def announce(self):
        print("A normal lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class BlueBokoblin(Bokoblin):
    def bludgeon(self):
        print("Blue bokoblin bludgeons you with a spiked boko club for 2 damage")
    def defend(self):
        print("Blue bokoblin defends itself with a spiked boko shield")
    def announce(self):
        print("A blue bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class BlueMoblin(Moblin):
    def stab(self):
        print("Blue moblin stabs you with a rusty halberd for 5 damage")
    def kick(self):
        print("Blue moblin kicks you for 2 damage")
    def announce(self):
        print("A blue moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class BlueLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Blue lizalflos throws its lizal forked boomerang at you for 3 damage")
    def hide(self):
        print("Blue lizalflos camouflages itself")
    def announce(self):
        print("A blue lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class SilverBokoblin(Bokoblin):
    def bludgeon(self):
        print("Silver bokoblin bludgeons you with a dragonbone boko club for 5 damage")
    def defend(self):
        print("Silver bokoblin defends itself with a dragonbone boko shield")
    def announce(self):
        print("A silver bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class SilverMoblin(Moblin):
    def stab(self):
        print("Silver moblin stabs you with a knight's halberd for 10 damage")
    def kick(self):
        print("Silver moblin kicks you for 3 damage")
    def announce(self):
        print("A silver moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class SilverLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Silver lizalflos throws its lizal tri-boomerang at you for 7 damage")
    def hide(self):
        print("Silver lizalflos camouflages itself")
    def announce(self):
        print("A silver lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class Dungeon(ABC):
    @abstractmethod
    def newBokoblin(self):
        pass
    @abstractmethod
    def newMoblin(self):
        pass
    @abstractmethod
    def newLizalflos(self):
        pass

class EasyDungeon(Dungeon):
    def newBokoblin(self):
        return NormalBokoblin()
    def newMoblin(self):
        return NormalMoblin()
    def newLizalflos(self):
        return NormalLizalflos()

class MediumDungeon(Dungeon):
    def newBokoblin(self):
        return BlueBokoblin()
    def newMoblin(self):
        return BlueMoblin()
    def newLizalflos(self):
        return BlueLizalflos()

class HardDungeon(Dungeon):
    def newBokoblin(self):
        return SilverBokoblin()
    def newMoblin(self):
        return SilverMoblin()
    def newLizalflos(self):
        return SilverLizalflos()


class Encounter:
    def __init__(self, dungeon: Dungeon):
        self.__dungeon = dungeon
        self.__enemies = []
        for _ in range(randint(0,8)):
            r = randint(1,3)
            if r == 1:
                self.__enemies.append(self.__dungeon.newBokoblin())
            elif r==2:
                self.__enemies.append(self.__dungeon.newMoblin())
            else:
                self.__enemies.append(self.__dungeon.newLizalflos())

    def announceEnemies(self):
        print("%d monsters appeared" % len(self.__enemies))
        for enemy in self.__enemies:
            enemy.announce()

    def moveEnemies(self):
        for enemy in self.__enemies:
            enemy.move()


easy = EasyDungeon()
medium = MediumDungeon()
hard = HardDungeon()

encounter = Encounter(medium)
encounter.announceEnemies()
print()
encounter.moveEnemies()
