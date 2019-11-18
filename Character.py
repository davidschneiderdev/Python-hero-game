
class Character:

    def is_alive(self):
        if self.health > 0:
            return True

    def attack(self, enemy):
        enemy.health -= self.power

    def print_status(self):
        print(f"{self.title} has {self.health} health and {self.power} power.")
