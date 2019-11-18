from Hero import Hero

from Goblin import Goblin

from Zombie import Zombie

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    hero = Hero()
    goblin = Goblin()
    zombie = Zombie()
    enemy = zombie

    while enemy.is_alive() and hero.is_alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            print("You do %d damage to the enemy." % hero.power)
            if not enemy.is_alive():
                print("The enemy is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.is_alive():
            # Goblin attacks hero
            enemy.attack(hero)
            print("The enemy does %d damage to you." % goblin.power)
            if not hero.is_alive():
                print("You are dead.")

main()
