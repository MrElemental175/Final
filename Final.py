
"""


TBC
    Class Characters
        Player will choose a character (Each Character has a unique skill)
            Knight
                Shield Bash
            Rogue
                Assassinate
            Mage
                Fireball
            Paladin
                Smite
        Each Character will have different stats
            Knight
                Armor:3
                HP: 30
                Hit Chance: 50
                Max Damage: 8
            Rogue
                Armor: 1
                HP:20
                Hit Chance: 75
                Max Damage: 6
            Mage
                Armor: 0
                HP: 20
                Hit Chance: 90
                Max Damage: 8
            Paladin
                Armor: 5
                HP: 40
                Hit Chance: 30
                Max Damage: 12
    Combat
        Turn Based Combat where player has three options:
            Attack
                Player will attempt to hit enemy
                Chance to hit is predetermined by the character
                Damage is predetermined by the character
            Skill
                Each Character has a unique skill
                Can only be used once every 4 rounds
                Damage is predetermined by the character
            Heal
                Restores 1 - 4 HP
        Player goes up against one of four enemies:
            Orc
                Armor: 3
                HP: 25
                Hit Chance: 50
                Max Damage: 10
            HobGoblin
                Armor: 2
                HP: 20
                Hit Chance: 60
                Max Damage: 8
            Skeleton
                Armor: 1
                HP: 20
                Hit Chance: 70
                Max Damage: 8
            Minotaur
                Armor: 5
                HP: 30
                Hit Chance: 30
                Max Damage: 15
    
"""

import random

class Character:
    def __init__(self, name, armor, hp, hit_chance, max_damage, skill_name, skill_damage):
        self.name = name
        self.armor = armor
        self.hp = hp
        self.max_hp = hp
        self.hit_chance = hit_chance
        self.max_damage = max_damage
        self.skill_name = skill_name
        self.skill_damage = skill_damage
        self.skill_cooldown = 0

    def attack(self, enemy):
        damage = random.randint(1, self.max_damage)
        if random.randint(1, 100) <= self.hit_chance:
            enemy.take_damage(damage)
            print(f"{self.name} hits {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name} misses!")

    def use_skill(self, enemy):
        if self.skill_cooldown == 0:
            self.skill_cooldown = 4
            damage = self.skill_damage
            enemy.take_damage(damage)
            print(f"{self.name} uses {self.skill_name} on {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s {self.skill_name} is on cooldown!")

    def heal(self):
        healed_amount = random.randint(1, 4)
        self.hp = min(self.max_hp, self.hp + healed_amount)
        print(f"{self.name} heals for {healed_amount} HP!")

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.armor)
        self.hp = max(0, self.hp - actual_damage)
        print(f"{self.name} takes {actual_damage} damage. {self.name}'s HP: {self.hp}/{self.max_hp}")

    def is_dead(self):
        return self.hp == 0

class Enemy(Character):
    pass

def choose_character():
    print("Choose your character:")
    print("1. Knight")
    print("2. Rogue")
    print("3. Mage")
    print("4. Paladin")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        return Character("Knight", 3, 30, 50, 8, "Shield Bash", 10)
    elif choice == '2':
        return Character("Rogue", 1, 20, 75, 6, "Assassinate", 8)
    elif choice == '3':
        return Character("Mage", 0, 20, 90, 8, "Fireball", 12)
    elif choice == '4':
        return Character("Paladin", 5, 40, 30, 12, "Smite", 15)
    else:
        print("Invalid choice. Please try again.")
        return choose_character()

def choose_enemy():
    enemies = [
        Enemy("Orc", 3, 25, 50, 10, "", 0),
        Enemy("HobGoblin", 2, 20, 60, 8, "", 0),
        Enemy("Skeleton", 1, 20, 70, 8, "", 0),
        Enemy("Minotaur", 5, 30, 30, 15, "", 0)
    ]
    return random.choice(enemies)

def display_stats(player, enemy):
    print("\n*** Battle Stats ***")
    print(f"{player.name} (HP: {player.hp}/{player.max_hp}, Armor: {player.armor})")
    print(f"{enemy.name} (HP: {enemy.hp}/{enemy.max_hp}, Armor: {enemy.armor})")
    print("*******************\n")

def main():
    print("Welcome to Monster Slayer!")

    while True:
        player = choose_character()

        enemy = choose_enemy()

        print(f"\nYou encounter a {enemy.name}!\n")

        while not player.is_dead() and not enemy.is_dead():
            display_stats(player, enemy)
            print("Your turn:")
            print("1. Attack")
            print("2. Use Skill")
            print("3. Heal")
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                player.attack(enemy)
            elif choice == '2':
                player.use_skill(enemy)
            elif choice == '3':
                player.heal()
            else:
                print("Invalid choice. Please try again.")
                continue

            enemy.attack(player)


            if player.skill_cooldown > 0:
                player.skill_cooldown -= 1

        if player.is_dead():
            print("\nYou were defeated. Game over!")
        else:
            print("\nCongratulations! You defeated the enemy!")

        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() != 'y':
            break

if __name__ == "__main__":
    main()


