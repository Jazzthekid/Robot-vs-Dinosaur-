from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = 'Rusty'
        self.health = 100
        self.active_weapon = Weapon("Necrosword")


    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print('')
        print(f'{self.name} attacked {dinosaur.name} for {self.active_weapon.attack_power} damage with {self.active_weapon.name}, leaving {self.name} with {dinosaur.health} health remaining.')