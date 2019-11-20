"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20, bounty=5, armor=0, evade=0, swap=False, items=[]):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.bounty = bounty
        self.armor = armor
        self.evade = evade
        self.swap = swap
        self.items = []

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        if self.swap:
            self.swap_attack(enemy)
        else:
            print("%s attacks %s" % (self.name, enemy.name))
            enemy.receive_damage(self.power)
            time.sleep(1.5)
    
    def swap_attack(self, enemy):
        self.power, enemy.power = enemy.power, self.power
        print(f"Swap talisman traded the power of {self.name} with {enemy.name}'s power!")
        print("%s attack was ALSO very effective! Double damage points dealt to %s." % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        self.power, enemy.power = enemy.power, self.power
        print("**The power of the swap talisman has been used up.**")
        print("Powers now traded back.")
        self.swap = False
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

    def print_status(self, enemy):
        if self.swap == True:
            print("%s has %d health and NOW has power of %d." % (self.name, self.health, enemy.power))
        elif enemy.swap == True:
            print("%s has %d health and NOW has power of %d." % (self.name, self.health, enemy.power))
        else:
            print("%s has %d health and %d power." % (self.name, self.health, self.power))

    def print_inventory(self):
        print("--------Item Inventory--------")
        if len(hero.items) == 0:
            print("No items in inventory.")
            print("------------------------------")
            print(f"{self.name} lifts gaze back to battlefield.")
        else:
            i = 0
            for item in hero.items:
                print(f"{i}: {item.name}")
                i += 1
            item_choice = int(input("Enter item number: "))
            return item_choice
            

    def buy(self, item):
        self.coins -= item.cost
        if item.name in ['armor', 'sword', 'evade points']:
            item.apply(hero)
        else:
            hero.items.append(item)
            print(f"{item.name} added to {hero.name}'s inventory.")
    
    def award_bounty(self, enemy):
        self.coins += enemy.bounty
        print(f"{self.name} received {enemy.bounty} coins in bounty for defeating {self.name}.")

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)    

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def swap_attack(self, enemy):
        self.power, enemy.power = enemy.power, self.power
        print(f"Swap talisman traded the power of {self.name} with {enemy.name}'s power!")
        print("%s attack was ALSO very effective! Double damage points dealt to %s." % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        self.power, enemy.power = enemy.power, self.power
        print("**The power of the swap talisman Hashtag  been used up.**")
        print("Powers now traded back.")
        self.swap = False
        time.sleep(1.5)

    def swap_attack_double(self, enemy):
        self.power, enemy.power = enemy.power, self.power
        print(f"Swap talisman traded the power of {self.name} with {enemy.name}'s power!")
        print(f"")
        print("%s attacks %s" % (self.name, enemy.name))
        double_points = self.power * 2
        enemy.receive_damage(double_points)
        self.power, enemy.power = enemy.power, self.power
        print("**The power of the swap talisman has been used up.**")
        print("Powers now traded back.")
        self.swap = False
        time.sleep(1.5)

    def attack(self, enemy):
        double_damage = random.random() <= 0.2
        if double_damage:
            if self.swap == True:
                self.swap_attack_double(enemy)
            else:
                print("%s attack was very effective! Double damage points dealt to %s." % (self.name, enemy.name))
                double_points = self.power * 2
                print(double_points)
                enemy.receive_damage(double_points)
                time.sleep(1.5)
        else:
            super().attack(enemy)

    # def equip_armor(self, boolean=False):
    #     self.armor = boolean
    
    def receive_damage(self, points):
        evade_chance = random.random() <= (0.05 * self.evade)
        # print(f"evade_chance = {evade_chance}")
        if evade_chance:
            print("Hero evaded attack and took no damage!")  
        else:      
            reduced_points = points - self.armor
            self.health -= reduced_points
            print("%s received %d damage." % (self.name, reduced_points))
            if not self.is_alive():
                print("Oh no! %s is dead." % self.name)


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
            print("Oh no! %s is STILL alive (and will continue to attack!)" % self.name)

    def is_alive(self):
        return True

class Elf(Character):
    def __init__(self, name):
        super().__init__(name, 7, 4, 10)

    def attack(self, enemy):
        precision_arrow = random.random() < 0.33
        if precision_arrow:
            print("%s landed a precision arrow! Double damage points dealt to %s." % (self.name, enemy.name))
            enemy.receive_damage(self.power * 2)
            time.sleep(1.5)
        else:
            super().attack(enemy)

    def receive_damage(self, points):
        eagle_eye = random.random() < 0.33
        if eagle_eye:
            print("%s used Eagle Eye to avoid attack from %s! Zero damage taken." % (self.name, enemy.name))
        else:
            super().receive_damage(points)

class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("%s faces the %s" % (hero.name, enemy.name))
        print("=====================")
        while hero.is_alive() and enemy.is_alive():
            hero.print_status(enemy)
            enemy.print_status(hero)
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. use item")
            print("3. do nothing")
            print("4. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
                enemy.attack(hero)
            elif user_input == 2:
                item_choice = hero.print_inventory()
                # print(item_choice)
                    # item_choice = int(input("Enter item number: "))
                try:
                    ItemToApply = hero.items[item_choice]
                    # print(ItemToApply)
                    ItemToApply.apply(hero)
                    if hero.swap == True:
                        print("**Power of swap talisman activated for this turn**")
                        pass
                except TypeError:
                    pass
                    # print(ItemToApply.name)
            elif user_input == 3:
                enemy.attack(hero)
            elif user_input == 4:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
        if hero.is_alive():
            print("You defeated %s" % enemy.name)
            hero.award_bounty(enemy)
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
        character.items.remove(self)


class SuperTonic:
    cost = 8
    name = 'super tonic'
    def apply(self, character):
        character.health = 10
        print("%s's health increased back to %d." % (character.name, character.health))
        character.items.remove(self)

class Armor:
    cost = 10
    name = 'armor'
    def apply(self, character):
        hero.armor += 2
        print(f"{hero.name}'s armor increased by 2.")

class Sword:
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Evade:
    cost = 5
    name = 'evade points'
    def apply(self, hero, cost=5):
        if hero.evade < 18:
            hero.evade += 2
            print(f"{hero.name} evade skillset increased by 2 points.")
            print(f"Total evade points equal {hero.evade}.")
        else:
            hero.coins += cost
            print("You have maxed out your evade points. Coins have been returned to you.")

class Swap:
    cost = 7
    name = 'swap talisman'
    def apply(self, hero):
        hero.swap = True
        character.items.remove(self)

        

class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Armor, Sword, Evade, Swap]
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
                if hero.coins >= item.cost:
                    hero.buy(item)
                else:
                    print("**Do not have enough coins**")

hero = Hero('Percival')
enemies = [Goblin('Kreten'), Zombie('Zombie')]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
