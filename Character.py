
class Character:

    def __init__(self, title, health, power):
        self.title = title
        self.health = health
        self.power = power
    
    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power

    def print_status(self):
        print(f"{self.title} has {self.health} health and {self.power} power.")
