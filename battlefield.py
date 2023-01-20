from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur("Blue",35)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print("Welcome to Battleworld! A battle for the ages is about to commence")
        print('')

    def battle_phase(self):
       
        fighter_alive = True
        while fighter_alive == True:
            while self.robot.health >0 and self.dinosaur.health >0:
                self.robot.attack(self.dinosaur)
                self.dinosaur.attack(self.robot)
                if self.robot.health <= 0:
                      fighter_alive = False
                      print('')
                      print(f'{self.dinosaur.name} defeated {self.robot.name}. {self.dinosaur.name} is the winner!')
                elif self.dinosaur.health <=0:
                          fighter_alive =False
                          print('')
                          print(f'{self.robot.name} defeated {self.dinosaur.name}. {self.robot.name} is the winner!')
                


    def display_winner(self):
        pass

            
