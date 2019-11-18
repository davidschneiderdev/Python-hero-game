
from Character import Character

class Zombie(Character):

    def __init__(self, title="The Zombie",health=10000, power=10000):
        self.title = title
        self.health = health
        self.power = health