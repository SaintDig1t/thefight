import random

player_health = 100
enemy_health = 100

print("Welcome to the Fight! You have 100 health points. Defeat the enemy to win the game.\n")

while player_health > 0 and enemy_health > 0:
    print("Your health:", player_health)
    print("Enemy health:", enemy_health)

    player_choice = input("What do you want to do? (attack/heal) ")

    if player_choice == "attack":
        damage = random.randint(10, 20)
        enemy_health -= damage
        print("You dealt", damage, "damage to the enemy.")
    elif player_choice == "heal":
        heal_amount = random.randint(10, 20)
        player_health += heal_amount
        print("You healed for", heal_amount, "health points.")
    else:
        print("Invalid choice. Try again.")
        continue

    if enemy_health <= 0:
        print("You defeated the enemy! Congratulations!")
    else:
        enemy_damage = random.randint(5, 15)
        player_health -= enemy_damage
        print("The enemy dealt", enemy_damage, "damage to you.")

if player_health <= 0:
    print("Game over. You lost.")
