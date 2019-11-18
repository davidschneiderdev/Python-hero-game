"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)    

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def attack(self, enemy):
        double_damage = random.random() <= 0.2
        if double_damage:
            print("%s attack was very effective! Double damage points dealt to %s." % (self.name, enemy.name))
            enemy.receive_damage(self.power * 2)
            time.sleep(1.5)
        else:
            super().attack(enemy)

class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, 6, 2, 0)

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 8, 1, 0)

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super().attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 7, 2, 15)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        apply_elixir = random.random() <= 0.2
        if apply_elixir:
            self.health += 2
            print("Magic elixir applied! You received 2 health points.")
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name, 12, 3, 20)
    
    def receive_damage(self, points):
        take_hit = random.random() <= 0.1
        if take_hit:
            self.health -= points
            print("%s received %d damage." % (self.name, points))
            if not self.is_alive():
                print("Oh no! %s is dead." % self.name)
        else:
            print("Shadow evaded attack.")

class Zombie(Character):
    def __init__(self, name):
        super().__init__(name, 8, 3, 0)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("Oh no! %s is still alive (and will continue to attack!)" % self.name)

    def is_alive(self):
        return True

class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("%s faces the %s" % (hero.name, enemy.name))
        print("=====================")
        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.is_alive():
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class Sword:
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero('Lancelot')
enemies = [Zombie('Undertaker'), Wizard('Jethro')]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
